# Identity gốc — General Forgot (khóa, dùng cho mọi request)

Dùng đúng nhân vật này trong mọi asset, trừ khi `identity_overrides` trong
request ghi đè một điểm cụ thể.

## Ngoại hình
- Ông già tướng quân, dáng **lùn chắc nịch**, mặt già, lông mày / ria mép / râu **trắng**
- Mũ đồng có **huy hiệu sao tỏa** + mào lông **xanh đậm**
- Giáp đồng-vàng nhiều lớp, huy hiệu đồng bộ, **khăn thắt lưng xanh**, **áo choàng xanh**
- Mảnh vải màu nhạt in **bản đồ với đường hành quân và dấu X đỏ**
- Giáo dài cán **nâu**, đầu giáo **VÀNG**, dây buộc/tua **xanh**, nắp đuôi giáo

## Phong cách & khung hình (bất biến)
- Phong cách **cartoon-anime 2D**, tuyệt đối không chuyển sang 3D
- Mặt nhân vật **hướng trái**
- Sprite sheet: nền **trong suốt (RGBA)**, các sprite căn giữa ô, **không chồng lấn**, tỉ lệ nhân vật đồng đều
- Reference video: nền **xám studio trơn** (không phong cảnh, không bóng đổ, không chữ, không UI), camera **cố định** (không zoom/pan/cắt/rung), nhân vật + toàn bộ cây giáo luôn **nằm trọn trong frame**, không close-up

## Drift đã biết
- Model video có xu hướng render đầu giáo màu **bạc/thép** thay vì **vàng** — cần nhấn mạnh màu vàng trong prompt.

## Quy tắc consistency (reference-first) cho mọi request
- Mỗi lần generate: đính kèm ảnh reference nhân vật (bản mới nhất đã duyệt trong `assets/`), và mô tả action mới như **một biến thể tư thế của reference**, không phải request mới hoàn toàn.
- Dù đã có reference, prompt vẫn **viết đầy đủ chi tiết trang phục bằng chữ** — nhất là: đầu giáo **VÀNG** (không bạc/thép), giáp đồng-vàng, mào/khăn xanh đậm, ria mép trắng, áo choàng bản đồ.
- Cụm từ ánh sáng/nền giữ **nguyên văn** mọi lần generate.
- Output đẹp nhất sau khi duyệt sẽ **thay thế reference** cho các lần sau.
