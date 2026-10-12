# Windmill Runaway v2 — manual assembly v3 FINAL (2026-10-12)

Teacher QC rules (2026-10-12): (1) keep ONLY clips where the windmill stands on
the circular stone platform — drop any clip without the base; (2) delete frames
with 5 blades or 3 blades; (3) drop sea/river/lake backgrounds, keep
mountains/clouds.

## Clip verdicts (teacher's 5-clip Flow package)
- seg_wide.mp4 (8s): base YES, no sea, 4 blades sharp in all 32 sampled frames.
  KEEP.
- seg_continue_a.mp4: base YES but river/sea background -> DROP (rule 3).
- seg_continue_b.mp4: river background + loses base mid-clip (morph) -> DROP.
- seg_suddenly_a.mp4: mountains OK but NO base -> DROP (rule 1).
- seg_suddenly_b.mp4: NO base + river -> DROP.
- Fresh malfunction generation (2026-10-12, Veo 3.1 Lite, 10 credits):
  seg_malfunction.mp4 (8s) — base YES in all frames, mountains/clouds, NO water,
  4 blades sharp/countable in all 64 sampled frames (8fps), no 5-blade or
  3-blade frames found. KEEP.

## Cut plan (final: windmill_runaway_v3_final_16s.mp4, 16.0s, 1280x720@24fps)
- Part A (0.0-8.0s): seg_wide — normal operation, wide cinematic pan.
- HARD CUT at 8.0s (deliberate camera-angle change).
- Part B (8.0-16.0s): seg_malfunction — slow push-in, sudden counterclockwise
  runaway, ends at full runaway spin.
- Watermark: Veo text removed per-part BEFORE joining (the remover truncated a
  12.5s single-pass assembly to 10s on the previous attempt, so parts are
  cleaned separately). Audio stripped (brief: no audio).

## Caveats
- Counterclockwise direction of the runaway spin cannot be verified from the
  blurred frames.
- No blade-morph frames existed, so no individual frames were deleted; the fix
  was clip selection per the teacher's rules.
