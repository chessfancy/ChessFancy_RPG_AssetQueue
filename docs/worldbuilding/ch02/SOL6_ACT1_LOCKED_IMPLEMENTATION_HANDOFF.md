# Sol 6 Handoff — Chapter 2 ACT I Locked Implementation

Status: **LOCKED for implementation**
Scope: Chapter 2 Scene 01–09 only (Map 1–3)
Do not implement or rewrite Scene 10+ from inference. Later Chapter 2 story remains in active review.

## Canonical role/name changes

- Remove `Cụ Bản Tiện` / `Bản Tiện` from story-facing content.
- Use **TRẠM TRƯỞNG**. No personal name is required.
- The settlement is a **Trạm**, not a stable village: temporary, overcrowded, populated by people retreating from higher settlements.

## Hard authoring rules

- Accepted `Cầu Không Nhìn Lại` remains source of truth; do not redesign it.
- Narrow walkbounds/corridors must remain low-density editing zones. Do not stack multiple selectable NPC states, duplicate conditional actors, barricades, and collision-bearing props in the same bottleneck.
- Do not preserve obsolete permit-office / permit-obtained / windmill-main-boss story behavior through compatibility hacks.
- Do not invent missing production art. Emit/report an AssetQueue gap instead.

## Chapter 2 NPC movement lock

Chapter 2 intentionally keeps NPC locomotion extremely limited.

- **TRẠM TRƯỞNG is the only authored walking NPC in the entire chapter.**
- His accepted walking asset already exists in the game runtime and must be reused.
- Do not request, generate, or integrate additional NPC walk/run/4-direction locomotion assets for Chapter 2.
- All other Chapter 2 civilian, worker, checkpoint and displaced-resident NPCs are static overworld actors.
- Their authored departure/arrival beats must be expressed through dialogue, event/state changes, repositioning between states/scenes, or map transitions rather than bespoke walking animation.
- A static NPC may still have a canonical reference image, one static overworld sprite, and dialogue portraits.
- Do not convert a static NPC into a walking NPC merely because the runtime supports `walk_to`.

---

# MAP 1 — TRẠM GIỮ TUYẾN

Preferred geometry source: existing `map_ch02_planning_station` base.
Repurpose content/dressing; keep the useful two-route geography.

## SCENE 01 — QUA CẦU

On entry from Cầu Không Nhìn Lại, show an overcrowded temporary settlement without narrator exposition:
- temporary tents/awnings;
- belongings moved down from upper settlements;
- agricultural tools and supply carts;
- too many people for the available permanent housing.

Party may remark briefly that it is crowded and looks recently occupied.

## SCENE 02 — TRẠM TRƯỞNG

Before speaking to the party, Trạm trưởng is handling a real route-safety report.

Locked dialogue intent:

**THỢ TUẦN TUYẾN**  
Ở khu Đông, đất vừa sạt một mảng lớn.

**TRẠM TRƯỞNG**  
Có ai bị thương không?

**THỢ TUẦN TUYẾN**  
Anh em rút về kịp.  
Nhưng chúng ta mất con đường đó rồi.

**TRẠM TRƯỞNG**  
Không ai sao là tốt.  
Đợi lúc gió dịu, chúng ta lên xem lại.  
Chỗ nào sửa được thì sửa.

Only after this does he notice the party.

Party says they need a route across the mountain range. Trạm trưởng tells them they should look at the map first.

Short NPC walk from work area to the map is encouraged if staging fits.

## SCENE 03 — BẢN ĐỒ ĐỎ

This is a dedicated cutscene beat, not a sequence of manual NPC clicks.

Required visual idea:
- a clear historical highland map;
- old settlements, terraces, Sơn Tinh shrine, old route network and highland regions;
- no Xương Cuồng spoiler;
- multiple upper regions have been crossed/marked red in layers over time.

During the cutscene, NPC 1 and NPC 2 speak automatically/off-screen:

**NPC 1**  
Nhà tôi ở đây.

**NPC 2**  
Nhà tôi cao hơn một đoạn nữa.

