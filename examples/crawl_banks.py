"""
Example: Crawl thông tin ngân hàng từ API VietQR
Sử dụng hàm crawl_bank_info để lấy danh sách ngân hàng và lưu vào file
"""

from vnqr.tools import crawl_bank_info


def main():
    """Crawl thông tin ngân hàng và lưu vào file"""
    
    # Sử dụng hàm crawl_bank_info để lấy dữ liệu và lưu vào file
    # File mặc định là "banks.json"
    print("=" * 50)
    print("Crawl thông tin ngân hàng từ API VietQR")
    print("=" * 50)
    print()
    
    crawl_bank_info(output_file="banks.json")
    
    print("\n" + "=" * 50)
    print("Bạn có thể mở file banks.json để xem dữ liệu!")
    print("=" * 50)


if __name__ == "__main__":
    main()

