# Muse Worker v2 Contract

This document is the operational contract for Muse jobs in AssetQueue v2.

## Polling and ownership

After migration, Muse consumes only requests where:

- `status == "pending"`
- `worker == "muse"`

Legacy requests without `worker` may be handled explicitly during migration, but must not become the permanent polling rule.

Muse may change only the request `status` field. All generated files belong under `assets/<job-id>/`.

## Supported routes

### `external_reference_first`
Use the repository reference paths in `reference_images` and any `character_spec_path`. Preserve identity exactly except for explicit `identity_overrides`.

### `muse_self_reference`
Create a canonical-reference candidate first. Ordinary enemies under `enemy_auto` may continue automatically after QC. Boss/guardian identities must stop at candidate-ready until human approval.

## Choreography

For animation work, read `frames_vi[]` in order. Treat the list as the requested movement beats, not optional prose.

Prefer one high-resolution contact-sheet generation pass for the sequence so identity, palette, scale and details remain coherent.

Preferred layouts:

- 8 frames: 4x2
- 12 frames: 4x3
- 16 frames: 4x4

Avoid long 8x1 / 16x1 creative-generation layouts unless explicitly justified.

## Generation prompt contract

Prompt for:

- same identity as canonical reference
- strict logical grid
- one pose per logical cell
- wide gutter
- no touching / overlap / crop
- full body and important weapon/parts visible
- consistent facing/camera
- stable apparent scale
- no text, watermark, UI or scenery unless requested
- simple removable white/solid background is acceptable

Runtime `128x128` / `192x192` cell sizes are delivery targets only. Keep the creative/master generation substantially larger.

## Background cleanup

Do not fail only because the model returns white instead of alpha.

Preferred cleanup:

1. derive foreground mask from alpha or keyed white/solid background
2. preserve antialiased edge pixels
3. export RGBA master assets

## Frame discovery and extraction

Do not trust rigid equal-grid cuts as the final crop.

Preferred sequence:

1. foreground mask
2. connected-component or component-cluster detection
3. discard tiny noise
4. associate detached semantic fragments (tail, tassel, weapon/FX) with the correct pose
5. order pose groups by logical reading order
6. compare detected count to requested frame count
7. crop actual pose groups with safe margin
8. remove neighboring-pose contamination

## Repair policy

Preserve good poses. Repair only missing/bad poses while carrying forward canonical reference and prior good sheet as style context.

Maximum repair passes: **2**.

If the request still cannot satisfy the required pose count/identity after two repair passes, set `status: failed` and explain the reason in result metadata.

## Re-spacing and normalization

Default extra working padding is **15 px per side** unless overridden.

Normalize without stretching:

- visible body scale
- feet/root baseline
- center placement
- safety margin
- aspect ratio

The high-resolution master is authoritative; Hermes performs final runtime downsample/atlas packing.

## Required delivery bundle

Preferred `assets/<job-id>/` contents:

- `master_sheet_rgba.png`
- `frames/frame_00.png` ...
- `preview.gif`
- `asset.json`

If individual frames are explicitly disabled, omit the `frames/` folder but retain enough metadata to reproduce extraction.

Raw AI generation may stay outside Git when large, but preserve snapshot id / SHA256 / dimensions in `asset.json` when available.

## QC before `done`

Muse checks at least:

- requested frame count satisfied
- canonical identity preserved
- readable choreography
- correct facing/camera
- no true body/weapon crop
- no neighboring-frame bleed
- background cleanup usable
- high-resolution master exists

`status: done` means the worker bundle is complete. It does **not** mean production promotion.
