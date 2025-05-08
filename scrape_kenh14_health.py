import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time


# URL trang chủ Kenh14
base_url = "https://kenh14.vn/"

# Hàm truy cập trang chủ và chọn chuyên mục "Sức Khỏe"
def navigate_to_health_section():
    response = requests.get(base_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Tìm liên kết đến chuyên mục "Sức Khỏe"
        health_section = soup.find('a', href="/suc-khoe.chn")
        if health_section:
            health_url = f"{base_url.strip('/')}{health_section['href']}"
            return health_url
        else:
            print("Không tìm thấy chuyên mục 'Sức Khỏe'.")
            return None
    else:
        print(f"Không thể truy cập trang chủ. Mã lỗi: {response.status_code}")
        return None

# Hàm thu thập dữ liệu từ chuyên mục "Sức Khỏe"
def scrape_health_data():
    health_url = navigate_to_health_section()
    if not health_url:
        return

    response = requests.get(health_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('div', class_='knswli-right')  # Lớp chứa thông tin bài viết
        data = []
        for article in articles:
            # Lấy tiêu đề bài viết
            title = article.find('h3', class_='knswli-title').get_text(strip=True) if article.find('h3', class_='knswli-title') else "N/A"
            
            # Lấy mô tả bài viết
            description = article.find('div', class_='knswli-sapo').get_text(strip=True) if article.find('div', class_='knswli-sapo') else "N/A"
            
            # Lấy liên kết bài viết
            link = article.find('a')['href'] if article.find('a') else "N/A"
            full_link = f"https://kenh14.vn{link}" if link != "N/A" else "N/A"
            
            # Lấy URL hình ảnh
            image_tag = article.find('img')  # Tìm thẻ <img>
            if image_tag and 'src' in image_tag.attrs:
                image_url = image_tag['src']  # Lấy URL từ thuộc tính src
            elif image_tag and 'data-src' in image_tag.attrs:
                image_url = image_tag['data-src']  # Một số trang dùng data-src thay vì src
            else:
                image_url = "N/A"  # Nếu không tìm thấy hình ảnh
            
            # Thêm dữ liệu vào danh sách
            data.append({
                "Tiêu đề": title,
                "Mô tả": description,
                "Liên kết": full_link,
                "Hình ảnh": image_url
            })
        
        # Lưu dữ liệu vào file CSV
        df = pd.DataFrame(data)
        df.to_csv('kenh14_health_articles.csv', index=False, encoding='utf-8-sig')
        print("Dữ liệu đã được lưu vào file 'kenh14_health_articles.csv'")
    else:
        print(f"Không thể truy cập chuyên mục 'Sức Khỏe'. Mã lỗi: {response.status_code}")

# Gọi hàm để thực hiện thu thập dữ liệu
scrape_health_data()

# Lên lịch chạy lúc 6:00 sáng mỗi ngày
schedule.every().day.at("06:00").do(scrape_health_data)

print("Đang chờ đến thời gian chạy...")
while True:
    schedule.run_pending()
    time.sleep(1)