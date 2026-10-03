# Asset Pipeline v2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Migrate AssetQueue to the approved v2 multi-worker contract and immediately release the first Muse v2 sprite batch without breaking v1 provenance.

**Architecture:** Keep the existing `pending | done | failed` lifecycle and legacy required fields for compatibility, then add routing, approval, choreography, generation/master/runtime metadata, and provenance fields. Muse remains able to process the first v2 request even before its poller is upgraded because the request retains the legacy core fields; the v2 contract instructs Muse to adopt `worker == muse` filtering for subsequent mixed-worker operation.

**Tech Stack:** GitHub repository contents, JSON Schema draft-07, Markdown contracts, Muse image generation + Python/PIL/NumPy/SciPy post-processing, Hermes integration/QC.

**Spec:** `docs/ASSET_PIPELINE_V2_DESIGN.md`

## Global Constraints

- Preserve v1 request/result history; never rewrite a rejected job into v2.
- `status` remains `pending | done | failed`.
- Regular enemies may auto-promote only after visual + technical QC pass.
- Boss and guardian/summon identities require human approval.
- Runtime cell size is not generation/master resolution.
- Muse image-sheet generation is not used for walk/run locomotion.
- No generator writes directly to game production paths.

## Review Focus

- Legacy v1 request still validates after schema migration.
- A Muse v2 request carries `worker=muse` but remains consumable by the current poller through legacy fields.
- `done` never implies production approval.
- Missing-pose repair is bounded to two passes and preserves good poses.
- Reference paths and approval policy cannot silently point a boss/guardian into auto-promotion.

---

### Task 1: Backward-compatible request schema v2

**Files:**
- Modify: `specs/request-schema.json`
- Create: `specs/example-request-clockwork-v2.json`

**Interfaces:**
- Consumes: current v1 schema and request lifecycle.
- Produces: v2 request contract with routing, approval, choreography, generation layout, runtime cell size, postprocess, references, and provenance-friendly fields.

- [ ] **Step 1:** Preserve the current required legacy keys: `id`, `character`, `action`, `asset_type`, `status`.
- [ ] **Step 2:** Add optional `protocol_version`, `worker`, `task_type`, `approval_policy`, `reference_mode`, `reference_images`, `character_spec_path`, `frames_vi`, `facing`, `generation_layout`, `runtime_cell_size`, `postprocess`, and `style_bible` properties with explicit enums/types.
- [ ] **Step 3:** Keep `status` enum exactly `pending | done | failed`; cap `postprocess.max_repair_passes` at 2.
- [ ] **Step 4:** Add `example-request-clockwork-v2.json` demonstrating 8 frames, 4x2 generation layout, 128x128 runtime cell, 15px padding, reference-first mode, and `worker=muse`.
- [ ] **Step 5:** Verify the old Clockwork v1 JSON and new v2 example are both structurally valid against the migrated schema.
- [ ] **Step 6:** Commit schema migration.

### Task 2: Muse communication contract and provenance

**Files:**
- Modify: `README.md`
- Create: `specs/muse-worker-v2.md`
- Create: `specs/asset-result-v2.md`

**Interfaces:**
- Consumes: v2 schema from Task 1.
- Produces: worker ownership, polling/filtering, generation/postprocess, result bundle, and QC/provenance contract.

- [ ] **Step 1:** Update README layout/ownership to add v2 routing without invalidating existing v1 history.
- [ ] **Step 2:** Specify that after migration Muse polls only `status == pending && worker == muse`, with explicit legacy handling for existing v1 requests.
- [ ] **Step 3:** Document Muse Sprite Pipeline v2: one high-res contact sheet, compact grid, removable background, component extraction, 15px repacking default, max two repair passes, high-res RGBA master, frames, GIF, metadata.
- [ ] **Step 4:** Define `asset.json` v2 provenance fields and the distinction between worker `done` and promotion approval.
- [ ] **Step 5:** Add result/QC expectations for frame count, identity, crop, bleed, background cleanup, and master/runtime separation.
- [ ] **Step 6:** Commit communication contract.

### Task 3: Style-bible and promotion skeleton

