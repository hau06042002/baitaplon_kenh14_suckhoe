# Bài Tập Lớn: Kenh14 Health Articles Scraper

## Mô tả

Chương trình này được viết bằng Python để thu thập dữ liệu từ chuyên mục **Sức Khỏe** trên trang web Kenh14. Dữ liệu được lưu vào file CSV với các thông tin:

- **Mục đích:** Giải thích ngắn gọn về chức năng của chương trình.
- **Dữ liệu thu thập:**
  - `Tiêu đề bài viết:` Tên của bài viết.
  - `Mô tả ngắn:` Nội dung tóm tắt của bài viết.
  - `Liên kết đầy đủ:` URL dẫn đến bài viết trên trang web Kenh14.
  - `Hình ảnh:` URL của hình ảnh minh họa trong bài viết.

Chương trình sử dụng thư viện `schedule` để tự động chạy vào thời gian được chỉ định.

---

## Yêu cầu hệ thống

- **Python 3.x**: Đảm bảo bạn đã cài đặt Python trên máy tính.
- **Các thư viện Python cần thiết**:
  - `requests`: Gửi yêu cầu HTTP để lấy nội dung trang web.
  - `beautifulsoup4`: Phân tích và trích xuất dữ liệu từ HTML.
  - `pandas`: Lưu dữ liệu vào file CSV.
  - `schedule`: Lên lịch chạy tự động.

---

## Cách cài đặt và sử dụng

### 1. Clone repository

    Clone project từ GitHub về máy:

    ```bash
    git clone https://github.com/<your-username>/baitaplon_kenh14_suckhoe.git
    cd baitaplon_kenh14_suckhoe
    ```

- **Clone repository**: Hướng dẫn người dùng tải mã nguồn từ GitHub về máy.
- **Câu lệnh**:
  - `git clone`: Tải toàn bộ mã nguồn từ repository GitHub.
  - `cd baitaplon_kenh14_suckhoe`: Di chuyển vào thư mục dự án.

---

### 2. Cài đặt các thư viện cần thiết

Chạy lệnh sau để cài đặt các thư viện:

```bash
pip install -r requirements.txt
```

- **Cài đặt thư viện**:
  - File `requirements.txt` chứa danh sách các thư viện cần thiết.
  - Lệnh `pip install -r requirements.txt` sẽ tự động cài đặt tất cả các thư viện.

---

### 3. Chạy chương trình

Chạy file Python để bắt đầu chương trình:

```bash
python scrape_kenh14_health.py
```

- **Chạy chương trình**:
  - Lệnh `python scrape_kenh14_health.py` sẽ khởi động chương trình.
  - Chương trình sẽ tự động chạy vào thời gian được chỉ định (mặc định là **6:00 sáng**).
  - Dữ liệu thu thập được sẽ được lưu vào file `kenh14_health_articles.csv`.

---

### 44. **Cấu trúc file CSV**

````markdown
## Cấu trúc file CSV

File `kenh14_health_articles.csv` sẽ chứa các cột:

- **Tiêu đề**: Tiêu đề bài viết.
- **Mô tả**: Mô tả ngắn của bài viết.
- **Liên kết**: URL đầy đủ của bài viết.
- **Hình ảnh**: URL của hình ảnh trong bài viết.

## Lên lịch chạy tự động

Chương trình sử dụng thư viện `schedule` để tự động chạy vào thời gian được chỉ định. Mặc định, chương trình sẽ chạy vào **6:00 sáng mỗi ngày**. Bạn có thể thay đổi thời gian bằng cách chỉnh sửa dòng sau trong file `scrape_kenh14_health.py`:

```python
schedule.every().day.at("06:00").do(scrape_data)
```
````

- **Lên lịch chạy tự động**:
  - Mặc định, chương trình sẽ chạy vào **6:00 sáng** mỗi ngày.
  - Người dùng có thể thay đổi thời gian bằng cách chỉnh sửa dòng:
    ```python
    schedule.every().day.at("06:00").do(scrape_data)
    ```

---

### 7. **Lưu ý**

- Để chương trình hoạt động, bạn cần để file Python chạy liên tục.
- Nếu muốn chạy tự động mà không cần mở Python, bạn có thể sử dụng **Task Scheduler** trên Windows.
