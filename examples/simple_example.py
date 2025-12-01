"""
Example đơn giản nhất: Tạo VietQR string và QR code image
"""

from vnqr import generate_vietqr_string, generate_qr_image

# Thông tin giao dịch
bank_bin = "970425"  # Techcombank
bank_account = "123456789"
amount = 100000  # 100,000 VNĐ
content = "Thanh toan don hang"

# Bước 1: Tạo chuỗi VietQR
qr_string = generate_vietqr_string(
    bank_bin=bank_bin,
    bank_account=bank_account,
    total_amount=amount,
    content=content,
)
print("VietQR String:", qr_string)

# Bước 2: Tạo QR code image (base64)
qr_image = generate_qr_image(qr_string)
print("QR Code Image (base64):", qr_image[:50] + "...")

# Để lưu thành file, sử dụng:
# import base64
# with open("qr.png", "wb") as f:
#     f.write(base64.b64decode(qr_image))

