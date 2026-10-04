# Muse Production Queue

This file is the human-readable production board for Muse. The executable queue remains `requests/*.json`: Muse should poll pending request files and produce bundles under `assets/<request-id>/`.

## Operating rules
- Poll `requests/` every normal cycle and execute `status: pending` jobs targeted to `worker: muse`.
- Use `specs/request-schema.json`, `specs/muse-worker-v2.md`, and `specs/muse-asset-kind-templates-v2.md`.
- Preserve canonical identity from `references/canonical/...` and the request's `reference_images`.
- Generate high-resolution masters first; do not creatively generate at runtime 128x128.
- Maximum repair passes: 2. Repair only bad/missing poses where possible.
- Muse changes only request `status`; results go to `assets/<request-id>/` with `asset.json` and requested previews/frames.
- Regular enemies use `enemy_auto`; bosses and Guardians require manual approval.
- Walking/running locomotion stays on the video pipeline unless explicitly overridden.

## Completed foundation
- Clockwork Knight attack v2 round-trip: DONE / QC PASS.
- Canonical references: Gấu Rừng, Mộc Linh, Rễ Cuồng: DONE / approved regular-enemy identities.
- Base attacks for all three: DONE.
- Specials for all three: DONE.
- Special VFX bundles for all three: DONE.
  - Mộc Linh: one-shot HP-drain visual language.
  - Rễ Cuồng: HP-drain-over-time application + status-loop visual language.
  - Gấu Rừng: physical heavy-slam visual language.

## ACTIVE EXECUTABLE WAVE — poll and process now
### Idle
1. `20261003-1721-gau-rung-idle`
2. `20261003-1721-moc-linh-idle`
3. `20261003-1721-re-cuong-idle`

### Hurt
4. `20261003-1722-gau-rung-hurt`
5. `20261003-1722-moc-linh-hurt`
6. `20261003-1722-re-cuong-hurt`

### KO
7. `20261003-1723-gau-rung-ko`
8. `20261003-1723-moc-linh-ko`
9. `20261003-1723-re-cuong-ko`

All nine request JSON files already exist under `requests/` with `status: pending`. Process them as normal production jobs; do not wait for another human handoff.

## NEXT PLANNED WAVE — do not invent requests yourself
After the active wave is delivered and QC is clean, Hermes/ChatGPT may issue:
- `enemy_gau_rung.attack.hit_pack`
- `enemy_moc_linh.attack.hit_pack`
- `enemy_re_cuong.attack.hit_pack`

Optional attack self-VFX should be issued only if visual review shows the normal attack rows need extra readability. Do not add them automatically.

## MANUAL-REVIEW LANE
Do not auto-create or auto-promote these:
- Xương Cuồng boss canonical/reference and all boss animation/VFX bundles — `boss_manual`.
- Guardian/Sơn Tinh new production animation/VFX bundles — `guardian_manual`.

## Remaining pipeline work outside Muse generation
Hermes/game integration still owns:
- final runtime downsample/atlas build;
- frame timing/event hooks;
- damage/heal/status logic;
- Mộc Linh one-shot drain gameplay;
- Rễ Cuồng damage-over-time duration/ticks/stacking;
- hit-pack/status-loop spawning and cleanup;
- runtime battle QC.

## Queue policy
`MUSE_QUEUE.md` is planning/index documentation, not a substitute for request files. Muse must never generate a planned item that has no `requests/<id>.json`. If a request is present and pending, process it; if it has dependencies, obey its dependency gate; if it is done/failed, do not duplicate it.

## CH4 CANDIDATE IDENTITY WAVE — executable, non-canon
These are deliberately over-provisioned regular-enemy identity candidates for the future Chapter 4 rewrite **CHIẾN TRƯỜNG GIÓ NỔI**. Sol/story may later use any subset. Muse should create canonical-reference candidates only; do not invent full animation jobs without new request JSON.

1. `20261004-1703-ch04-co-tan-reference` — Cờ Tàn
2. `20261004-1703-ch04-giap-rong-reference` — Giáp Rỗng
3. `20261004-1703-ch04-dieu-chien-reference` — Diều Chiến
4. `20261004-1703-ch04-no-gio-reference` — Nỏ Gió
5. `20261004-1703-ch04-khien-gio-reference` — Khiên Gió
6. `20261004-1703-ch04-chien-xa-cu-reference` — Chiến Xa Cũ
7. `20261004-1703-ch04-binh-nom-reference` — Binh Nộm
8. `20261004-1703-ch04-ken-lenh-reference` — Kèn Lệnh

All eight request JSON files exist with `worker=muse`, `status=pending`, `approval_policy=enemy_auto`, and `reference_mode=muse_self_reference`. Their shared art direction is `style-bibles/chapter04/README.md`; the broader library including legacy candidates is `docs/worldbuilding/ch04/ENEMY_CANDIDATE_POOL.md`.