Party asks whether everyone moved down to the Trạm. NPCs explain most did, though some still remain higher up. The visual progression should communicate that first fields, then roads, then settlements were lost.

After cutscene, return free exploration.

Optional free-explore dialogue:

**NPC 1**  
Trước kia ông tôi hay dẫn tôi lên chiêm bái miếu thờ ngài ấy.

**NPC 2**  
Có lẽ ngài ấy nổi giận rồi.  
Không muốn chúng tôi ở đây nữa.

This is rumor, not confirmed truth.

### Asset gap — do not fake

Needed from world-building/AssetQueue:
- `ch02_highland_map_historical_clean`
- `ch02_highland_map_current_red`
- Red Map cutscene/storyboard/video reference package

If the new AssetQueue bridge exists, create a validated gap/draft. Otherwise report the exact gap to Hermes/ChatGPT. Do not create a permanent placeholder pretending to be production art.

## SCENE 04 — CHỐT THỢ XÂY

Right-side mountain approach contains a simple safety/construction checkpoint, not a wall of chess-piece blockers.

Use 1–2 NPCs placed outside the narrow walkbound.

Core dialogue:
- party may go up; nobody forbids it;
- before climbing, teams check the wind at the Windmill;
- calm weather below does not imply safe wind above;
- sudden wind can cause falling stone, trees and damaged routes;
- route through the residential fringe leads to the Windmill.

Remove the old stacked three-piece choke-point implementation from this story role. The old three chess pieces/resting duplicates are not canonical for this corridor.

---

# MAP 2 — KHU DÂN CƯ CUỐI CÙNG

Preferred geometry source: existing `map_ch02_permit_office` base.
Delete the **permit office** identity. Repurpose the geometry as the residential fringe / final inhabited area and route-team preparation point.

Keep suitable supply/settlement props such as signposts, ropes, crates, awnings, stools and route equipment if they fit the new dressing.

## SCENE 05 — NHỮNG NGƯỜI VẪN Ở LẠI

Free-explore NPC dialogue, not one forced group conversation.

### NPC 1 — memory

**NPC 1**  
Hồi tôi còn nhỏ, ruộng bậc thang trải dài từ trên cao xuống đây.  
Bản làng hồi đó nhộn nhịp lắm.

### NPC 2 — concern about Sơn Tinh

**NPC 2**  
Dị tượng từ vùng cao mỗi lúc một khắc nghiệt.

Party must ask what the anomalies are.

**SLOT**  
Dị tượng gì vậy ạ?

**NPC 2**  
Đất sạt.  
Có những trận gió mạnh tới mức cuốn cả gia súc đi.  
Đường lên núi cứ hỏng rồi mất.  
Những nơi còn sống được cũng mỗi lúc một ít hơn.

Pause.

**NPC 2**  
Thần bảo hộ muốn tuyệt đường chúng tôi rồi sao?

Do not have the party correct or reassure this NPC; they do not know the truth yet.

### NPC 3 — route maintenance

Explains that construction/route teams still go up to reset stakes, reinforce banks and reopen whatever can still be reopened. Some repairs last months; some must be redone almost immediately.

## SCENE 06 — ĐỘI TUẦN TUYẾN KHỞI HÀNH

Show ordinary workers preparing:
- rope;
- anchors;
- stakes;
- hoes/tools;
- folded map;
- food;
- safety gear.

They are workers, not a fantasy combat squad.

Locked beat:

**THỢ TUẦN TUYẾN 1**  
Gió thuận thì hôm nay thử lên thêm một đoạn.

**THỢ TUẦN TUYẾN 2**  
Đi xem Cối Xay Gió trước đã.

The route team does **not** require visible walking animation.

Chapter 2's only walking NPC is **TRẠM TRƯỞNG**.

For Scene06, show the workers preparing to depart, deliver the locked dialogue, then use event/state progression to represent their departure. Static workers may disappear/reposition after the beat or be absent on the next state/map.

Do not request NPC locomotion assets for the route team.

Party is not invited as heroes; both groups simply share the same destination.

---

# MAP 3 — ĐỒI CỐI XAY / TRẠM GIÓ

This needs a **new exploration map asset**. Do not repurpose the old Windmill Plateau boss map as this location.

