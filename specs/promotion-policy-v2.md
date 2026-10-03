# Promotion Policy v2

Generation, QC and production promotion are separate stages.

## Policies

### `enemy_auto`
For ordinary enemies and routine production assets.

Automatic promotion is allowed only after:

1. worker candidate bundle is complete
2. visual QC passes
3. Hermes technical/runtime QC passes
4. no manual-approval trigger applies

A regular-enemy canonical reference may be created by ChatGPT/Codex/Hermes/user or Muse and auto-lock after QC.

### `boss_manual`
Boss identity and boss-defining visual work always stops at `candidate_ready` until the user approves it.

Animation rows derived from an already approved boss canonical identity may still require manual promotion when they materially change the boss silhouette/identity; routine technical repacks do not create a new identity approval.

### `guardian_manual`
Guardian/summon identity and identity-defining revisions always require user approval before production promotion.

## States

Recommended promotion states:

`pending -> generated_raw -> processed_candidate -> qc_passed -> candidate_ready -> approved -> production`

Terminal failure state:

`failed`

The worker request `status` remains only `pending | done | failed`; detailed candidate/promotion states belong in review/promotion records, not by expanding worker status.

## Promotion record

A future `promotions/<job-id>.json` should contain at least:

- source request id
- source/result commit SHA
- output SHA256
- destination path
- approval policy
- visual QC result
- technical QC result
- approver/QC mechanism
- timestamp

## Manual-approval boundary

Human approval is required by default only for:

- boss identity / defining visual revision
- guardian / summon identity / defining visual revision

Do not silently require human approval for ordinary enemies, props, routine attack/hurt/KO rows, or other production assets when their configured automatic policy and QC both pass.
