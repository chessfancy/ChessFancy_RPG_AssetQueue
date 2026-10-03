# ChessFancy RPG Asset Pipeline v2 — Design Spec

Status: design approved in chat on 2026-10-03; written-spec review pending before protocol migration.

## 1. Goal

Build a multi-worker asset studio that uses each system for the work it does best while preserving visual continuity, provenance, and safe promotion into the game.

Primary roles:
- ChatGPT Web: world art direction, connected-map batches, props, canonical references, style continuity, visual escalation/review.
- Muse: sprite production, contact-sheet generation, animation post-processing, frame extraction, bleed cleanup, GIF previews, sprite provenance.
- Video pipeline (Flow/Veo + extraction): walk/run and other motion that benefits from continuous temporal generation.
- Hermes: producer/router, request authoring, technical QC, atlas/runtime build, integration, promotion records.

No generator writes directly into production runtime paths at creation time.

## 2. Approval policy

### Enemy / ordinary production asset — automatic
Regular enemies, minor props, ordinary animation rows, and routine variants may auto-promote after visual + technical QC pass.

A new regular-enemy identity may be created either by ChatGPT/Codex/Hermes or by Muse itself. If QC passes, no human identity approval is required.

### Boss — manual
Boss identities and boss-defining visual revisions require human approval before production promotion.

### Guardian / summon / story-critical identity — manual
Guardians, summons, and story-critical character identities require human approval before production promotion.

Tier choice controls promotion only; it does not change the requirement that every generated asset first lands as a candidate.

## 3. Worker routing

Hermes is the router of record.

Preferred request metadata in v2:
- `worker`: `muse | chatgpt | video | hermes`
- `task_type`: e.g. `combat_animation`, `canonical_reference`, `connected_map_set`, `prop_pack`, `locomotion`, `postprocess`
- `approval_policy`: `enemy_auto | boss_manual | guardian_manual`

Worker rules:
- Muse consumes only requests addressed to Muse.
- ChatGPT requests remain untouched by Muse.
- Video requests go through the continuous-motion pipeline.
- Hermes owns technical post-processing/integration requests.

## 4. Canonical reference architecture

Canonical identity is separate from generated output.

Preferred durable path:
`references/canonical/<chapter>/<character_key>/canonical.png`

A canonical reference changes only when an approved identity revision explicitly replaces it.
Do not use an arbitrary latest generated image as the permanent source of truth.

Two supported sprite routes:

### Route A — external reference first
1. ChatGPT Image / Codex / Hermes / user creates a strong reference.
2. Reference becomes canonical according to approval policy.
3. Muse generates animation from that canonical reference.

### Route B — Muse self-reference first
1. Muse creates a canonical-reference candidate.
2. Regular enemies may auto-accept after QC; boss/guardian identities wait for human approval.
3. Muse continues from the accepted canonical identity into animation production.

## 5. Muse Sprite Pipeline v2

### 5.1 Choreography before generation
Every non-trivial animation request should include:
- action summary (`action_vi`)
- expected frame count
- facing / camera constraints
- ordered `frames_vi[]` beats describing the intended pose/action progression
- known identity drift risks

The choreography is specified before generation. Muse illustrates the sequence rather than inventing a new action structure each time.

### 5.2 Generate one high-resolution contact sheet
Prefer one diffusion/image-generation pass for the whole animation sequence to minimize identity drift and quota usage.

Preferred compact layouts:
- 8 frames: 4x2
- 12 frames: 4x3
- 16 frames: 4x4

Avoid long 8x1 / 16x1 generation layouts unless specifically justified.

Generation prompt requirements:
- strict grid
- each pose isolated in its own logical cell
- wide gutter
- no touching / overlap / cropping
- full body and important weapon/parts visible
- uniform apparent scale
- consistent identity from canonical reference
- no text / watermark / UI
- simple removable background

### 5.3 Generation resolution is not runtime resolution
Runtime `128x128` or `192x192` cells are delivery sizes, not creative-generation sizes.

V2 separates:
- `generation_layout`
- working/master resolution
- `runtime_cell_size`

Muse keeps a high-resolution master; Hermes performs the final runtime downsample/atlas build.

### 5.4 Background handling
Do not fail merely because the model returns white instead of true alpha.
A clean white/solid generation background may be removed by post-processing to RGBA.

### 5.5 Frame discovery and segmentation
Do not rely on rigid grid cutting as the authoritative extraction method.

Preferred process:
1. Build foreground mask from alpha or removable background.
2. Detect connected components / sprite clusters.
3. Drop tiny noise.
4. Associate nearby fragments with the same pose where appropriate.
5. Order poses by expected row/column reading order.
6. Compare detected pose count to requested frame count.

Rigid cell cutting is allowed only as a coarse locator; final sprite bounds should follow the actual sprite group.

### 5.6 Missing-pose repair
If the initial sheet is missing or corrupting poses:
- preserve good poses
- generate only missing/bad poses
- use the prior sheet/canonical reference as style context
- maximum repair passes: 2

After two unsuccessful repair passes, mark the job `failed` with a reason instead of looping.

### 5.7 De-bleed and re-spacing
For each pose:
- extract actual pose group
- crop to tight bbox with safe margin
- mask pixels that belong to neighboring pose groups
- preserve detached but semantically related parts (weapon tassel, FX, tail) with the correct pose

