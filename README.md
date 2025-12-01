# vnqr 🇻🇳

Thư viện Python để tạo VietQR code - mã QR thanh toán chuẩn Việt Nam theo tiêu chuẩn NAPAS.

## ✨ Tính năng

- ✅ Tạo chuỗi VietQR theo tiêu chuẩn NAPAS
- ✅ Tạo hình ảnh QR code từ chuỗi VietQR
- ✅ Hỗ trợ các ngân hàng tại Việt Nam
- ✅ Type hints đầy đủ

## 📦 Cài đặt

### Cài đặt cơ bản

```bash
pip install vnqr
```

Hoặc sử dụng `uv`:

```bash
uv pip install vnqr
```

## 🚀 Sử dụng nhanh

### Tạo chuỗi VietQR

```python
from vnqr import generate_vietqr_string

vietqr_string = generate_vietqr_string(
    bank_bin="970425",           # Mã BIN của ngân hàng
    bank_account="123456789",    # Số tài khoản
    total_amount=100000,         # Số tiền (VNĐ)
    content="Thanh toan don hang"  # Nội dung giao dịch
)

print(vietqr_string)
# Output: 00020101021238530010A0000007270123000697042501091234567890208QRIBFTTA5303704540710000005802VN62150811Thanh toan don hang6304...
```

### Tạo hình ảnh QR code

```python
from vnqr import generate_vietqr_string, generate_qr_image
import base64

# Tạo chuỗi VietQR
vietqr_string = generate_vietqr_string(
    bank_bin="970425",
    bank_account="123456789",
    total_amount=100000,
    content="Thanh toan don hang"
)

# Tạo hình ảnh QR code (dạng base64)
qr_image_base64 = generate_qr_image(vietqr_string)

# Lưu vào file
image_data = base64.b64decode(qr_image_base64)
with open("vietqr.png", "wb") as f:
    f.write(image_data)
```

### Tạo QR code với icon

```python
import io
from vnqr import generate_vietqr_string, generate_qr_image_with_icon

# Tạo chuỗi VietQR
qr_string = generate_vietqr_string(
    bank_bin="970425",
    bank_account="123456789",
    total_amount=100000,
    content="Thanh toan don hang",
)

# Cách 1: truyền đường dẫn file icon
qr_with_logo = generate_qr_image_with_icon(
    qr_string=qr_string,
    icon_path="examples/logo.png",
)

# Cách 2: đọc icon thành bytes rồi wrap bằng BytesIO
with open("examples/logo.png", "rb") as f:
    icon_bytes = f.read()

qr_with_logo_from_bytes = generate_qr_image_with_icon(
    qr_string=qr_string,
    icon_path=io.BytesIO(icon_bytes),  # BinaryIO được hỗ trợ
)
```

## 📚 API Reference

### `generate_vietqr_string()`

Tạo chuỗi VietQR theo tiêu chuẩn NAPAS.

**Tham số:**
- `bank_bin` (str): Mã BIN của ngân hàng (6 chữ số). Ví dụ: "970425" (Techcombank)
- `bank_account` (str): Số tài khoản ngân hàng
- `total_amount` (int): Số tiền giao dịch (VNĐ)
- `content` (str): Nội dung giao dịch

**Trả về:**
- `str`: Chuỗi VietQR

**Ví dụ:**

```python
from vnqr import generate_vietqr_string

vietqr_string = generate_vietqr_string(
    bank_bin="970425",
    bank_account="123456789",
    total_amount=100000,
    content="Thanh toan don hang"
)
```

### `generate_qr_image()`

Tạo hình ảnh QR code từ chuỗi VietQR.

**Tham số:**
- `qr_string` (str): Chuỗi VietQR

**Trả về:**
- `str`: Hình ảnh QR code dạng base64

**Ví dụ:**

```python
from vnqr import generate_qr_image

qr_image_base64 = generate_qr_image(vietqr_string)
```

### `generate_qr_image_with_icon()`

Tạo hình ảnh QR code với icon đặt giữa (ví dụ logo thương hiệu).

**Tham số:**
- `qr_string` (str): Chuỗi VietQR
- `icon_path` (str | Path | BinaryIO): Đường dẫn tới icon hoặc đối tượng file-like (có `.read()` trả về bytes). Có thể đọc file ảnh vào bytes rồi truyền `io.BytesIO(icon_bytes)`.
- `icon_size_ratio` (float): Tỷ lệ kích thước icon so với QR (mặc định 0.25)
- `error_correction` (int): Mức sửa lỗi QR, mặc định `qrcode.ERROR_CORRECT_H`

