"""
Tests for QR code generation functions
"""

import base64
import io
from pathlib import Path

import pytest

from vnqr.qr import generate_qr_image, generate_qr_image_with_icon
from vnqr.vietqr import generate_vietqr_string


def test_generate_qr_image_basic():
    """Test tạo QR code cơ bản"""
    qr_string = "test_qr_string"
    result = generate_qr_image(qr_string)

    # Kiểm tra kết quả là base64 string
    assert isinstance(result, str)
    assert len(result) > 0

    # Kiểm tra có thể decode thành image
    image_data = base64.b64decode(result)
    assert len(image_data) > 0


@pytest.mark.parametrize(
    "box_size,border",
    [
        (5, 2),
        (10, 4),
        (15, 4),
    ],
)
def test_generate_qr_image_with_size(box_size, border):
    """Test tạo QR code với các kích thước khác nhau"""
    qr_string = "test_qr_string"
    result = generate_qr_image(qr_string, box_size=box_size, border=border)

    assert isinstance(result, str)
    assert len(result) > 0

    image_data = base64.b64decode(result)
    assert len(image_data) > 0


def test_generate_qr_image_error_correction():
    """Test tạo QR code với các mức error correction khác nhau"""
    from qrcode import (
        ERROR_CORRECT_H,
        ERROR_CORRECT_L,
        ERROR_CORRECT_M,
        ERROR_CORRECT_Q,
    )

    qr_string = "test_qr_string"

    for error_correction in [
        ERROR_CORRECT_L,
        ERROR_CORRECT_M,
        ERROR_CORRECT_Q,
        ERROR_CORRECT_H,
    ]:
        result = generate_qr_image(
            qr_string=qr_string,
            error_correction=error_correction,
        )

        assert isinstance(result, str)
        assert len(result) > 0

        image_data = base64.b64decode(result)
        assert len(image_data) > 0


@pytest.fixture
def sample_qr_string():
    """Fixture tạo chuỗi VietQR mẫu"""
    return generate_vietqr_string(
        bank_bin="970425",
        bank_account="123456789",
        total_amount=100000,
        content="test",
    )


