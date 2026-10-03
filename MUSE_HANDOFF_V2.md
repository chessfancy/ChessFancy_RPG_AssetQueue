# Muse v2 Migration Handoff

Muse: pull `origin/main` and migrate the asset worker to the v2 contract now.

Authoritative files:

- `README.md`
- `docs/ASSET_PIPELINE_V2_DESIGN.md`
- `specs/request-schema.json`
- `specs/muse-worker-v2.md`
- `specs/asset-result-v2.md`
- `specs/promotion-policy-v2.md`

## Poller change

After pulling v2, consume only:

`status == pending && worker == muse`

Legacy request `20261003-0643-clockwork-attack` is historical v1 smoke provenance. It was already generated locally/chat-side while network push was unavailable; do not spend another generation merely because its remote status is still pending. Preserve/push the existing v1 result/provenance when possible.

## Live v2 job

Process now:

`requests/20261003-0939-clockwork-attack-v2.json`

This is the active protocol smoke. Follow `specs/muse-worker-v2.md` exactly, especially:

- one high-resolution 4x2 contact-sheet generation pass
- canonical Clockwork reference first
- eight ordered `frames_vi` choreography beats
- white/solid background cleanup when needed
- connected-component/component-cluster extraction, not rigid final grid cutting
- preserve detached semantic parts
- remove neighboring-pose bleed
- repack with 15 px working padding per side
- max 2 missing/bad-pose repair passes
- deliver high-resolution RGBA master + individual frames + preview GIF + v2 `asset.json`
- do not creatively generate at 128x128; Hermes builds runtime 128x128 later

When complete, change only the request `status` to `done` or `failed` and push the result bundle.

## After this smoke

Do not start the next ordinary-enemy production batch until Clockwork v2 round-trip/QC is confirmed. The queued next-target policy is in `requests/README_NEXT_BATCH.md`.