Then repack into normalized master cells with explicit gutter/padding.

Default working extra padding: 15 px per side unless a request overrides it.

### 5.8 Normalize
Normalize:
- visible body scale
- baseline / root position
- center placement
- full-body safety margin
- aspect ratio

Do not arbitrarily stretch characters. Work from the high-resolution master and downsample later.

### 5.9 Muse deliverables
Preferred bundle:
- high-resolution RGBA master sheet
- individual high-resolution frames
- GIF preview
- `asset.json`
- QC/provenance fields

Raw AI generation may be omitted from Git if large, but its SHA256/snapshot/provenance should be retained when available.

## 6. Sprite QC

Visual QC:
- identity consistency
- readable choreography
- correct facing/camera
- no missing body/weapon parts
- no crop
- no neighboring-frame bleed
- acceptable style continuity

Technical QC:
- expected frame count
- usable alpha/background cleanup
- dimensions and master layout
- stable baseline/scale
- deterministic runtime packing succeeds
- runtime asset loads in game

Regular enemies can auto-promote only if both visual and technical QC pass.

## 7. Muse asset provenance

`asset.json` should evolve to record enough information to reproduce/audit the job, including where available:
- request id and request blob/commit SHA
- generator/worker
- canonical reference path/SHA
- generation mode (`single_contact_sheet` etc.)
- requested frame count
- initially detected frame count
- repaired frame indexes
- repair passes used
- generation/master/runtime size metadata
- background cleanup mode
- padding/gutter
- raw generation SHA256/snapshot id
- QC results

`done` means the worker completed its deliverables; it does not by itself mean production approval.

## 8. Review and promotion records

Generation and production approval remain separate.

Proposed states:
`pending -> generated_raw -> processed_candidate -> qc_passed -> candidate_ready -> approved -> production`

Failures may terminate as `failed`.

For automatic enemy promotion, `approved` may be machine-derived from the approved policy after both QC layers pass.
For boss/guardian assets, `approved` requires the user.

Promotion records should include:
- source request id
- source/result commit SHA
- output SHA256
- destination path
- approval policy
- approver / QC mechanism
- timestamp

## 9. ChatGPT connected-map batch

ChatGPT Web is the preferred generator/art director for connected exploration regions and matching prop families.

A connected-map request describes a whole region instead of independent prompts.

Example package fields:
- chapter/region
- 4-7 scene ids
- shared perspective/camera
- shared terrain/material/vegetation language
- lighting/time-of-day
- path width / traversability cues
- explicit edge connectivity (`A east -> B west`, `B north -> C south`, etc.)
- required landmarks
- forbidden temporary props
- chapter style bible

Expected ChatGPT outputs may include:
- connected scene images
- chapter/region palette reference
- matching prop sheets
- continuity notes / connectivity metadata

Maps are reviewed as a region batch rather than one isolated map at a time.

## 10. Style bible

The queue should maintain durable style guidance, preferably under `style-bibles/`.

Suggested structure:
- `style-bibles/global/`
  - exploration style
  - battle sprite style
  - character/reference style
- `style-bibles/chapter02/`
- `style-bibles/chapter03/`
- etc.

Each chapter bible should lock:
- palette
- materials
- terrain/geology
- vegetation
- architecture/props
- path/collision readability
- lighting/mood
- recurring visual laws
- chapter-specific enemy language

## 11. Map / prop / reference promotion

Maps:
`concept_candidate -> continuity_review -> chapter_fit_review -> collision/integration -> approved_map`

Props:
`candidate_prop_sheet -> style_review -> extraction/cleanup -> approved_prop_pack`

References:
`candidate_reference -> identity_review/policy -> locked_canonical_reference`

Regular-enemy references may auto-lock after QC. Boss/guardian references require human approval.

## 12. Communication contract migration

Migration must be backward-compatible enough to finish/record any v1 job already in flight.

Recommended sequence:
1. Keep current v1 request/result for provenance; do not rewrite history.
2. Record the first Clockwork attack attempt as QC-rejected once its remote result exists.
3. Add v2 schema fields while preserving the core `pending | done | failed` lifecycle.
4. Change Muse polling to consume only requests with `worker == muse` (legacy v1 may be handled explicitly during migration).
5. Add one v2 smoke request for Clockwork attack using high-res 4x2 contact-sheet workflow.
6. Validate round-trip and QC.
7. Begin regular-enemy production batches; Muse may self-create ordinary enemy references when needed.
8. Introduce ChatGPT/video lanes after Muse v2 routing is proven.

## 13. First v2 production target

Clockwork Knight attack v2 is the protocol smoke target:
- external canonical reference
- 8 choreography beats
- 4x2 high-resolution generation layout
- simple removable generation background
- connected-component extraction
- 15 px re-spacing
- high-resolution RGBA master + individual frames + GIF
- Hermes builds the final 128x128 runtime row

After that succeeds, ordinary Chapter 2 enemies may be batched with automatic approval under the enemy policy.

## 14. Non-goals

- Do not use Muse image-sheet generation for walk/run cycles when video extraction provides better temporal continuity.
- Do not auto-promote boss or guardian identities.
- Do not generate directly into production runtime paths.
- Do not treat `status: done` as production approval.
- Do not overwrite prior failed/rejected jobs; create a new request id/version so provenance remains intact.
