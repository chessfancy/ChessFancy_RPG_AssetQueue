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

Use 1–2 **static** NPCs placed outside the narrow walkbound.

Locked dialogue — use verbatim:

**THỢ CHỐT TUYẾN**  
Các cháu định lên cao à?

**SLOT 3**  
Dạ. Bọn cháu cần tìm đường qua dãy núi.

**THỢ CHỐT TUYẾN**  
Đi thì được.

**THỢ CHỐT TUYẾN**  
Nhưng đội nào lên cao cũng phải ghé Cối Xay Gió xem gió trước.

**SLOT 1**  
Ở dưới này có vẻ vẫn yên mà ạ?

**THỢ CHỐT TUYẾN**  
Ở dưới yên không có nghĩa trên cao cũng yên.

**THỢ CHỐT TUYẾN**  
Gió quật ngang sườn núi thì đá lăn, cây đổ.  
Đường vừa sửa xong cũng có thể mất.

**THỢ CHỐT TUYẾN**  
Cứ đi qua khu dân cư phía trước.  
Từ đó có đường lên Cối Xay.

Do not expand this exchange with extra safety exposition.

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

Locked dialogue — use verbatim:

**NPC 3**  
Bọn tôi vẫn lên tuyến đều.

**SLOT 2**  
Đường hỏng như vậy vẫn sửa được ạ?

**NPC 3**  
Cọc mất thì đóng lại.  
Bờ sạt thì gia cố.  
Đường bị lấp thì mở lại.

**NPC 3**  
Có chỗ giữ được vài tháng.

**NPC 3**  
Có chỗ vừa sửa xong...  
ít hôm sau đã phải làm lại.

Do not add an explanation of the underlying cause; this NPC knows maintenance work, not the truth behind the disturbance.

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

Locked dialogue — use verbatim:

**THỢ TRẠM GIÓ**  
Cối Xay này không chỉ dùng để xay lương thực cho Trạm.

**THỢ TRẠM GIÓ**  
Nhìn hướng cánh, cánh định gió và chuông báo...  
bọn tôi biết gió trên cao đang đổi thế nào.

**THỢ TUẦN TUYẾN 1**  
Hôm nay lên tuyến được không?

**THỢ TRẠM GIÓ**  
Chờ nó đọc xong đã.

Do not expand this into a machinery tutorial.

### Scene07–08 implementation simplification lock

Do **not** build a multi-component runtime simulation for the Windmill.

Do **not** separately engineer runtime systems for:
- independent blade rotation;
- weather-vane pivoting;
- local wind-flag physics;
- bell/indicator oscillation;
- synchronizing those parts over a timeline.

The scene only needs to **communicate the visual event**, not expose those components as gameplay systems.

Preferred implementation:

1. Map 3 begins in a simple normal/stable exploration state.
2. Play the Scene07 dialogue above.
3. Use **one short pre-battle cinematic video** to show the Windmill transition from normal operation into the abnormal runaway state.
4. Return from the video directly into the battle trigger.
5. After battle, return to a simple stabilized/alive Windmill world state.

Use the existing Google Flow / Veo video workflow if available. The cinematic should be generated from the accepted Map 3 / Windmill reference so the location and machine identity remain continuous.

One coherent video is preferred over building reusable machinery animation code that Chapter 2 does not otherwise need.

## SCENE 08 — DỊ TƯỢNG / RUNAWAY

No Pawn Wall battle. No Knight Wild battle. Remove that encounter from this sequence.

The pre-battle cinematic communicates, in one visual sequence:
- Windmill begins in normal operation;
- nearby cloth/flag still reads as ordinary local wind;
- Windmill slows;
- Windmill stops;
- Windmill turns in the wrong direction;
- its wind-reading direction pulls toward the mountain;
- bells/indicators become unstable;
- nearby workers/civilians retreat from danger.

This is **visual storytelling inside the video**, not a requirement for separate live runtime mechanisms.

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
1. The Scene07–08 cinematic has already communicated the abnormal upper-level wind and runaway.
2. Trạm trưởng suspends ascent.
3. Use a **simple short free-exploration/time beat**, then a state/flag change to represent that local wind has calmed. Do not implement a dynamic wind simulation.
4. Route team is allowed to inspect only the old known route up to the final stake.
5. Party may follow the same route **behind** the route team.

The route team remains static for Chapter 2 asset purposes. Its departure/progression is represented through event/state changes, repositioning between states, or absence in the next state. Do not create route-team walk animation just to illustrate departure.

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
- NPC staging; only Trạm trưởng may use the already-accepted Chapter 2 walking asset;
- removal of obsolete permit semantics inside the locked area;
- removal of Pawn Wall/Knight Wild from Map 3 flow;
- one short Scene07–08 pre-battle Windmill cinematic video rather than a new live machinery simulation;
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
