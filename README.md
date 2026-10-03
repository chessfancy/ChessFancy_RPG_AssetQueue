# ChessFancy RPG Asset Queue

Public handoff repository for the ChessFancy RPG multi-worker asset pipeline.

Authoritative design: `docs/ASSET_PIPELINE_V2_DESIGN.md`

## Layout

- `requests/` — requester/Hermes creates immutable-versioned job JSON files.
- `assets/` — workers write generated result bundles under `assets/<job-id>/`.
- `specs/` — request/result contracts, worker instructions, examples.
- `references/` — canonical/style/action references.
- `style-bibles/` — durable global/chapter art direction.
- `docs/worldbuilding/` — screenplay-to-world coordination, connected-map plans and cross-worker art handoffs.
- future `reviews/` / `promotions/` — QC and production-promotion records.

## Ownership

- Hermes/requester may create `requests/` and `references/` content.
- Workers must not rewrite requester fields in an existing request; they may change only `status` to `done` or `failed`.
- Muse owns Muse-generated bundles under `assets/<job-id>/` and Muse-maintained worker/spec documents.
- Neither side overwrites another worker's owned result bundle.
- No generator writes directly to the game production runtime tree.

## Request lifecycle

1. Requester validates `requests/<job-id>.json` against `specs/request-schema.json`.
2. Request is pushed with `status: pending`.
3. Target worker consumes the request.
4. Worker creates a candidate bundle under `assets/<job-id>/` with provenance metadata.
5. Worker changes only request `status` to `done` or `failed` and pushes.
6. Hermes performs technical QC/runtime integration; visual QC follows the request's approval policy.
7. `done` means worker delivery completed. It does **not** mean production approval.
8. Rejected/failed work remains as provenance; fixes use a new versioned request id.

## Worker routing (v2)

New requests should set `protocol_version: "2"` and `worker`.

- `worker: "muse"` — sprite production and image post-processing.
- `worker: "chatgpt"` — connected-map batches, props, canonical references, art-direction work.
- `worker: "video"` — walk/run and other continuous-motion generation/extraction.
- `worker: "hermes"` — post-processing, runtime packing, technical integration.

Muse v2 polling target is:

`status == pending && worker == muse`

Legacy requests without `worker` may be handled explicitly during migration only.

## Approval policy

- `enemy_auto` — ordinary enemies/production assets may auto-promote only after visual + technical QC pass.
- `boss_manual` — boss identity/defining visual work requires user approval.
- `guardian_manual` — guardian/summon identity work requires user approval.

Only boss and guardian/summon assets require human approval by default. Ordinary enemy identities may be created by ChatGPT/Codex/Hermes or Muse and auto-lock after QC.

## Canonical reference rule

Preferred durable identity path:

`references/canonical/<chapter>/<character_key>/canonical.png`

Two supported routes:

1. `external_reference_first` — ChatGPT/Codex/Hermes/user supplies the accepted identity, then Muse animates it.
2. `muse_self_reference` — Muse creates the ordinary-enemy identity candidate, QC accepts it automatically when policy allows, then Muse continues into animation production.

Do not silently replace a canonical identity with an arbitrary latest generated frame.

## Muse Sprite Pipeline v2

See `specs/muse-worker-v2.md` for the complete contract. Core rules:

- choreography first (`frames_vi[]`)
- one high-resolution contact-sheet generation pass when practical
- prefer compact layouts: 8→4x2, 12→4x3, 16→4x4
- runtime 128x128/192x192 is **not** creative generation resolution
- removable white/solid background is acceptable; post-process to RGBA
- use connected-component/cluster extraction rather than trusting rigid grid cuts
- mask neighboring-frame bleed and repack with explicit gutter (default 15 px per side)
- preserve good poses and repair only missing/bad poses; max 2 repair passes
- return high-resolution master + frames + GIF preview + provenance/QC metadata

Walking/running cycles stay on the video-to-animation route.

## World-building coordination

Authoritative cross-worker handoff:

- `docs/worldbuilding/CHATGPT_MUSE_WORLD_BUILDING_HANDOFF.md`
- `docs/worldbuilding/ch02/REGION_ART_BIBLE.md`
- `docs/worldbuilding/ch02/MAP_PRODUCTION_MATRIX.md`
- `docs/worldbuilding/ch02/CUTSCENE_REFERENCE_PLAN.md`
- `docs/worldbuilding/CH03_CH05_REWRITE_ROADMAP.md`

World production follows chapter-by-chapter vertical slices: lock story first, then connected map/world art, then integrate and prove the chapter playable before moving on.

## Request naming

Use unique versioned request names and matching IDs, e.g.:

`requests/YYYYMMDD-HHMM-<subject>-<action>-v2.json`

## Security

This repository is public. Never commit tokens, deploy private keys, cookies, credentials, environment secrets, or private auth material. Worker write credentials must be provisioned outside chat/repo through a secure mechanism.

## Current Chapter 2 production direction

After Sơn Tinh, ordinary-enemy work includes Mộc Linh, Gấu Rừng and Rễ Cuồng. Xương Cuồng / Mộc Tinh is a boss and therefore uses manual boss approval. Cối Xay is not the main boss; it is the ancient wind-reading communal device and runaway encounter earlier in the chapter.
