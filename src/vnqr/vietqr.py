from .qr import generate_qr_image
from .constants import VietQRField, VietQRMerchantInfoField
from .crc import crc_func
from .element import Element


def generate_vietqr_string(
    bank_bin: str,
    bank_account: str,
    total_amount: int,
    content: str,
) -> str:
    # Phiên bản dữ liệu (ID 00)
    # Phiên bản dữ liệu có giá trị là “01”.
    version_element = Element(
        element_id=VietQRField.PAYLOAD_FORMAT_INDICATOR, value="01"
    )

    # Phương thức khởi tạo (ID 01)
    # - “11” = QR tĩnh – áp dụng khi mã QR cho phép thực hiện nhiều lần giao dịch.
    # - “12” = QR động – áp dụng khi mã QR chỉ cho phép thực hiện một lần giao dịch.
    init_method = Element(element_id=VietQRField.INITIATION_METHOD, value="12")

    # Thông tin định danh ĐVCNTT (ID 38)
    # ID 38 được sử dụng cho dịch vụ VietQR qua hệ thống Napas.

    # ID quy định dữ liệu với 1 trong các giá trị sau:
    # AID: luôn có giá trị “A000000727”.
    merchant_info_guid = Element(
        element_id=VietQRMerchantInfoField.GUID, value="A000000727"
    )

    # merchant_info_org_info
    merchant_info_org_info_acquirer = Element(element_id="00", value=bank_bin)
    merchant_info_org_info_consumer = Element(element_id="01", value=bank_account)
    merchant_info_org_info = Element(
        element_id=VietQRMerchantInfoField.ORG_INFO,
        value=f"{merchant_info_org_info_acquirer}{merchant_info_org_info_consumer}",
    )

    # merchant_info_service_code
    # - QRIBFTTC: dịch vụ chuyển nhanh NAPAS247 bằng mã QR đến thẻ
    # - QRIBFTTA: dịch vụ chuyển nhanh NAPAS247 bằng mã QR đến Tài khoản
    merchant_info_service_code = Element(
        element_id=VietQRMerchantInfoField.SERVICE_CODE,
        value="QRIBFTTA",
    )

    merchant_info = Element(
        element_id=VietQRField.MERCHANT_ACCOUNT_INFO,
        value=f"{merchant_info_guid}{merchant_info_org_info}{merchant_info_service_code}",
    )

    # Mã tiền tệ (ID 53)
    currency_code = Element(element_id=VietQRField.TRANSACTION_CURRENCY, value="704")

    # Số tiền giao dịch (ID 54)
    transaction_amount = Element(
        element_id=VietQRField.TRANSACTION_AMOUNT, value=f"{total_amount}"
    )

    # Mã quốc gia (ID 58)
    country_code = Element(element_id=VietQRField.COUNTRY_CODE, value="VN")

    # Thông tin bổ sung (ID 62)
    # Mục đích giao dịch (08)
    additional_info_purpose = Element(element_id="08", value=f"{content}")
    additional_info = Element(
        element_id=VietQRField.ADDITIONAL_DATA, value=f"{additional_info_purpose}"
    )

    # Mã kiểm thử giá trị - CRC (ID 63)
    before_crc_data = f"{version_element}{init_method}{merchant_info}{currency_code}{transaction_amount}{country_code}{additional_info}{VietQRField.CRC}04"
    crc_element = Element(element_id=VietQRField.CRC, value=crc_func(before_crc_data))
    return f"{version_element}{init_method}{merchant_info}{currency_code}{transaction_amount}{country_code}{additional_info}{crc_element}"


def generate_vietqr_image(
    bank_bin: str,
    bank_account: str,
    total_amount: int,
    content: str,
) -> str:
    vietqr_string = generate_vietqr_string(
        bank_bin=bank_bin,
        bank_account=bank_account,
        total_amount=total_amount,
        content=content,
    )

    return generate_qr_image(
        qr_string=vietqr_string,
    )
