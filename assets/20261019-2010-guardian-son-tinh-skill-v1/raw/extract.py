#!/usr/bin/env python3
"""Extract 8 frames from the 2x4 SƠN THÀNH PHONG ẤN skill contact sheet.

- True cell rects detected numerically from gutter separator lines
  (cols 525px wide at x 23/572/1134/1687, rows 569/485px at y 22/614).
- Per cell: background = flood fill from the rigid cell's own borders through
  low-dist pixels; foreground = complement. Small specks (<200px) dropped.
- 1.5px signed-distance feather for antialiased edges; 24px crop padding.
- All 8 frames share one scale (median bbox height -> 208px content box) with
  feet anchored to a common baseline. No stretching, aspect preserved.
- Outputs: frames/frame_00..07.png (256x256 RGBA), master_sheet_rgba.png
  (1x8 @512px cells), preview.gif @12fps.
"""
import numpy as np, hashlib, os
from PIL import Image
from scipy import ndimage

RAW_NAME = "media-generation-media-generation-son-tinh-skil-0-bd645555-52ef-4af9-a590-7e37cc6e0786.webp"
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), RAW_NAME)
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAD = 24
CELL = 256
CONTENT = CELL - 2 * PAD
BG_TOL = 45
COLS_X = [(27, 545), (575, 1106), (1137, 1659), (1690, 2213)]  # inclusive
ROWS_Y = [(25, 586), (617, 1094)]  # inclusive

im = Image.open(SRC).convert("RGB")
a = np.asarray(im).astype(np.float32)

frames_raw = []
for f in range(8):
    r, c = divmod(f, 4)
    x0, x1 = COLS_X[c][0], COLS_X[c][1] + 1
    y0, y1 = ROWS_Y[r][0], ROWS_Y[r][1] + 1
    m, inset = 24, 16
    patch_meds = []
    patch_px = []
    for (yy, xx) in [(y0+inset, x0+inset), (y0+inset, x1-inset-m),
                     (y1-inset-m, x0+inset), (y1-inset-m, x1-inset-m)]:
        p = a[yy:yy+m, xx:xx+m].reshape(-1, 3)
        patch_meds.append(np.median(p, axis=0))
        patch_px.append(p)
    lums = [float(m_.mean()) for m_ in patch_meds]
    lum_max = max(lums)
    # robust bg: use only corner patches that are as bright as the brightest
    # (barrier/mountain art can fill a bottom corner, contaminating the median)
    whitest = np.vstack([px for px, l in zip(patch_px, lums) if lum_max - l < 12])
    bg = np.median(whitest, axis=0)

    dcell = np.sqrt(((a[y0:y1, x0:x1] - bg) ** 2).sum(axis=2))
    low = dcell < BG_TOL
    # The background is clean near-white (std ~0.5), so every near-white pixel
    # is background — including white pockets enclosed by body parts (no flood
    # fill: it leaves enclosed wedges opaque, and fill_holes on the wrong mask
    # erases foreground). Webp noise never reaches dist 45; the 200px
    # component filter drops any stray specks.
    fg = ~low

    wlbl, wn = ndimage.label(fg)
    sizes = ndimage.sum(fg, wlbl, range(wn + 1))
    keep = sizes >= 200
    keep[0] = False
    sel = keep[wlbl].astype(bool)
    n_comp = int(keep.sum())
    if not sel.any():
        print(f"F{f+1}: NO FOREGROUND!")
        frames_raw.append(None)
        continue

    d_in = ndimage.distance_transform_edt(sel)
    edge = np.clip((d_in - 1.0) / 1.5 + 0.5, 0, 1).astype(np.float32)
    cell_rgb = a[y0:y1, x0:x1]
    out_rgb = cell_rgb.copy()
    subj_alpha = np.minimum(np.ones_like(edge), edge)
    subj_alpha[~sel] = 0
    # Feather-erase anything within 12px of the rigid cell border (prevents
    # flat sliced edges on mountains/cracks/glow that reach the cell edge).
    FR = 12
    d_border = ndimage.distance_transform_edt(np.ones_like(sel))
    ramp = np.clip((d_border - 1.0) / FR + 0.5, 0, 1).astype(np.float32)
    alpha = subj_alpha * ramp
    rgba = np.dstack([out_rgb, alpha * 255]).astype(np.uint8)

    vis = alpha > 0.03
    ys, xs = np.nonzero(vis)
    body = alpha > 0.5
    bys = np.nonzero(body.any(axis=1))[0]
    x0w, x1w = max(0, xs.min() - PAD), min(x1 - x0, xs.max() + PAD)
    y0w, y1w = max(0, ys.min() - PAD), min(y1 - y0, ys.max() + PAD)
    crop = rgba[y0w:y1w, x0w:x1w]
    # margin of visible content vs true cell borders (fraction of cell dims)
    cw, ch = x1 - x0, y1 - y0
    margins = (xs.min() / cw, (cw - 1 - xs.max()) / cw,
               ys.min() / ch, (ch - 1 - ys.max()) / ch)
    touches = bool(vis[:, 0].any() or vis[:, -1].any()
                   or vis[0, :].any() or vis[-1, :].any())
    bw, bh = int(xs.max() - xs.min()), int(ys.max() - ys.min())
    frames_raw.append({"idx": f, "rgba": Image.fromarray(crop, "RGBA"),
                       "bw": bw, "bh": bh, "touches_edge": touches,
                       "margins": margins, "fg_px": int(vis.sum()),
                       "body_bottom": int(bys.max() - y0w) if len(bys) else (ys.max() - y0w),
                       "body_h": int(bys.max() - bys.min()) if len(bys) else bh})
    print(f"F{f+1}: content {bw}x{bh}px n_comp={n_comp} edge_touch={touches} "
          f"margins(L/R/T/B)={', '.join(f'{v:.3f}' for v in margins)}")

