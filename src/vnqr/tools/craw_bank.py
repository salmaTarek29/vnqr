"""
Crawl thông tin ngân hàng từ API VietQR
Lấy danh sách ngân hàng và lưu vào file banks.json

Cách sử dụng:
    pip install requests
    python src/vnqr/tools/craw_bank.py

Hoặc:
    python -m vnqr.tools.craw_bank

API: https://api.vietqr.io/v2/banks
"""

import json
from pathlib import Path
from typing import Any

try:
    import requests
except Exception:
    print("Module requests not installed!")
    raise


def fetch_banks() -> dict[str, Any]:
    """
    Gọi API để lấy danh sách ngân hàng từ VietQR API

    Returns:
        dict: Dữ liệu JSON từ API

    Raises:
        requests.RequestException: Nếu có lỗi khi gọi API
    """
    url = "https://api.vietqr.io/v2/banks"
    
    print(f"🔄 Đang gọi API: {url}")
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception nếu status code không phải 2xx
        
        data = response.json()
        
        if data.get("code") == "00":
            print(f"✅ Lấy dữ liệu thành công! Tổng cộng {len(data.get('data', []))} ngân hàng")
        else:
            print(f"⚠️  API trả về code: {data.get('code')}, desc: {data.get('desc')}")
        
        return data
        
    except requests.Timeout:
        raise requests.RequestException("⏱️  Timeout khi gọi API. Vui lòng thử lại.")
    except requests.RequestException as e:
        raise requests.RequestException(f"❌ Lỗi khi gọi API: {str(e)}")


def save_banks_to_file(data: dict[str, Any], output_file: str) -> None:
    """
    Lưu dữ liệu ngân hàng vào file JSON

    Args:
        data: Dữ liệu từ API
        output_file: Tên file output (mặc định: banks.json)
    """
    output_path = Path(output_file)
    
    print(f"💾 Đang lưu dữ liệu vào file: {output_path.absolute()}")
    
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Đã lưu thành công vào {output_path.absolute()}")
        
        # In thống kê
        banks = data.get("data", [])
        if banks:
            print(f"\n📊 Thống kê:")
            print(f"  - Tổng số ngân hàng: {len(banks)}")
            
            # Đếm số ngân hàng hỗ trợ transfer
            transfer_supported = sum(1 for bank in banks if bank.get("transferSupported") == 1)
            print(f"  - Ngân hàng hỗ trợ chuyển khoản: {transfer_supported}")
            
            # In một vài ngân hàng đầu tiên
            print(f"\n📋 Một số ngân hàng:")
            for bank in banks[:5]:
                print(f"  - {bank.get('shortName')} ({bank.get('code')}): BIN {bank.get('bin')}")
            
            if len(banks) > 5:
                print(f"  ... và {len(banks) - 5} ngân hàng khác")
    
    except IOError as e:
        raise IOError(f"❌ Lỗi khi ghi file: {str(e)}")


def crawl_bank_info(output_file: str="banks.json") -> None:
    """Hàm main để chạy script"""
    try:
        # Gọi API lấy dữ liệu
        data = fetch_banks()
        
        # Lưu vào file
        save_banks_to_file(data, output_file=output_file)
        
        print("\n🎉 Hoàn thành!")
        
    except Exception as e:
        print(f"\n❌ Có lỗi xảy ra: {str(e)}")
        raise
