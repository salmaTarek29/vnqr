"""
Example: Lưu QR code image vào file
Tạo QR code và lưu dưới dạng file PNG
"""

import base64
from vnqr import generate_vietqr_string, generate_qr_image


def save_qr_image_to_file(base64_string: str, output_path: str):
    """Lưu QR code từ base64 string vào file PNG"""
    image_data = base64.b64decode(base64_string)
    with open(output_path, "wb") as f:
        f.write(image_data)
    print(f"✅ Đã lưu QR code vào file: {output_path}")


def main():
    # Thông tin giao dịch
    bank_bin = "970422"  # Ví dụ: Vietinbank
    bank_account = "987654321"
    total_amount = 500000  # 500,000 VNĐ
    content = "Noi dung chuyen khoan"

    # Tạo chuỗi VietQR
    vietqr_string = generate_vietqr_string(
        bank_bin=bank_bin,
        bank_account=bank_account,
        total_amount=total_amount,
        content=content,
    )

    print("VietQR String:")
    print(vietqr_string)
    print("\n" + "=" * 50 + "\n")

    # Tạo QR code image
    qr_image_base64 = generate_qr_image(vietqr_string)

    # Lưu vào file
    save_qr_image_to_file(qr_image_base64, "vietqr_code.png")

    # Hiển thị thông tin
    print(f"\n📋 Thông tin giao dịch:")
    print(f"  - Mã BIN: {bank_bin}")
    print(f"  - Số tài khoản: {bank_account}")
    print(f"  - Số tiền: {total_amount:,} VNĐ")
    print(f"  - Nội dung: {content}")


if __name__ == "__main__":
    main()

