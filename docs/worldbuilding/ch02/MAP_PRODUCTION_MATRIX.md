# Chapter 2 Map Production Matrix

Status: approved vertical world-building plan.

## Map 1 — Trạm Giữ Tuyến

Game source: `map_ch02_planning_station`.

Decision: `KEEP / REPURPOSE`.

Keep the existing 2048×1152 highland-junction geometry. Re-dress it as the crowded temporary station immediately after Cầu Không Nhìn Lại.

Required additions:
- temporary shelters / awnings / supplies
- displaced household goods
- large red-map focal point
- small number of NPCs placed in open areas
- right-side builder checkpoint with low object density

Do not restore the old stacked blocker actors at the narrow bridge.

## Map 2 — Khu Dân Cư Cuối Cùng

Game source: `map_ch02_permit_office` geometry.

Decision: `KEEP GEOMETRY / DELETE PERMIT-OFFICE IDENTITY / REPURPOSE`.

The existing grassy clearing/fork is suitable for the inhabited fringe. Re-dress with signposts, rope, crates, awnings, stools and patrol/build-team supplies.

Story function: ordinary people, memories of prosperity, rumors about Sơn Tinh, patrol team preparing to depart.

## Map 3 — Đồi Cối Xay / Trạm Gió

Decision: `GENERATE NEW`.

Requirements:
- open route with strong wind exposure
- ancient intelligent windmill as unmistakable focal point
- enough safe battle/readability space around the windmill
- minimal clutter
- mountain ridges / flags / wind indicators readable in exploration view
- direct route continuity from Map 2 and onward toward Map 4

Combat: runaway Cối Xay only. No Pawn Wall + Knight Wild battle here.

## Map 4 — Vành Đai Bỏ Hoang / Miếu Cũ

Decision: `GENERATE NEW`.

Environmental timeline inside one map:
1. relatively intact abandoned homes
2. grass-covered terraces and collapsing fences
3. roots overtaking paths and foundations

Required landmarks:
- abandoned Sơn Tinh shrine
- old storehouse/home suitable for Gấu Rừng encounter
- endpoint where returning patrol team is encountered

The map should be quiet for most of its traversal.

## Map 5 — Sườn Núi Từng Bước

Game source: `map_ch02_mountains`.

Decision: `KEEP / CLEAR DRESSING / REPURPOSE`.

The current 2048×1152 terrace-and-stair geometry is a strong fit. Remove almost all temporary worksite/planning clutter.

Required story markers:
- patrol marker 17 / final known marker
- no active settlement beyond this point
- Sơn Tinh reveal space
- giant root glimpse / Xương Cuồng evidence
- route forward into Map 6

No combat.

## Map 6 — Rừng Lấn

Decision: `GENERATE NEW`.

Requirements:
- former human route still barely legible
- sparse house/store foundations and old stone traces
- forest clearly overtaking those traces
- space for Mộc Linh encounter
- Root Anchor 1
- traversal/environmental beat leading to Root Anchor 2
- first strong practical use of Guardian Sơn Tinh after unlock

## Map 7 — Đường Rễ

Decision: `GENERATE NEW`.

Requirements:
- no inhabited structures
- no maintained human road
- stone, roots, fissures, torn earth, trunks
- strong threshold feeling before final territory
- Rễ Cuồng pre-boss encounter
- Root Anchor 3
- exit composition that supports silence and distant creaking before Map 8

## Map 8 — Cao Nguyên Cổ Mộc

Game source: `map_ch02_windmill_plateau` geometry.

Decision: `KEEP GEOMETRY / REGENERATE VISUAL IDENTITY`.

The existing plateau/stair progression is useful, but all windmill/worksite/planning identity is removed.

Rebuild as a swallowed ancient highland settlement:
- stone road
- village gate
- well
- terraces / old fields
- house foundations
- larger old Sơn Tinh shrine
- drainage channel
- monumental tree/root structure at center

Xương Cuồng must initially read as part of the landscape, then animate into the final boss.

Post-boss state needs a restrained alternate dressing: loosened roots, restored wind, small water flow, visible old route toward Chapter 3.

## Connected-map continuity contract

Before generation, define entry/exit edge and path direction for all 8 maps. New map generations must be reviewed as a region sequence, not as isolated pretty images.

Every map review must check:
- path direction continuity
- apparent elevation progression
- vegetation escalation
- human-presence gradient
- landmark visibility
- safe collision readability
- narrow-walkbound object density
