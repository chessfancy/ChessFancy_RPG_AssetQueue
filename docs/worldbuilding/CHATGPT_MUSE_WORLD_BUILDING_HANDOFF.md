# ChatGPT ↔ Muse World-Building Handoff

Status: approved workflow on 2026-10-03.

## Production strategy

Use chapter-by-chapter vertical production:

`story lock -> world/map art -> asset production -> integration/playable -> next chapter`

Do not generate a chapter's exploration geography before its dramatic function and route graph are locked.

## Roles

### ChatGPT — World Director

Owns screenplay-to-space translation and visual continuity:
- chapter route graph and map count
- connected exploration-map bases
- geography, landmarks and traversal readability
- settlement / ruin / vegetation / geology language
- chapter palette and regional style bible
- prop families and environmental storytelling
- canonical environmental references
- boss/guardian art-direction references
- cutscene storyboard/reference images
- visual escalation from map to map

ChatGPT does **not** author runtime collision/event code merely because art exists.

### Muse — Asset Production

Owns production from accepted references:
- enemy and NPC sprite production
- battle animation rows
- attacks / specials / hurt / KO
- self VFX / hit packs / status loops
- environment/cutscene video from locked references
- image post-processing, extraction, de-bleed and previews

Muse must not invent chapter geography or silently replace a locked environmental identity.

### Sol / Hermes — Game Integration

Owns:
- map JSON and scene wiring
- collision / walkbounds / portals
- event chains and flags
- runtime atlases / manifests
- deterministic packing and technical QC
- browser/runtime witnesses
- promotion into the game repo

Sol/Hermes must not invent missing production art inside runtime code. Missing art becomes an AssetQueue gap/request.

## Canon rules

- Existing art is classified as `KEEP`, `REPURPOSE`, `REFERENCE_ONLY`, `REGENERATE`, or `DELETE_FROM_CANON` before production work.
- High-resolution generation stays in AssetQueue/cache; the game repo receives only approved runtime outputs and provenance.
- Boss and Guardian/Summon defining identities remain manual approval.
- Regular enemies may auto-promote after visual + technical QC.
- Walk/run/continuous locomotion stays on the video-to-animation lane.
- No generator writes directly to game production runtime paths.

## Narrow-walkbound rule

Narrow corridors, bridges, stairs and chokepoints are low-density authoring zones. Do not stack multiple independent actors, conditional duplicate actors, and collision-bearing props on the same small walkbound. Prefer one logical actor/state or move alternate states away from the bottleneck.

## Chapter order

1. Finish Chapter 2 story lock and world art.
2. Integrate Chapter 2 to a playable vertical slice.
3. Rewrite Chapter 3 from the foundation, then build its connected world set.
4. Rewrite Chapter 4, then build its world set.
5. Rewrite Chapter 5/finale, then build its world set.

Do not preserve obsolete story behavior just to keep legacy tests green. Tests follow the accepted screenplay, not the reverse.
