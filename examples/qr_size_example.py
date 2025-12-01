"""
Example: Tùy chỉnh kích thước QR code
Demo các tham số box_size và border để điều chỉnh kích thước QR code
"""

import base64

from vnqr import generate_vietqr_string, generate_qr_image


def main():
    """Tạo QR code với các kích thước khác nhau"""
    
    print("=" * 60)
    print("Demo: Tùy chỉnh kích thước QR code")
    print("=" * 60)
    print()
    
    # Tạo chuỗi VietQR
    vietqr_string = generate_vietqr_string(
        bank_bin="970425",
        bank_account="123456789",
        total_amount=100000,
        content="Thanh toan don hang",
    )
    
    print("✅ Đã tạo chuỗi VietQR")
    print()
    
    # Các cấu hình kích thước khác nhau
    configs = [
        {"box_size": 5, "border": 2, "name": "Nhỏ (mặc định)"},
        {"box_size": 10, "border": 4, "name": "Trung bình"},
        {"box_size": 15, "border": 4, "name": "Lớn"},
        {"box_size": 20, "border": 4, "name": "Rất lớn"},
    ]
    
    print("📏 Tạo QR code với các kích thước khác nhau:\n")
    
    for i, config in enumerate(configs, 1):
        print(f"{i}. {config['name']}")
        print(f"   - box_size: {config['box_size']} pixels")
        print(f"   - border: {config['border']} ô")
        
        # Tạo QR code với kích thước tùy chỉnh
        qr_image_base64 = generate_qr_image(
            qr_string=vietqr_string,
            box_size=config["box_size"],
            border=config["border"],
        )
        
        # Lưu vào file
        filename = f"vietqr_size_{i}_{config['name'].lower().replace(' ', '_')}.png"
        with open(filename, "wb") as f:
            f.write(base64.b64decode(qr_image_base64))
        
        print(f"   ✅ Đã lưu: {filename}")
        print()
    
    print("=" * 60)
    print("💡 Giải thích:")
    print("=" * 60)
    print()
    print("• box_size: Kích thước mỗi ô vuông (pixel)")
    print("  - Tăng box_size => QR code lớn hơn")
    print("  - Ví dụ: box_size=5 => mỗi ô 5x5 pixels")
    print()
    print("• border: Viền xung quanh QR code (số ô)")
    print("  - Tăng border => thêm viền trắng xung quanh")
    print("  - Ví dụ: border=2 => viền 2 ô mỗi bên")
    print()
    print("• Kích thước tổng thể:")
    print("  QR size = (số ô × box_size) + (border × 2 × box_size)")
    print()
    print("📌 Lưu ý:")
    print("  - box_size nhỏ (< 3) có thể khó scan")
    print("  - box_size lớn (> 20) tạo file lớn")
    print("  - border nên từ 2-4 để dễ scan")
    print()


if __name__ == "__main__":
    main()

