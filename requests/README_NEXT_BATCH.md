# Next Muse Batch — Chapter 2

Current live protocol smoke:

`20261003-0939-clockwork-attack-v2`

Do **not** create additional pending production requests until this v2 job proves the migrated Muse round trip and QC/result contract.

## Legacy v1 handling

`20261003-0643-clockwork-attack` is historical v1 smoke provenance. Muse already produced a local/chat-side result while network push was unavailable; do not regenerate it merely because the remote request still appears pending. When possible, preserve/push its existing provenance/result or mark the historical attempt failed/rejected according to the worker-side record, without overwriting it into v2.

## After Clockwork v2 passes

Queue ordinary Chapter 2 enemies under `enemy_auto`:

1. Mộc Linh — Muse may use `muse_self_reference` or an external ChatGPT/Codex reference if one is supplied; canonical identity may auto-lock after QC.
2. Gấu Rừng — same ordinary-enemy automatic policy.
3. Rễ Cuồng — same ordinary-enemy automatic policy.
4. Xương Cuồng / Mộc Tinh — **boss_manual**; canonical identity requires user approval before production promotion.

## Locomotion rule

Do not use Muse image-sheet generation for walk/run cycles. Route locomotion through the video-to-animation pipeline.

## Production rule

`status: done` means the worker bundle is complete. Hermes still performs technical/runtime QC before automatic ordinary-enemy promotion.