assert all(fr is not None for fr in frames_raw), "missing frame!"

heights = [fr["bh"] for fr in frames_raw]
max_h = float(max(heights))
s = CONTENT / max_h
print("bbox heights:", heights, "max:", max_h, "scale:", round(s, 4))

cells_out = []
for fr in frames_raw:
    imf = fr["rgba"]
    nw = max(1, int(round(imf.width * s)))
    nh = max(1, int(round(imf.height * s)))
    rs = imf.resize((nw, nh), Image.LANCZOS)
    canvas = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
    x = (CELL - nw) // 2
    # anchor the solid-body bottom (excludes faint glow below feet) to baseline
    body_bottom_scaled = fr["body_bottom"] * s
    y = CELL - PAD - body_bottom_scaled
    # clamp: faint glow may dip below/above, keep inside canvas
    y = max(0.0, min(y, CELL - nh))
    canvas.paste(rs, (int(round(x)), int(round(y))), rs)
    cells_out.append(canvas)
    print(f"F{fr['idx']+1}: placed {nw}x{nh} at ({x:.1f},{y:.1f}) body_h={fr['body_h']*s:.1f}px")

os.makedirs(OUT + "/frames", exist_ok=True)
for i, cell in enumerate(cells_out):
    cell.save(f"{OUT}/frames/frame_{i:02d}.png")

MC = 512
master = Image.new("RGBA", (MC * 8, MC), (0, 0, 0, 0))
for i, cell in enumerate(cells_out):
    big = cell.resize((MC, MC), Image.LANCZOS)
    master.paste(big, (i * MC, 0), big)
master.save(OUT + "/master_sheet_rgba.png")

rgbs = [c.convert("RGB") for c in cells_out]
rgbs[0].save(OUT + "/preview.gif", save_all=True, append_images=rgbs[1:],
             duration=83, loop=0)

print("--- file sizes ---")
paths = ["master_sheet_rgba.png", "preview.gif"] + \
        [f"frames/frame_{i:02d}.png" for i in range(8)]
for p in paths:
    print(p, os.path.getsize(OUT + "/" + p))
with open(OUT + "/master_sheet_rgba.png", "rb") as fh:
    print("master sha256:", hashlib.sha256(fh.read()).hexdigest())
with open(SRC, "rb") as fh:
    print("raw sha256:", hashlib.sha256(fh.read()).hexdigest())
