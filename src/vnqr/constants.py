from typing import List


class VietQRField:
    # Phiên bản dữ liệu
    PAYLOAD_FORMAT_INDICATOR = "00"

    # Phương thức khởi tạo
    INITIATION_METHOD = "01"

    # Thông tin định danh ĐVCNTT
    MERCHANT_ACCOUNT_INFO = "38"

    # Mã danh mục ĐVCNTT
    MERCHANT_CATEGORY_CODE = "52"

    # Mã tiền tệ
    TRANSACTION_CURRENCY = "53"

    # Số tiền GD
    TRANSACTION_AMOUNT = "54"

    # Chỉ thị cho Tip và Phí GD
    CONVENIENCE_INDICATOR = "55"

    # Mã quốc gia
    COUNTRY_CODE = "58"

    # Thông tin bổ sung
    ADDITIONAL_DATA = "62"

    CRC = "63"

    @classmethod
    def all(cls) -> List[str]:
        return [
            getattr(cls, attr)
            for attr in dir(cls)
            if not callable(getattr(cls, attr)) and not attr.startswith("__")
        ]


# ID = 38
class VietQRMerchantInfoField:
    # Định danh duy nhất toàn cầu - GUID
    GUID = "00"

    # Tổ chức thụ hưởng(NHTV,TGTT)
    ORG_INFO = "01"

    # Mã dịch vụ
    SERVICE_CODE = "02"

    @classmethod
    def all(cls) -> List[str]:
        return [
            getattr(cls, attr)
            for attr in dir(cls)
            if not callable(getattr(cls, attr)) and not attr.startswith("__")
        ]