**Files:**
- Create: `style-bibles/global/README.md`
- Create: `style-bibles/chapter02/README.md`
- Create: `specs/promotion-policy-v2.md`

**Interfaces:**
- Consumes: approved role split and approval tiers.
- Produces: durable style guidance entry points and machine/human promotion rules.

- [ ] **Step 1:** Create global style-bible skeleton for exploration, battle sprites, canonical references, and recurring visual laws.
- [ ] **Step 2:** Create Chapter 2 style-bible skeleton with current highland/forest/root-zone art direction and slots for palette/material/terrain/vegetation/enemy language.
- [ ] **Step 3:** Define promotion policies `enemy_auto`, `boss_manual`, `guardian_manual` and require candidate -> QC -> approval -> production separation.
- [ ] **Step 4:** Explicitly state only boss and guardian/summon need human approval by default; ordinary enemies may auto-lock identity after QC.
- [ ] **Step 5:** Commit style/promotion skeleton.

### Task 4: Release Muse v2 Clockwork batch

**Files:**
- Create: `requests/20261003-<time>-clockwork-attack-v2.json`

**Interfaces:**
- Consumes: Clockwork canonical reference, v2 schema, Muse worker contract.
- Produces: first live v2 Muse request.

- [ ] **Step 1:** Author 8 ordered `frames_vi` beats for ready -> wind-up -> mechanical compression -> powered leap/lunge -> contact -> follow-through -> recovery -> ready.
- [ ] **Step 2:** Set `reference_mode=external_reference_first`, `worker=muse`, `task_type=combat_animation`, `approval_policy=enemy_auto`, `generation_layout=4x2`, `runtime_cell_size=128x128`, `postprocess.extra_padding_px=15`, `max_repair_passes=2`.
- [ ] **Step 3:** Point the request to `references/existing/enemy_clockwork_knight/canonical.png` and existing attack brief.
- [ ] **Step 4:** Keep all legacy required fields so current Muse poller can still consume it before its routing update.
- [ ] **Step 5:** Validate request against the migrated schema and push with `status=pending`.
- [ ] **Step 6:** Verify remote request exists and the previous v1 request remains untouched.

### Task 5: Queue the next ordinary-enemy batch template

**Files:**
- Create: `specs/example-request-enemy-self-reference-v2.json`
- Create: `requests/README_NEXT_BATCH.md`

**Interfaces:**
- Consumes: v2 Muse contract and `enemy_auto` policy.
- Produces: reusable template and explicit next targets without prematurely emitting multiple pending jobs before the protocol smoke returns.

- [ ] **Step 1:** Add self-reference-first template for a regular enemy canonical reference candidate followed by animation production.
- [ ] **Step 2:** Record next Chapter 2 targets: Mộc Linh, Gấu Rừng, Rễ Cuồng, then Xương Cuồng/Mộc Tinh with boss/manual policy for the boss.
- [ ] **Step 3:** State that Mộc Linh/Gấu Rừng/Rễ Cuồng may auto-approve after QC; Xương Cuồng/Mộc Tinh waits for human approval.
- [ ] **Step 4:** Do not emit additional pending production requests until Clockwork v2 proves the migrated round trip.
- [ ] **Step 5:** Commit the next-batch template/queue note.

### Task 6: Verification and handoff

**Files:**
- Read/verify all files changed above.

**Interfaces:**
- Consumes: Tasks 1-5.
- Produces: verified remote protocol and clear Muse handoff message.

- [ ] **Step 1:** Fetch the final remote schema, Muse contract, promotion policy, style-bible entries, and live Clockwork v2 request.
- [ ] **Step 2:** Confirm no secret/private credential appears in committed text.
- [ ] **Step 3:** Confirm v1 request remains unchanged and v2 request is uniquely versioned.
- [ ] **Step 4:** Provide Muse the exact migration instruction: pull latest, adopt `worker == muse` filter, follow `specs/muse-worker-v2.md`, then process the pending Clockwork v2 job.
- [ ] **Step 5:** Report commit SHAs, live request id, and what will happen automatically next.
