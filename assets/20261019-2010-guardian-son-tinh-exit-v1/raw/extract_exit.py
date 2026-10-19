#!/usr/bin/env python3
"""Extract 8 exit-sequence frames from the contact sheet.

Layout is NOT a uniform grid: top row has 6 cells (we use first 4),
bottom row has 4 cells. Cell rects detected numerically from vertical
white gutter bands present at all scanlines. Digits in cell top-left
corners are masked out before segmentation. Mist is recovered with true
alpha un-keying (same method as the summon job). One shared scale for
all frames; F1-F5 feet-anchored, F6-F8 vertically centered (fragments).
"""
import numpy as np, hashlib, os
from PIL import Image
from scipy import ndimage

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "media-generation-son-tinh-exit-contact-sheet-0-c6c9ddde-946a-4684-8d7d-65a3eb9f2fbe.webp")
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAD = 24            # extra_padding_px from request
CELL = 256
CONTENT = CELL - 2 * PAD
BG_TOL = 45

# (x0, x1_exclusive) per cell; top-row cells A..D, bottom-row cells A..D
TOP_X = [(43, 421), (437, 756), (768, 1111), (1132, 1453)]
BOT_X = [(43, 562), (576, 1111), (1132, 1657), (1691, 2198)]
ROWS = [(34, 651), (679, 1083)]  # (y0, y1_exclusive)

FRAMES = []  # (row, col) for F1..F8
FRAMES += [(0, c) for c in range(4)]
FRAMES += [(1, c) for c in range(4)]
CELL_X = [TOP_X, BOT_X]

im = Image.open(SRC).convert("RGB")
a = np.asarray(im).astype(np.float32)
print("source:", im.size, "sha256:", hashlib.sha256(open(SRC, "rb").read()).hexdigest())

frames_raw = []
for f, (r, c) in enumerate(FRAMES):
    x0, x1 = CELL_X[r][c]
    y0, y1 = ROWS[r]
    cw, ch = x1 - x0, y1 - y0
    cell = a[y0:y1, x0:x1]

    # bg from corners
    m, inset = 24, 16
    corners = np.vstack([
        a[y0+inset:y0+inset+m, x0+inset:x0+inset+m].reshape(-1, 3),
        a[y0+inset:y0+inset+m, x1-inset-m:x1-inset].reshape(-1, 3),
        a[y1-inset-m:y1-inset, x0+inset:x0+inset+m].reshape(-1, 3),
        a[y1-inset-m:y1-inset, x1-inset-m:x1-inset].reshape(-1, 3),
    ])
    bg = np.median(corners, axis=0)

    # digit mask: dark components inside the top-left corner box only
    lum = cell.mean(axis=2)
    dbox = np.zeros_like(lum, bool)
    dbox[4:62, 4:48] = True
    cand = (lum < 140) & dbox
    dlbl, dn = ndimage.label(cand)
    digit_mask = np.zeros_like(lum, bool)
    if dn:
        sizes = ndimage.sum(cand, dlbl, range(1, dn + 1))
        big = int(np.argmax(sizes)) + 1
        if sizes[big - 1] < 2000:
            digit_mask = dlbl == big
            print(f"F{f+1}: masked digit ({int(sizes[big-1])}px)")

    dcell = np.sqrt(((cell - bg) ** 2).sum(axis=2))
    low = (dcell < BG_TOL) | digit_mask
    seed = np.zeros_like(low, bool)
    seed[0, :] = seed[-1, :] = seed[:, 0] = seed[:, -1] = True
    seed &= low
    background = ndimage.binary_propagation(seed, mask=low)
    fg = ~background

    wlbl, wn = ndimage.label(fg)
    sizes = ndimage.sum(fg, wlbl, range(wn + 1))
    keep = sizes >= 200
    keep[0] = False
    sel = keep[wlbl].astype(bool)
    n_comp = int(keep.sum())
    print(f"F{f+1}: fg components n={n_comp}", end=" ")

    sat = cell.max(axis=2) - cell.min(axis=2)
    bg_lum = float(bg.mean())
    halo = ndimage.binary_dilation(sel, iterations=12) if sel.any() else np.zeros_like(sel)
    mist_zone = halo & (lum > bg_lum + 8) & (sat < 25) & (dcell < 130)
    if not mist_zone.any():
        # mist-only fallback (F8): any faint neutral haze not connected to border
        mist_zone = (lum > bg_lum + 6) & (sat < 25) & (dcell < 130) & ~background
        mist_zone &= ndimage.binary_dilation(ndimage.binary_erosion(mist_zone, iterations=3), iterations=3)
    a_mist = np.clip((lum - bg_lum) / (255 - bg_lum), 0, 1).astype(np.float32)
    a_mist[a_mist < 0.04] = 0
    a3 = a_mist[..., None]
    fg_rgb = np.clip((cell - (1 - a3) * bg) / np.maximum(a3, 1e-3), 0, 255)
    out_rgb = np.where(mist_zone[..., None], fg_rgb, cell)

    if sel.any():
        d_in = ndimage.distance_transform_edt(sel)
        subj_alpha = np.clip((d_in - 1.0) / 1.5 + 0.5, 0, 1).astype(np.float32)
        subj_alpha[~sel] = 0
    else:
        subj_alpha = np.zeros_like(a_mist)
    alpha = np.maximum(subj_alpha, np.where(mist_zone, a_mist, 0).astype(np.float32))
    rgba = np.dstack([out_rgb, alpha * 255]).astype(np.uint8)

    vis = alpha > 0.03
    touches = False
    if vis.any():
        ys, xs = np.nonzero(vis)
        x0w, x1w = max(0, xs.min() - PAD), min(cw, xs.max() + PAD)
        y0w, y1w = max(0, ys.min() - PAD), min(ch, ys.max() + PAD)
        crop = rgba[y0w:y1w, x0w:x1w]
        touches = bool(vis[:, 0].any() or vis[:, -1].any() or vis[0, :].any() or vis[-1, :].any())
        bw, bh = int(xs.max() - xs.min()), int(ys.max() - ys.min())
        print(f"content {bw}x{bh}px edge_touch={touches} vis={int(vis.sum())}")
    else:
        crop = rgba  # whole cell, mist only
        bw = bh = 0
        print("NO fg content -> full-cell mist frame")
    frames_raw.append({"idx": f, "rgba": Image.fromarray(crop, "RGBA"),
                       "bw": bw, "bh": bh, "touches_edge": touches,
                       "vis": int(vis.sum())})