**Trả về:**
- `str`: Hình ảnh QR code dạng base64

**Ví dụ:**

```python
import io
from vnqr import generate_qr_image_with_icon

with open("logo.png", "rb") as f:
    icon_bytes = f.read()

qr_image_base64 = generate_qr_image_with_icon(
    qr_string=vietqr_string,
    icon_path=io.BytesIO(icon_bytes),
)
```

## 💡 Examples / Ví dụ sử dụng

### Example 1: Sử dụng đơn giản nhất

Xem file [`examples/simple_example.py`](examples/simple_example.py):

```python
from vnqr import generate_vietqr_string, generate_qr_image

qr_string = generate_vietqr_string(
    bank_bin="970425",
    bank_account="123456789",
    total_amount=100000,
    content="Thanh toan don hang"
)

qr_image = generate_qr_image(qr_string)
print("VietQR String:", qr_string)
```

Chạy ví dụ:

```bash
python examples/simple_example.py
```

### Example 2: Sử dụng cơ bản với HTML (xem trực quan QR)

Xem file [`examples/basic_usage.py`](examples/basic_usage.py):

```python
from vnqr import generate_vietqr_string, generate_qr_image

# Tạo chuỗi VietQR
vietqr_string = generate_vietqr_string(
    bank_bin="970425",
    bank_account="123456789",
    total_amount=100000,
    content="Thanh toan don hang"
)

# Tạo QR code image
qr_image_base64 = generate_qr_image(vietqr_string)

# Lưu vào file HTML để xem
# ... (xem file example để biết chi tiết)
```

Chạy ví dụ:

```bash
python examples/basic_usage.py
```

Kết quả:

- File `vietqr_example.html` được tạo trong thư mục `examples/`
- Mở file này bằng trình duyệt, bạn sẽ thấy:
  - **Ảnh QR code** có thể quét bằng app ngân hàng
  - **Thông tin giao dịch**: BIN, số tài khoản, số tiền, nội dung
  - **Chuỗi VietQR** đầy đủ hiển thị bên dưới ảnh

### Example 3: Lưu QR code vào file

Xem file [`examples/save_qr_image.py`](examples/save_qr_image.py):

```python
import base64
from vnqr import generate_vietqr_string, generate_qr_image

vietqr_string = generate_vietqr_string(
    bank_bin="970422",
    bank_account="987654321",
    total_amount=500000,
    content="Noi dung chuyen khoan"
)

qr_image_base64 = generate_qr_image(vietqr_string)

# Lưu vào file PNG
image_data = base64.b64decode(qr_image_base64)
with open("vietqr_code.png", "wb") as f:
    f.write(image_data)
```

Chạy ví dụ:

```bash
python examples/save_qr_image.py
```

Kết quả:

- File ảnh `vietqr_code.png` được tạo trong thư mục `examples/`
- Đây là QR code hoàn chỉnh, có thể mở trực tiếp bằng trình xem ảnh hoặc quét bằng ứng dụng ngân hàng

📸 **Ảnh minh họa QR code tạo từ ví dụ:**

- QR code cơ bản (không icon):

  ![VietQR sample](examples/vietqr_code.png)

### Example 4: Tạo VietQR code với icon ở giữa

Xem file [`examples/qr_with_icon.py`](examples/qr_with_icon.py):

```python
import base64
from pathlib import Path

from vnqr import generate_vietqr_string, generate_qr_image_with_icon


def main():
    vietqr_string = generate_vietqr_string(
        bank_bin="970425",
        bank_account="123456789",
        total_amount=100000,
        content="Thanh toan don hang",
    )

    icon_path = "vn_flag.png"  # hoặc logo thương hiệu của bạn

    qr_image_base64 = generate_qr_image_with_icon(
        qr_string=vietqr_string,
        icon_path=icon_path,
        icon_size_ratio=0.15,
    )

    with open("vietqr_with_icon.png", "wb") as f:
        f.write(base64.b64decode(qr_image_base64))
```

Chạy ví dụ:

```bash
python examples/qr_with_icon.py
```

Kết quả:

