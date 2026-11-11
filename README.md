# Tuần 7 — Đám mây điểm và ảnh độ sâu từ STL

Bài tập Python đọc mô hình STL, tạo đám mây điểm và biểu diễn ảnh độ sâu.

## Các file mã nguồn

| File | Nội dung |
| --- | --- |
| `stl_utils.py` | Đọc STL dạng ASCII hoặc binary, gộp các đỉnh và loại điểm trùng. |
| `bai1.py` | Tạo và vẽ đám mây điểm 3D từ các đỉnh của mô hình. |
| `bai2.py` | Giữ các điểm có tọa độ Z lớn hơn hoặc bằng trung điểm khoảng Z. |
| `bai3.py` | Chiếu đám mây điểm lên lưới XY 64 × 64, giữ độ sâu nhỏ nhất tại mỗi ô. |
| `bai4.py` | Bổ sung trọng tâm tam giác và so sánh ảnh độ sâu trước, sau khi bổ sung. |

## Cài đặt và chạy

Cần Python 3, NumPy và Matplotlib:

```bash
python -m pip install numpy matplotlib
```

Tự chuẩn bị mô hình STL và đặt tên **`ball.STL`** trong cùng thư mục với các file Python. File mô hình không được đưa lên repository. Các bài hiện đọc trực tiếp tên `ball.STL`, không nhận tham số dòng lệnh.

Mở terminal tại thư mục chứa mã nguồn rồi chạy bài muốn xem:

```bash
python bai1.py
python bai2.py
python bai3.py
python bai4.py
```

Mỗi bài in kết quả ra terminal, lưu ảnh vào thư mục `output/` (được tạo tự động) và mở cửa sổ đồ thị. Đóng cửa sổ đồ thị để chương trình kết thúc.

Repository chỉ lưu mã nguồn và README; mô hình STL, đề bài PDF, ảnh kết quả và bộ nhớ đệm Python không được đưa lên GitHub.
