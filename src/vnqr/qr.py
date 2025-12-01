import base64
import io
from pathlib import Path
from typing import BinaryIO

import qrcode
from qrcode import ERROR_CORRECT_H, ERROR_CORRECT_L

try:
    from PIL import Image
except ImportError:
    Image = None  # type: ignore


def generate_qr_image(
    qr_string: str,
    box_size: int = 5,
    border: int = 2,
    error_correction: int = ERROR_CORRECT_L,
) -> str:
    """
    Tạo QR code image từ chuỗi

    Args:
        qr_string: Chuỗi để tạo QR code
        box_size: Kích thước mỗi ô vuông (pixel). Mặc định: 5
        border: Kích thước viền xung quanh (số ô). Mặc định: 2
        error_correction: Mức độ sửa lỗi (ERROR_CORRECT_L, M, Q, H). Mặc định L (thấp nhất)

    Returns:
        str: QR code image dạng base64

    Note:
        Kích thước QR code = (số ô × box_size) + (border × 2 × box_size)
        Ví dụ: QR 25x25 ô với box_size=5, border=2
        => (25 × 5) + (2 × 2 × 5) = 125 + 20 = 145 pixels
        Error correction cao hơn = nhiều ô hơn = QR code lớn hơn
    """
    # Tạo QR code (tự động chọn version phù hợp)
    qr = qrcode.QRCode(
        error_correction=error_correction,
        box_size=box_size,
        border=border,
    )
    qr.add_data(qr_string)
    qr.make(fit=True)

    # Tạo QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    # Lưu vào BytesIO và encode base64
    f = io.BytesIO()
    img.save(f, format="PNG")
    f.seek(0)
    image_content = f.read()
    base64_utf8_str = base64.b64encode(image_content).decode("utf-8")

    return base64_utf8_str


def generate_qr_image_with_icon(
    qr_string: str,
    icon_path: str | Path | BinaryIO,
    icon_size_ratio: float = 0.25,
    error_correction: int = ERROR_CORRECT_L,
    box_size: int = 5,
    border: int = 2,
) -> str:
    """
    Tạo QR code image với icon ở giữa

    Args:
        qr_string: Chuỗi để tạo QR code
        icon_path: Đường dẫn đến file icon (PNG, JPG, v.v.) hoặc file-like object
        icon_size_ratio: Tỷ lệ kích thước icon so với QR code (0.1 - 0.3 khuyến nghị)
        error_correction: Mức độ sửa lỗi (ERROR_CORRECT_L, M, Q, H).
                         Mặc định L (thấp nhất) - giống với generate_qr_image() để có cùng kích thước.
                         Khuyến nghị dùng ERROR_CORRECT_H khi icon lớn (>25%) để QR code vẫn scan được tốt
        box_size: Kích thước mỗi ô vuông (pixel). Mặc định: 5
        border: Kích thước viền xung quanh (số ô). Mặc định: 2

    Returns:
        str: QR code image dạng base64

    Raises:
        ImportError: Nếu Pillow chưa được cài đặt
        ValueError: Nếu icon_path không hợp lệ

    Note:
        Kích thước QR code = (số ô × box_size) + (border × 2 × box_size)
        Error correction cao hơn = nhiều ô hơn = QR code lớn hơn
        Để có cùng kích thước với generate_qr_image(), dùng cùng error_correction level
    """
    if Image is None:
        raise ImportError(
            "Pillow (PIL) is required for generating QR code with icon. "
            "Please install it: pip install Pillow"
        )

    # Tạo QR code (không fix version để tự động chọn version phù hợp)
    qr = qrcode.QRCode(
        error_correction=error_correction,
        box_size=box_size,
        border=border,
    )
    qr.add_data(qr_string)
    qr.make(fit=True)

    # Tạo QR code image (make_image() trả về PIL Image object)
    # Không dùng image_factory để đảm bảo trả về PIL Image
    qr_img_temp = qr.make_image(fill_color="black", back_color="white")

    # Đảm bảo là PIL Image object (convert sang RGB)
    if isinstance(qr_img_temp, Image.Image):
        qr_img = qr_img_temp.convert("RGB")
    else:
        # Nếu không phải PIL Image, convert qua BytesIO
        f_temp = io.BytesIO()
        qr_img_temp.save(f_temp)
        f_temp.seek(0)
        qr_img = Image.open(f_temp).convert("RGB")

    # Mở và resize icon
    if isinstance(icon_path, (str, Path)):
        icon = Image.open(icon_path)
    else:
        # File-like object
        icon = Image.open(icon_path)

    # Convert icon sang RGBA nếu cần (để hỗ trợ transparency)
    if icon.mode != "RGBA":
        icon = icon.convert("RGBA")  # type: ignore [assignment]

    # Tính toán kích thước icon
    qr_width, qr_height = qr_img.size
    icon_size = (
        int(qr_width * icon_size_ratio),
        int(qr_height * icon_size_ratio),
    )

    # Resize icon (giữ tỷ lệ)
    # Sử dụng LANCZOS resampling (có thể là Image.Resampling.LANCZOS hoặc Image.LANCZOS)
    try:
        resampling = Image.Resampling.LANCZOS  # Pillow >= 10.0.0
    except AttributeError:
        # for Pillow < 10.0.0
        resampling = Image.LANCZOS  # type: ignore [attr-defined]
    icon.thumbnail(icon_size, resampling)

    # Tạo một image mới với background trong suốt có cùng kích thước
    icon_with_bg = Image.new("RGBA", icon_size, (255, 255, 255, 0))

    # Paste icon vào giữa background
    icon_x = (icon_size[0] - icon.size[0]) // 2
    icon_y = (icon_size[1] - icon.size[1]) // 2
    icon_with_bg.paste(icon, (icon_x, icon_y), icon)

    # Tính toán vị trí để paste icon vào giữa QR code
    qr_x = (qr_width - icon_size[0]) // 2
    qr_y = (qr_height - icon_size[1]) // 2

    # Paste icon vào QR code
    qr_img.paste(icon_with_bg, (qr_x, qr_y), icon_with_bg)

    # Convert về BytesIO và encode base64
    f = io.BytesIO()
    qr_img.save(f, format="PNG")
    f.seek(0)
    image_content = f.read()
    base64_utf8_str = base64.b64encode(image_content).decode("utf-8")

    return base64_utf8_str
