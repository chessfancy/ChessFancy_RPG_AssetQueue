#!/usr/bin/env python3
"""Extract 8 frames from 2x4 contact sheet (v5, final approach).

- True cell rects detected numerically from gutter bands (the sheet is NOT an
  equal 560 grid: cols ~527px, rows 508/535px).
- Per cell: background = flood fill from the rigid cell's own borders through
  low-dist pixels (BG_TOL). Foreground = complement -> warm-tan skin stays
  fully opaque. Gutters are wide and verified empty, so the rigid cell alone
  is used (the expanded window admitted gutter-gray webs).
- 1.5px signed-distance feather for antialiased edges; 24px crop padding.
- Full-body frames F5..F8 share one scale (median bbox height -> 208px) with
  feet anchored; partial-manifestation frames F1..F4 use the same scale,
  vertically centered. No stretching, aspect preserved.
- Outputs: frames/frame_00..07.png (256x256 RGBA), master_sheet_rgba.png
  (1x8 @512px cells), preview.gif @12fps.
"""
import numpy as np, hashlib, os
from PIL import Image
from scipy import ndimage

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "media-generation-son-tinh-summon-contact-sheet-0-f4f2be44-6294-4d0f-bbc8-dac19427264c.png")
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAD = 24
CELL = 256
CONTENT = CELL - 2 * PAD
BG_TOL = 45
COLS_X = [(20, 547), (578, 1104), (1135, 1662), (1692, 2218)]  # inclusive
ROWS_Y = [(22, 529), (559, 1093)]  # inclusive

im = Image.open(SRC).convert("RGB")
a = np.asarray(im).astype(np.float32)

frames_raw = []
for f in range(8):
    r, c = divmod(f, 4)
    x0, x1 = COLS_X[c][0], COLS_X[c][1] + 1
    y0, y1 = ROWS_Y[r][0], ROWS_Y[r][1] + 1
    m, inset = 24, 16
    corners = np.vstack([
        a[y0+inset:y0+inset+m, x0+inset:x0+inset+m].reshape(-1, 3),
        a[y0+inset:y0+inset+m, x1-inset-m:x1-inset].reshape(-1, 3),
        a[y1-inset-m:y1-inset, x0+inset:x0+inset+m].reshape(-1, 3),
        a[y1-inset-m:y1-inset, x1-inset-m:x1-inset].reshape(-1, 3),
    ])
    bg = np.median(corners, axis=0)

    dcell = np.sqrt(((a[y0:y1, x0:x1] - bg) ** 2).sum(axis=2))
    low = dcell < BG_TOL
    seed = np.zeros_like(low, bool)
    seed[0, :] = seed[-1, :] = seed[:, 0] = seed[:, -1] = True
    seed &= low
    n_seed = int(seed.sum())
    background = ndimage.binary_propagation(seed, mask=low)
    fg = ~background

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
    # TRUE mist un-keying: the source is white mist over gray bg, so the real
    # mist alpha is (lum-bg)/(255-bg) and its color un-premultiplies to white.
    # This keeps broad faint haze faint on ANY background instead of turning
    # into a glaring white slab. Low saturation required so the warm cream
    # skirt (sat~30) and gold are protected; only neutral-white haze qualifies.
    # Everything else (skin, costume, staff, dark mist) stays fully opaque.
    cell_rgb = a[y0:y1, x0:x1]
    lum = cell_rgb.mean(axis=2)
    sat = cell_rgb.max(axis=2) - cell_rgb.min(axis=2)
    bg_lum = float(bg.mean())
    # mist halo: neutral-white haze within 12px of the fg mass (kills isolated
    # bg specks); alpha follows the true un-keyed fade so the fringe dissolves
    # instead of cutting at the flood-fill boundary
    halo = ndimage.binary_dilation(sel, iterations=12)
    mist_zone = halo & (lum > bg_lum + 8) & (sat < 25) & (dcell < 130)
    a_mist = np.clip((lum - bg_lum) / (255 - bg_lum), 0, 1).astype(np.float32)
    a_mist[a_mist < 0.04] = 0
    a3 = a_mist[..., None]
    fg_rgb = (cell_rgb - (1 - a3) * bg) / np.maximum(a3, 1e-3)
    fg_rgb = np.clip(fg_rgb, 0, 255)
    out_rgb = np.where(mist_zone[..., None], fg_rgb, cell_rgb)
    subj_alpha = np.minimum(np.ones_like(edge), edge)
    subj_alpha[~sel] = 0
    alpha = np.maximum(subj_alpha, np.where(mist_zone, a_mist, 0).astype(np.float32))
    rgba = np.dstack([out_rgb, alpha * 255]).astype(np.uint8)

    vis = alpha > 0.03
    ys, xs = np.nonzero(vis)
    x0w, x1w = max(0, xs.min() - PAD), min(x1 - x0, xs.max() + PAD)
    y0w, y1w = max(0, ys.min() - PAD), min(y1 - y0, ys.max() + PAD)
    crop = rgba[y0w:y1w, x0w:x1w]
    touches = bool(vis[:, 0].any() or vis[:, -1].any()
                   or vis[0, :].any() or vis[-1, :].any())
    bw, bh = int(xs.max() - xs.min()), int(ys.max() - ys.min())
    frames_raw.append({"idx": f, "rgba": Image.fromarray(crop, "RGBA"),
                       "bw": bw, "bh": bh, "touches_edge": touches,
                       "fg_px": int(vis.sum())})
    print(f"F{f+1}: seed={n_seed} content {bw}x{bh}px n_comp={n_comp} edge_touch={touches}")

assert all(fr is not None for fr in frames_raw), "missing frame!"

heights = [fr["bh"] for fr in frames_raw[4:]]
med_h = float(np.median(heights))
s = CONTENT / med_h
print("full-body heights F5..F8:", heights, "median:", med_h, "scale:", round(s, 4))

cells_out = []
for fr in frames_raw:
    imf = fr["rgba"]
    nw = max(1, int(round(imf.width * s)))
    nh = max(1, int(round(imf.height * s)))
    rs = imf.resize((nw, nh), Image.LANCZOS)
    canvas = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
    x = (CELL - nw) // 2
    y = CELL - PAD - nh if fr["idx"] >= 4 else (CELL - nh) // 2
    canvas.paste(rs, (x, y), rs)
    cells_out.append(canvas)
    assert nw <= CELL and nh <= CELL, f"F{fr['idx']+1} overflow {nw}x{nh}"
    print(f"F{fr['idx']+1}: placed {nw}x{nh} at ({x},{y})")

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
