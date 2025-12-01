"""
Example: Tạo VietQR code với icon ở giữa
Thêm logo/icon vào giữa mã QR code để branding
"""

import base64
from pathlib import Path

from vnqr import generate_vietqr_string, generate_qr_image_with_icon


def main():
    """Tạo VietQR code với icon ở giữa"""
    
    print("=" * 60)
    print("Tạo VietQR code với icon ở giữa")
    print("=" * 60)
    print()
    
    # Thông tin giao dịch
    bank_bin = "970425"  # Techcombank
    bank_account = "123456789"
    total_amount = 100000  # 100,000 VNĐ
    content = "Thanh toan don hang"
    
    # Tạo chuỗi VietQR
    vietqr_string = generate_vietqr_string(
        bank_bin=bank_bin,
        bank_account=bank_account,
        total_amount=total_amount,
        content=content,
    )
    
    print("✅ Đã tạo chuỗi VietQR")
    print()
    
    # Đường dẫn đến file icon (PNG, JPG, v.v.)
    # Bạn có thể thay bằng đường dẫn đến logo của bạn
    icon_path = "vn_flag.png"  # Thay bằng đường dẫn icon của bạn
    
    # Kiểm tra xem file icon có tồn tại không
    if not Path(icon_path).exists():
        print(f"⚠️  File icon không tìm thấy: {icon_path}")
        print("💡 Tạo một icon đơn giản để demo...")

        # Tạo một icon đơn giản bằng PIL nếu file không tồn tại
        try:
            from PIL import Image, ImageDraw

            # Tạo một icon đơn giản (hình vuông với chữ VN)
            icon_size = 200
            icon = Image.new("RGBA", (icon_size, icon_size), (0, 0, 0, 0))
            draw = ImageDraw.Draw(icon)

            # Vẽ hình tròn nền
            margin = 20
            draw.ellipse(
                [margin, margin, icon_size - margin, icon_size - margin],
                fill=(0, 100, 200, 255),  # Màu xanh
            )

            # Vẽ chữ VN (đơn giản)
            # Vẽ chữ V
            draw.polygon(
                [
                    (50, 50),
                    (50, 150),
                    (75, 150),
                    (100, 100),
                    (125, 150),
                    (150, 150),
                    (150, 50),
                    (125, 50),
                    (100, 100),
                    (75, 50),
                ],
                fill=(255, 255, 255, 255),
            )

            # Lưu icon tạm
            icon.save(icon_path)
            print(f"✅ Đã tạo icon demo tại: {icon_path}")

        except ImportError:
            print("❌ Cần Pillow để tạo icon demo")
            print("   Hãy tạo file icon.png (kích thước khoảng 200x200px) và chạy lại")
            return

    print(f"🖼️  Đang tạo QR code với icon: {icon_path}")
    print()
    
    try:
        # Tạo QR code với icon
        # icon_size_ratio: tỷ lệ kích thước icon (0.25 = 25% kích thước QR code)
        qr_image_base64 = generate_qr_image_with_icon(
            qr_string=vietqr_string,
            icon_path=icon_path,
            icon_size_ratio=0.15,  # Icon chiếm 25% kích thước QR code
        )
        
        # Lưu vào file
        output_file = "vietqr_with_icon.png"
        with open(output_file, "wb") as f:
            f.write(base64.b64decode(qr_image_base64))
        
        print(f"✅ Đã tạo QR code với icon!")
        print(f"   File output: {output_file}")
        print()
        print("💡 Tips:")
        print("   - icon_size_ratio nên từ 0.15 đến 0.3 (15% - 30%)")
        print("   - Icon quá lớn có thể làm QR code không scan được")
        print("   - Nên dùng icon có nền trong suốt (PNG)")
        print("   - Error correction level cao (H) giúp QR code vẫn scan được")
        
    except ImportError as e:
        print(f"❌ Lỗi: {e}")
        print("   Cần cài đặt Pillow: pip install Pillow")
    except Exception as e:
        print(f"❌ Có lỗi xảy ra: {e}")


if __name__ == "__main__":
    main()

