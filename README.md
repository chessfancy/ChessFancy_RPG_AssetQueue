# ChessFancy RPG Asset Queue

Public handoff repository between Hermes and Muse for generating RPG assets.

## Layout

- `requests/` — Hermes creates request JSON files here.
- `assets/` — Muse commits generated outputs under `assets/<job-id>/`.
- `specs/` — Muse-maintained request schema, examples, and character identity specs.
- `references/` — canonical reference images supplied by Hermes/user for reference-first generation.

## Ownership

- Hermes may create files in `requests/` and `references/`.
- Hermes must not write or overwrite files in `assets/`.
- Muse may write `assets/` and `specs/`.
- In an existing request, Muse may change only the `status` field.
- Neither side overwrites the other side's owned outputs.

## Request lifecycle

1. Hermes validates `requests/<job-id>.json` against `specs/request-schema.json`.
2. Hermes pushes the request with `status: pending`.
3. Muse polls the repository every 10–15 minutes.
4. Muse generates from the request and canonical references.
5. Muse writes outputs to `assets/<job-id>/`, including `asset.json` provenance metadata.
6. Muse changes only the request `status` to `done` or `failed` and pushes.
7. Hermes pulls, validates the bundle, then copies it into the RPG `assets-source` tree as a candidate.
8. Smoke-test output is never auto-promoted into production.

## Reference-first rule

Every character-generation request must reference one or more canonical files under `references/`.
The action prompt describes pose/motion as a variation of that identity, not a redesign.

## Request naming

Use unique request names and matching IDs:

`requests/YYYYMMDD-HHMM-<action>.json`

## Security

This repository is public.
Never commit tokens, deploy private keys, cookies, credentials, local environment files, or other secrets.
Muse write credentials must be provisioned through a secure channel outside chat and outside this repository.

## First smoke test

The first live job is Cụ Bản Tiện / `npc_ch02_planning_elder` walking animation.
Reference: `references/ch02/npc_ch02_planning_elder/canonical.png`.

Runtime convention verified from `map_warrior_female_run` / `_stand`:

- row 0: down
- row 1: up
- row 2: left
- row 3: right
- run sheet: 6 frames per row, 14 fps
- stand sheet: 1 authored standing frame per direction
- transparent PNG, full body, normalized apparent body scale and feet baseline