World-building requirements:
- open hill/mountain view;
- sparse props;
- wind-reading equipment;
- Windmill is the clear focal landmark;
- Windmill reads as both useful infrastructure and an ancient intelligent/sacred mechanism.

## SCENE 07 — CỐI XAY ĐỌC GIÓ

Show the Windmill operating normally first.

It serves two functions:
1. grinds food for the Trạm;
2. reads higher-altitude wind conditions for route teams.

A worker explains these functions while showing vane/bells/indicators.

The route team asks whether conditions are good.

## SCENE 08 — DỊ TƯỢNG / RUNAWAY

No Pawn Wall battle. No Knight Wild battle. Remove that encounter from this sequence.

Locked staging:
- Windmill slows;
- nearby normal wind flag still indicates ordinary wind;
- Windmill stops;
- then rotates in the wrong direction;
- its vane points toward the mountain;
- warning bells/indicators become unstable;
- mechanism loses control;
- civilians/workers retreat from danger.

Only battle on Map 3:

**CỐI XAY GIÓ — THẦN VẬT MẤT KIỂM SOÁT**

Gameplay meaning is stabilization/disable, not killing an evil boss.

After battle the Windmill survives and remains part of the world.

## SCENE 09 — SAU CỐI XAY

Trạm trưởng arrives and inspects the machine before speaking to the party.

Mechanical inspection confirms the obvious parts are not simply broken; the vane continues pulling/pointing toward the mountain despite ordinary local wind.

Important safety logic:

**TRẠM TRƯỞNG**  
Hôm nay không ai lên nữa.

He suspends ascent while wind is unstable.

When the actual wind later calms, he permits the route team only to inspect the known route as far as the final marker/stake. They must not push beyond it.

Party asks about a route across the mountains.

**TRẠM TRƯỞNG**  
Có một tuyến.  
Sườn Núi Từng Bước.

When asked whether it still crosses the mountains:

**TRẠM TRƯỞNG**  
Trước đây thì được.  
Bây giờ ta không biết.

### Time/safety beat

Do not have everyone leave immediately after the runaway battle.

Required causal sequence:
1. Windmill detects/expresses abnormal upper-level wind and runs away.
2. Trạm trưởng suspends ascent.
3. Local wind calms after a short exploration/time beat.
4. Route team is allowed to inspect only the old known route up to the final stake.
5. Party may follow the same route **behind** the route team.

Trạm trưởng explicitly tells the party not to pass the route team.

Suggested locked line:

**TRẠM TRƯỞNG**  
Đi sau đội tuần tuyến.  
Đừng vượt họ.

End objective: proceed toward the Abandoned Belt / old route. Do not implement the later story beyond this handoff.

---

# Technical implementation boundaries

Sol may now implement for Scene 01–09:
- chapter/event/dialogue data;
- map 1/2 repurpose and scene object cleanup;
- NPC staging and short walk sequences;
- removal of obsolete permit semantics inside the locked area;
- removal of Pawn Wall/Knight Wild from Map 3 flow;
- Windmill runaway battle transition and post-battle alive/stabilized state;
- objective/state transitions through the end of Scene 09;
- asset-gap records for missing Map 3 and Red Map cutscene art.

Sol must NOT yet:
- write Scene 10+ dialogue/story;
- invent the Abandoned Belt/Sơn Tinh implementation beyond interfaces needed for the exit;
- generate world art itself;
- restore old permit/windmill-main-boss logic for test compatibility;
- make story decisions for Xương Cuồng/Sơn Tinh that are not yet in a locked handoff.

# Verification expected from Sol

For this locked slice, report:
- exact game branch/HEAD;
- tests changed/added;
- Map 1 entry → Red Map cutscene → free explore witness;
- Map 2 optional NPC dialogue + route-team departure witness;
- Map 3 runaway Windmill → battle → suspension → wait-for-calm → route-team departure witness;
- proof no Pawn Wall/Knight Wild encounter remains in this sequence;
- proof no permit-office gating remains in the locked route;
- asset gaps emitted for missing production art instead of hidden placeholders.
