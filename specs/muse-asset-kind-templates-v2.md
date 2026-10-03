# Muse Asset Kind Templates v2

This document standardizes four reusable Muse production asset kinds. `requests/*.json` remain the executable queue; this file defines how to author them consistently.

## 1. `skill_animation`
Use for the character/enemy animation row itself. Preserve canonical identity exactly. The row may contain light motion trails or small self-glow, but large target impact effects and persistent status visuals should be separate assets.

Required guidance:
- high-resolution master first; runtime 128x128 comes later;
- detailed `frames_vi[]` choreography;
- explicit `fps`;
- compact generation grid such as 4x2 for 8 frames;
- canonical reference + style bible;
- `timing_hints` for cast start, peak/contact, effect spawn, recovery, and optional status application.

Typical result: `master_sheet_rgba.png`, individual frames, preview GIF, `asset.json`.

## 2. `self_vfx`
Use for isolated transparent VFX composited on the caster: charge aura, core glow, weapon/root buildup, foot dust, or similar.

Rules:
- do not include the full character in the VFX asset;
- include an anchor such as `caster_center` or `caster_feet`;
- keep regular-enemy VFX small/medium and below boss/guardian spectacle;
- do not obscure the caster silhouette when composited;
- palette must match the related skill animation.

Typical size: 128x128 runtime target, generated from a larger master.

## 3. `hit_pack`
Use for isolated impact VFX spawned at the target: slash burst, life-drain pulse, root latch, dust/shock impact, etc.

Rules:
- no full character or background plate;
- include an anchor such as `target_center` or `target_feet`;
- impact peak must be obvious and short-lived;
- one-shot drain must end cleanly and must not resemble a persistent DoT;
- DoT application hit packs should communicate latch/infestation rather than consuming the whole effect in one pulse.

Typical size: 192x192 runtime target, generated from a larger master.

## 4. `status_loop`
Use only for persistent visual status indicators that remain after an effect is applied.

Rules:
- transparent isolated effect only;
- seamless loop is mandatory;
- final frame must return naturally to the starting state;
- no progressive size drift or brightness escalation;
- do not obscure the target;
- gameplay duration/tick logic remains in code; this asset is visual-only.

Typical size: 128x128 runtime target; 6 frames at about 8 fps unless the request says otherwise.

## Shared production rules
1. `requests/*.json` is the executable queue. Muse changes only `status` in request files.
2. Generate at high resolution first. Do not creatively generate directly at runtime resolution.
3. Prefer one high-resolution contact sheet to preserve identity, then segment by component clusters, de-bleed, normalize, and repack.
4. Use at least 15 px working padding unless a request overrides it.
5. Maximum repair passes: 2. Repair only missing/bad poses, not the whole sheet unless identity is globally broken.
6. Export transparent RGBA masters and preview GIFs at the requested playback rate.
7. Regular enemies may auto-promote after QC. Boss and Guardian assets remain manual review.
8. Walking/running locomotion should use the video pipeline unless explicitly overridden; Muse image-sheet production is preferred for bounded combat poses and VFX.

## Recommended dependency contract
VFX requests should reference the related skill request with:
- `depends_on_request`: request id;
- `dependency_policy`: `skip_until_done`.

Muse should leave a dependent request `pending` until the prerequisite request is `done`, then use the committed skill master/preview as motion and palette references.