# shared scale from full-body frames F1..F4 (idx 0..3)
heights = [fr["bh"] for fr in frames_raw[:4]]
med_h = float(np.median(heights))
s = CONTENT / med_h
print("F1..F4 heights:", heights, "median:", round(med_h, 1), "scale:", round(s, 4))

cells_out = []
for fr in frames_raw:
    imf = fr["rgba"]
    nw = max(1, int(round(imf.width * s)))
    nh = max(1, int(round(imf.height * s)))
    rs = imf.resize((nw, nh), Image.LANCZOS)
    canvas = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
    x = (CELL - nw) // 2
    y = CELL - PAD - nh if fr["idx"] <= 4 else (CELL - nh) // 2
    assert nw <= CELL and nh <= CELL, f"F{fr['idx']+1} overflow {nw}x{nh}"
    canvas.paste(rs, (x, y), rs)
    cells_out.append(canvas)
    print(f"F{fr['idx']+1}: placed {nw}x{nh} at ({x},{y})")

os.makedirs(OUT + "/frames", exist_ok=True)
for i, cell_im in enumerate(cells_out):
    cell_im.save(f"{OUT}/frames/frame_{i:02d}.png")

MC = 512
master = Image.new("RGBA", (MC * 8, MC), (0, 0, 0, 0))
for i, cell_im in enumerate(cells_out):
    big = cell_im.resize((MC, MC), Image.LANCZOS)
    master.paste(big, (i * MC, 0), big)
master.save(OUT + "/master_sheet_rgba.png")

rgbs = [c.convert("RGB") for c in cells_out]
rgbs[0].save(OUT + "/preview.gif", save_all=True, append_images=rgbs[1:],
             duration=83, loop=0)

print("--- files ---")
paths = ["master_sheet_rgba.png", "preview.gif"] + \
        [f"frames/frame_{i:02d}.png" for i in range(8)]
for p in paths:
    print(p, os.path.getsize(OUT + "/" + p))
with open(OUT + "/master_sheet_rgba.png", "rb") as fh:
    print("master sha256:", hashlib.sha256(fh.read()).hexdigest())
