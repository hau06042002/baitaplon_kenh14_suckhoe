import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time

# URL của chuyên mục Sức Khỏe
url = "https://kenh14.vn/suc-khoe.chn"

# Hàm thu thập dữ liệu
def scrape_data():
    response = requests.get(url)
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
        print(f"Không thể truy cập trang web. Mã lỗi: {response.status_code}")

# Lên lịch chạy lúc 7:15 sáng mỗi ngày
schedule.every().day.at("06:00").do(scrape_data)

print("Đang chờ đến thời gian chạy...")
while True:
    schedule.run_pending()
    time.sleep(1)