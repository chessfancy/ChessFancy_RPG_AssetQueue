# Chapter 2 — Scene 08: Cối Xay Mất Kiểm Soát

Tài liệu brief cho request video Chapter 2 Scene 08. Worker chỉ tạo candidate; chưa có quyết định tích hợp runtime.

## Tham chiếu

- Chuyển động/identity: `reference/windmill_overworld_idle.gif`, tách máy móc từ asset overworld đang dùng `windmill_overworld_stable`: 24 frame, 192×192, 8 fps, loop 3 giây.
- Nền/vị trí: `static/game/assets/maps/map_ch02_windmill_plateau_base.png` và NPC `windmill` trong `content/maps/windmill_station.json`. Dùng đúng map hiện tại; không đổi topology, vị trí hay tỉ lệ. Khi gửi vào AssetQueue, copy đúng snapshot nền sang `references/ch02/map3_windmill_background.png` cùng GIF.

## Scene flow đơn giản

1. Mở trên Map 3, cối xay đang chạy bình thường.
2. Chong chóng chậm dần rồi dừng hẳn.
3. Sau một nhịp ngắt, nó quay **ngược chiều kim đồng hồ theo góc nhìn của camera**, tăng tốc và mất kiểm soát; thân tháp vẫn nguyên vẹn.
4. Kết clip ở trạng thái runaway. Sau clip, một worker bước vào bằng runtime/gameplay event, báo cối xay mất kiểm soát và nhờ nhóm ổn định nó; rồi vào trận ổn định cối xay. Event/thoại worker này còn cần được implement; không sinh chữ hay thoại trong video.

Không xây hệ thống riêng cho cờ, chuông, weather-vane hay indicator; không cần prop báo động mới. Giữ nguyên hai cờ vải nhỏ đã có trong ảnh nền như chi tiết tĩnh; không animate chúng thành tín hiệu sự cố. Video chỉ truyền đạt sự cố. Trận đánh là ổn định/vô hiệu hóa, không phải giết boss; cối xay sống sót.

## Prompt và QC

Prompt: `prompt_muse_vi.txt`. GIF là nguồn thật của sprite và nhịp quay, nhưng bốn cánh đối xứng nên chiều quay không kết luận chắc từ GIF; prompt ghi rõ chiều ngược kim đồng hồ theo góc nhìn camera. Cần đính kèm riêng ảnh nền Map 3 để khóa location.

- Request một video 16:9, 6–8 giây; toàn bộ cối xay và một phần đủ rộng của Map 3 phải hiện trong khung.
- Giữ mặt, mái xanh, thân đá, màu sắc, silhouette và tỉ lệ; thân đứng yên, chỉ rotor đổi tốc độ/hướng.
- Không redesign, không thêm worker/civilian/quái vật vào clip, không cờ/chuông/indicator, chữ/subtitle/UI/logo/watermark/audio, không camera roll/crop/phá hủy.
- Giữ output thô để QC. Chưa copy vào production. Tích hợp video là bước riêng sau khi user duyệt hình ảnh và test playback/fallback; video thiếu/lỗi không được chặn trận.
