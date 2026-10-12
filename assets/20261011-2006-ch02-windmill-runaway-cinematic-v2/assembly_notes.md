# Windmill Runaway v2 — manual assembly (2026-10-12)

Source package: teacher's Flow download (5 clips, "Untitled_Scene_10-12_02_59_38").

## Analysis
- seg_wide.mp4 (8s): Map-3-correct location, normal operation, blades sharp. KEEP.
- seg_continue_a/b, seg_suddenly_a/b (7s each): location drifted (river / snowy
  mountains; continue_b morphs river->mountains mid-clip). DROPPED.
- Original first-gen clip (windmill_runaway_v2_veo31_lite_raw.mp4, 8s, Map 3):
  rotor-crop analysis at 12fps over t=4-8s shows blades NEVER morph/disappear;
  the "missing blade" the teacher saw was heavy motion blur during the runaway
  acceleration, which is physically natural. No frame deletion needed.

## Cut plan (final: windmill_runaway_v2_final_12s.mp4, 12.5s, 1280x720@24fps)
- Part A (0.0-8.0s): seg_wide, full — normal operation, wide cinematic pan.
- HARD CUT at 8.0s (deliberate camera-angle change, per teacher's direction).
- Part B (8.0-12.5s): original clip t=3.5-8.0 — slowing (~0.5s) -> stopped tense
  beat (~2s) -> sudden runaway blur (~2s).
- Watermark: Veo text removed per-part (tool truncated a 12.5s single pass to
  10s, so parts were cleaned separately then joined). Audio stripped (brief: no audio).

## Caveat
- Counterclockwise direction of the runaway spin cannot be verified from the
  blurred frames; same limitation as the first-gen QC.