@pytest.fixture
def sample_icon(tmp_path):
    """Fixture tạo icon mẫu"""
    try:
        from PIL import Image, ImageDraw

        # Tạo một icon đơn giản
        icon_size = 200
        icon = Image.new("RGBA", (icon_size, icon_size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(icon)

        # Vẽ hình tròn đơn giản
        margin = 20
        draw.ellipse(
            [margin, margin, icon_size - margin, icon_size - margin],
            fill=(0, 100, 200, 255),
        )

        # Lưu vào file tạm
        icon_path = tmp_path / "test_icon.png"
        icon.save(icon_path)

        return str(icon_path)
    except ImportError:
        pytest.skip("Pillow not available")


@pytest.fixture
def sample_icon_rgb(tmp_path):
    """Fixture tạo icon RGB (không có alpha)"""
    try:
        from PIL import Image, ImageDraw

        icon_size = 200
        icon = Image.new("RGB", (icon_size, icon_size), (255, 0, 0))
        draw = ImageDraw.Draw(icon)
        draw.rectangle([50, 50, 150, 150], fill=(0, 255, 0))

        icon_path = tmp_path / "test_icon_rgb.png"
        icon.save(icon_path)

        return str(icon_path)
    except ImportError:
        pytest.skip("Pillow not available")


def test_generate_qr_image_with_icon_success(sample_qr_string, sample_icon):
    """Test tạo QR code với icon thành công"""
    result = generate_qr_image_with_icon(
        qr_string=sample_qr_string,
        icon_path=sample_icon,
    )

    # Kiểm tra kết quả là base64 string
    assert isinstance(result, str)
    assert len(result) > 0

    # Kiểm tra có thể decode thành image
    image_data = base64.b64decode(result)
    assert len(image_data) > 0

    # Kiểm tra là PNG hợp lệ
    assert image_data[:8] == b"\x89PNG\r\n\x1a\n"


def test_generate_qr_image_same_size_default_config(sample_qr_string, sample_icon):
    """Test cả 2 hàm với cùng default config tạo cùng kích thước QR code"""
    from PIL import Image

    # Dùng default config (cùng ERROR_CORRECT_L, box_size=5, border=2)
    qr_without_icon = generate_qr_image(sample_qr_string)
    qr_with_icon = generate_qr_image_with_icon(
        sample_qr_string,
        icon_path=sample_icon,
    )

    # Decode images
    img1_data = base64.b64decode(qr_without_icon)
    img2_data = base64.b64decode(qr_with_icon)

    # Kiểm tra là PNG hợp lệ
    assert img1_data[:8] == b"\x89PNG\r\n\x1a\n"
    assert img2_data[:8] == b"\x89PNG\r\n\x1a\n"

    # Mở images và so sánh kích thước (width x height)
    img1 = Image.open(io.BytesIO(img1_data))
    img2 = Image.open(io.BytesIO(img2_data))

    # Với cùng config, cả 2 QR code phải có cùng kích thước (số ô)
    # Vì cùng error correction level, box_size và border
    assert img1.size == img2.size, (
        f"QR codes should have same size with same config. "
        f"Without icon: {img1.size}, With icon: {img2.size}"
    )


def test_generate_qr_image_same_size_explicit_config(sample_qr_string, sample_icon):
    """Test cả 2 hàm với cùng explicit config tạo cùng kích thước"""
    from PIL import Image
    from qrcode import ERROR_CORRECT_L

    # Dùng cùng explicit config
    box_size = 10
    border = 4

    qr_without_icon = generate_qr_image(
        sample_qr_string,
        error_correction=ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    qr_with_icon = generate_qr_image_with_icon(
        sample_qr_string,
        icon_path=sample_icon,
        error_correction=ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )

    # Decode và so sánh kích thước
    img1 = Image.open(io.BytesIO(base64.b64decode(qr_without_icon)))
    img2 = Image.open(io.BytesIO(base64.b64decode(qr_with_icon)))

    # Phải có cùng kích thước
    assert img1.size == img2.size


def test_generate_qr_image_with_icon_path_object(sample_qr_string, sample_icon):
    """Test tạo QR code với icon từ Path object"""
    icon_path = Path(sample_icon)
    result = generate_qr_image_with_icon(
        qr_string=sample_qr_string,
        icon_path=icon_path,
    )

    assert isinstance(result, str)
    assert len(result) > 0


def test_generate_qr_image_with_icon_file_like(sample_qr_string, sample_icon):
    """Test tạo QR code với icon từ file-like object"""
    with open(sample_icon, "rb") as f:
        result = generate_qr_image_with_icon(
            qr_string=sample_qr_string,
            icon_path=f,
        )

    assert isinstance(result, str)
    assert len(result) > 0


def test_generate_qr_image_with_icon_rgb(sample_qr_string, sample_icon_rgb):
    """Test tạo QR code với icon RGB (không có alpha channel)"""
    result = generate_qr_image_with_icon(
        qr_string=sample_qr_string,
        icon_path=sample_icon_rgb,
    )

    assert isinstance(result, str)
    assert len(result) > 0


@pytest.mark.parametrize(
    "icon_size_ratio",
    [
        0.15,
        0.20,
        0.25,
        0.30,
    ],
)
def test_generate_qr_image_with_icon_size_ratios(
    sample_qr_string, sample_icon, icon_size_ratio
):
    """Test tạo QR code với các tỷ lệ kích thước icon khác nhau"""
    result = generate_qr_image_with_icon(
        qr_string=sample_qr_string,
        icon_path=sample_icon,
        icon_size_ratio=icon_size_ratio,
    )

    assert isinstance(result, str)
    assert len(result) > 0


def test_generate_qr_image_with_icon_error_correction(sample_qr_string, sample_icon):
    """Test tạo QR code với các mức error correction khác nhau"""
    from qrcode import (
        ERROR_CORRECT_H,
        ERROR_CORRECT_L,
        ERROR_CORRECT_M,
        ERROR_CORRECT_Q,
    )

    for error_correction in [
        ERROR_CORRECT_L,
        ERROR_CORRECT_M,
        ERROR_CORRECT_Q,
        ERROR_CORRECT_H,
    ]:
        result = generate_qr_image_with_icon(
            qr_string=sample_qr_string,
            icon_path=sample_icon,
            error_correction=error_correction,
        )

        assert isinstance(result, str)
        assert len(result) > 0


@pytest.mark.parametrize(
    "box_size,border",
    [
        (5, 2),
        (10, 4),
        (15, 4),
        (20, 4),
    ],
)
def test_generate_qr_image_with_icon_box_size_border(
    sample_qr_string, sample_icon, box_size, border
):
    """Test tạo QR code với icon và các kích thước box_size, border khác nhau"""
    from PIL import Image

    result = generate_qr_image_with_icon(
        qr_string=sample_qr_string,
        icon_path=sample_icon,
        box_size=box_size,
        border=border,
    )

    assert isinstance(result, str)
    assert len(result) > 0

    # Kiểm tra có thể decode thành image
    image_data = base64.b64decode(result)
    assert len(image_data) > 0

    # Verify cùng kích thước với generate_qr_image khi dùng cùng config
    qr_without_icon = generate_qr_image(
        sample_qr_string,
        box_size=box_size,
        border=border,
    )
    img1 = Image.open(io.BytesIO(base64.b64decode(qr_without_icon)))
    img2 = Image.open(io.BytesIO(image_data))

    assert img1.size == img2.size, (
        f"QR codes should have same size with box_size={box_size}, border={border}. "
        f"Without icon: {img1.size}, With icon: {img2.size}"
    )


def test_generate_qr_image_with_icon_default_box_size_border(
    sample_qr_string, sample_icon
):
    """Test tạo QR code với icon sử dụng giá trị mặc định box_size=5, border=2"""
    result = generate_qr_image_with_icon(
        qr_string=sample_qr_string,
        icon_path=sample_icon,
    )

    assert isinstance(result, str)
    assert len(result) > 0


def test_generate_qr_image_same_size_all_error_correction_levels(
    sample_qr_string, sample_icon
):
    """Test cả 2 hàm với tất cả error correction levels đều tạo cùng kích thước"""
    from PIL import Image
    from qrcode import (
        ERROR_CORRECT_H,
        ERROR_CORRECT_L,
        ERROR_CORRECT_M,
        ERROR_CORRECT_Q,
    )

    box_size = 5
    border = 2

    for error_correction in [
        ERROR_CORRECT_L,
        ERROR_CORRECT_M,
        ERROR_CORRECT_Q,
        ERROR_CORRECT_H,
    ]:
        qr_without_icon = generate_qr_image(
            sample_qr_string,
            error_correction=error_correction,
            box_size=box_size,
            border=border,
        )
        qr_with_icon = generate_qr_image_with_icon(
            sample_qr_string,
            icon_path=sample_icon,
            error_correction=error_correction,
            box_size=box_size,
            border=border,
        )

        # So sánh kích thước
        img1 = Image.open(io.BytesIO(base64.b64decode(qr_without_icon)))
        img2 = Image.open(io.BytesIO(base64.b64decode(qr_with_icon)))

        assert img1.size == img2.size, (
            f"QR codes should have same size with error_correction={error_correction}. "
            f"Without icon: {img1.size}, With icon: {img2.size}"
        )


def test_generate_qr_image_with_icon_nonexistent_file(sample_qr_string):
    """Test tạo QR code với icon file không tồn tại"""
    nonexistent_path = "/nonexistent/path/icon.png"

    with pytest.raises(Exception):  # FileNotFoundError hoặc OSError
        generate_qr_image_with_icon(
            qr_string=sample_qr_string,
            icon_path=nonexistent_path,
        )


def test_generate_qr_image_with_icon_no_pillow(monkeypatch, sample_qr_string, tmp_path):
    """Test raise ImportError khi không có Pillow"""
    # Tạo một icon file tạm
    icon_path = tmp_path / "test_icon.png"
    icon_path.touch()

    # Mock để Image là None
    import vnqr.qr as qr_module

    # Lưu Image hiện tại
    original_image = getattr(qr_module, "Image", None)

    try:
        # Set Image thành None để test ImportError
        monkeypatch.setattr(qr_module, "Image", None)

        with pytest.raises(ImportError, match="Pillow.*required"):
            generate_qr_image_with_icon(
                qr_string=sample_qr_string,
                icon_path=str(icon_path),
            )
    finally:
        # Restore original Image nếu có
        if original_image is not None:
            monkeypatch.setattr(qr_module, "Image", original_image)


def test_generate_qr_image_with_icon_valid_png(sample_qr_string, sample_icon):
    """Test QR code với icon tạo ra file PNG hợp lệ"""
    result = generate_qr_image_with_icon(
        qr_string=sample_qr_string,
        icon_path=sample_icon,
    )

    # Decode và kiểm tra là PNG hợp lệ
    image_data = base64.b64decode(result)

    # PNG file signature
    assert image_data[:8] == b"\x89PNG\r\n\x1a\n"

    # Có thể mở lại bằng PIL
    from PIL import Image

    img = Image.open(io.BytesIO(image_data))
    assert img.format == "PNG"
    assert img.mode == "RGB" or img.mode == "RGBA"


def test_generate_qr_image_with_icon_different_sizes(sample_qr_string, tmp_path):
    """Test với icon có kích thước khác nhau"""
    from PIL import Image, ImageDraw

    icon_sizes = [(100, 100), (200, 200), (300, 150)]  # Hình vuông và hình chữ nhật

    for width, height in icon_sizes:
        icon = Image.new("RGBA", (width, height), (255, 0, 0, 255))
        draw = ImageDraw.Draw(icon)
        draw.rectangle([10, 10, width - 10, height - 10], fill=(0, 255, 0, 255))

        icon_path = tmp_path / f"icon_{width}x{height}.png"
        icon.save(icon_path)

        result = generate_qr_image_with_icon(
            qr_string=sample_qr_string,
            icon_path=str(icon_path),
            icon_size_ratio=0.2,
        )

        assert isinstance(result, str)
        assert len(result) > 0