- Tạo file `vietqr_with_icon.png` trong thư mục `examples/`
- QR code có **icon/logo ở giữa**, vẫn đảm bảo khả năng quét nhờ sử dụng error correction level cao
- Script tự tạo một icon demo (`vn_flag.png`) nếu chưa có sẵn

📸 **Ảnh minh họa QR code tạo từ ví dụ:**

- QR code có icon ở giữa:

  ![VietQR sample with icon](examples/vietqr_with_icon.png)

### Example 5: Crawl danh sách ngân hàng từ API VietQR

Xem file [`examples/crawl_banks.py`](examples/crawl_banks.py):

```python
from vnqr.tools import crawl_bank_info


def main():
    crawl_bank_info(output_file="banks.json")
```

Chạy ví dụ:

```bash
python examples/crawl_banks.py
```

Kết quả:

- Gọi API `https://api.vietqr.io/v2/banks` để lấy danh sách ngân hàng mới nhất
- Lưu dữ liệu vào file `banks.json` (bao gồm mã BIN, tên ngân hàng, trạng thái hỗ trợ chuyển khoản…)
- In thống kê nhanh: tổng số ngân hàng, bao nhiêu ngân hàng hỗ trợ chuyển khoản, liệt kê vài ngân hàng đầu tiên

Bạn cũng có thể chạy trực tiếp module tiện ích:

```bash
python -m vnqr.tools.craw_bank
```

## 🏦 Mã BIN của các ngân hàng phổ biến

Dưới đây là một số mã BIN phổ biến (6 chữ số):

| Ngân hàng | Mã BIN |
|-----------|--------|
| Techcombank | 970425 |
| Vietinbank | 970422 |
| Vietcombank | 970436 |
| BIDV | 970418 |
| Agribank | 970405 |
| ACB | 970416 |
| VPBank | 970432 |
| TPBank | 970423 |
| MBBank | 970422 |

> **Lưu ý:** Mã BIN có thể khác nhau tùy theo loại thẻ. Vui lòng kiểm tra với ngân hàng của bạn để có mã BIN chính xác.

## 🔧 Yêu cầu hệ thống

- Python >= 3.10
- Dependencies:
  - `crcmod >= 1.7` - Tính toán CRC
  - `pypng >= 0.20220715.0` - Xử lý hình ảnh PNG
  - `qrcode >= 8.2` - Tạo QR code

## 📝 Cấu trúc dự án

```
vnqr/
├── src/
│   └── vnqr/
│       ├── __init__.py
│       ├── constants.py      # Các hằng số VietQR
│       ├── crc.py            # Tính toán CRC
│       ├── element.py        # Class Element
│       ├── qr.py             # Tạo QR code image
│       └── vietqr.py         # Tạo chuỗi VietQR
├── examples/                 # Các ví dụ sử dụng
├── tests/                    # Unit tests
├── pyproject.toml
└── README.md
```

## 🧪 Testing

Chạy tests:

```bash
pytest
```

Với coverage:

```bash
pytest --cov=vnqr
```

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón! Vui lòng:

1. Fork dự án
2. Tạo branch cho feature mới (`git checkout -b feature/AmazingFeature`)
3. Commit các thay đổi (`git commit -m 'Add some AmazingFeature'`)
4. Push lên branch (`git push origin feature/AmazingFeature`)
5. Mở Pull Request

## 📄 License

Dự án này được phân phối dưới giấy phép MIT. Xem file [LICENSE](LICENSE) để biết thêm chi tiết.

## 👤 Author

**Do Quoc Vuong**
- Email: vuongtlt13@gmail.com
- GitHub: [@vuongtlt13](https://github.com/vuongtlt13)

## 🔗 Links

- [Homepage](https://github.com/vuongtlt13/vietqr)
- [Issues](https://github.com/vuongtlt13/vietqr/issues)
- [License](https://opensource.org/licenses/MIT)

## ⚠️ Lưu ý

- Package này tạo VietQR code theo tiêu chuẩn NAPAS
- Mã BIN cần phải chính xác để QR code hoạt động đúng
- Đảm bảo số tiền và thông tin giao dịch là hợp lệ
- QR code được tạo là QR động (one-time use)

## 🙏 Acknowledgments

- NAPAS - Tiêu chuẩn VietQR
- Thư viện [qrcode](https://github.com/lincolnloop/python-qrcode) - Tạo QR code

---

Made with ❤️ in Vietnam

