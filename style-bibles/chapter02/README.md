# Chapter 2 — Art Style Bible

Working region: Thung Lũng Trung Cuộc / mountain route / root-zone escalation after Sơn Tinh.

## Environment language

- Vietnamese-fantasy highland frontier
- cliffs, ravines, windswept grass, rough mountain paths, stone steps, distant mountains
- practical handmade structures and safety elements; avoid modern industrial visual language
- Cối Xay is a wind-observation/story landmark, not the main boss identity

## Palette

Keep a natural highland family built around:

- warm earth/stone
- grass greens and muted yellow-greens
- weathered wood
- restrained amber/gold magical accents when needed
- avoid neon saturation unless tied to a specific magical event

## Materials

- rough mountain stone
- weathered timber
- rope / simple fencing
- cloth and practical village/planning materials where story-motivated
- roots, bark, leaves and living wood in the later root zone

## Vegetation

- hardy mountain grass
- shrubs and sparse trees on exposed slopes
- denser living-root / leaf language toward Mộc Linh, Rễ Cuồng and Xương Cuồng territory

## Path readability

- traversable routes must read clearly at exploration scale
- stairs/terraces keep consistent perspective and usable width
- connected maps should preserve where entering/exiting paths meet the image edges
- temporary planning props must not block the clean basemap unless explicitly required by the scene

## Enemy language after Sơn Tinh

### Mộc Linh
Small living-wood/root/leaf spirit; child-friendly, readable, disturbed/influenced rather than inherently evil.

### Gấu Rừng
Forest/mountain creature language; sturdy, practical silhouette, belongs naturally in the highland biome rather than looking like an imported fantasy monster.

### Rễ Cuồng
Aggressive root-zone threat; stronger root/wood silhouette while remaining suitable for a child-friendly JRPG.

### Xương Cuồng / Mộc Tinh
Boss identity. Requires `boss_manual` approval. It should feel like the major source/escalation of the root disturbance, visually distinct from ordinary Mộc Linh/Rễ Cuồng.

## Chapter 2 approval defaults

- Mộc Linh: `enemy_auto`
- Gấu Rừng: `enemy_auto`
- Rễ Cuồng: `enemy_auto`
- Xương Cuồng / Mộc Tinh: `boss_manual`

Boss/guardian rules override automatic ordinary-enemy production rules.

## NPC language

Chapter 2 NPCs are grounded Vietnamese-fantasy highland civilians and workers.

Emotional baseline:
neutral / restrained / weary / worried / subdued.

Avoid:
- exaggerated friendliness or cheerful welcoming poses
- broad happy smiles by default
- chess-piece decorations on hair, hats or clothing
- chess-themed armor or accessories unless explicitly story-authorized
- heroic combat styling for ordinary workers/civilians

Chapter 2 locomotion lock:
- **TRẠM TRƯỞNG is the chapter's only walking NPC and already has accepted runtime walk art.**
- All other Chapter 2 NPCs use static overworld art.
- Do not generate walk/run locomotion for them.
