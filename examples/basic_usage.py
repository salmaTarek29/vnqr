"""
Example: Sử dụng cơ bản vnqr package
Tạo chuỗi VietQR và hình ảnh QR code
"""

from vnqr import generate_vietqr_string, generate_qr_image


def main():
    # Thông tin ngân hàng và tài khoản
    bank_bin = "970425"  # Mã BIN của ngân hàng (VD: Techcombank)
    bank_account = "123456789"  # Số tài khoản
    total_amount = 100000  # Số tiền (VNĐ)
    content = "Thanh toan don hang"  # Nội dung giao dịch

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

    # Tạo hình ảnh QR code (dạng base64)
    qr_image_base64 = generate_qr_image(vietqr_string)

    print("QR Code Image (Base64):")
    print(qr_image_base64[:100] + "...")  # In một phần để demo
    print("\n" + "=" * 50 + "\n")

    # Lưu QR code vào file HTML để xem
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>VietQR Example</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                padding: 20px;
                text-align: center;
            }}
            .qr-container {{
                margin: 20px auto;
                padding: 20px;
                border: 1px solid #ddd;
                border-radius: 8px;
                display: inline-block;
            }}
            img {{
                max-width: 300px;
            }}
            .info {{
                margin-top: 20px;
                text-align: left;
                display: inline-block;
            }}
        </style>
    </head>
    <body>
        <h1>VietQR Example</h1>
        <div class="qr-container">
            <img src="data:image/png;base64,{qr_image_base64}" alt="VietQR Code">
            <div class="info">
                <p><strong>Bank BIN:</strong> {bank_bin}</p>
                <p><strong>Account:</strong> {bank_account}</p>
                <p><strong>Amount:</strong> {total_amount:,} VNĐ</p>
                <p><strong>Content:</strong> {content}</p>
            </div>
        </div>
        <div style="margin-top: 20px;">
            <p><strong>VietQR String:</strong></p>
            <p style="word-break: break-all; max-width: 600px; margin: 0 auto;">
                {vietqr_string}
            </p>
        </div>
    </body>
    </html>
    """

    with open("vietqr_example.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("✅ Đã tạo file vietqr_example.html - Mở file này trong trình duyệt để xem QR code!")


if __name__ == "__main__":
    main()

