# Hệ thống Backend

## Giới thiệu
Dự án này là hệ thống quản lý nhân sự, xây dựng theo kiến trúc Hexagonal, sử dụng Python và SQLAlchemy.

## Yêu cầu hệ thống
- Python >= 3.10
- pip
- Cơ sở dữ liệu (ví dụ: PostgreSQL, SQLite...)

## Cài đặt

1. **Clone dự án**
   ```bash
   git clone <link-repo>
   ```

2. **Cài đặt các thư viện**
   ```bash
   pip install -r requirements.txt
   ```

3. **Cấu hình database**
   - Chỉnh sửa file cấu hình kết nối database tại:  
     `src/infrastructure/database/sessions.py`  
   - Hoặc tạo file .env và thêm URL_DB trong đó

4. **Khởi tạo database**
   - Nếu dùng SQLAlchemy, có thể chạy lệnh migrate hoặc tự động tạo bảng:
     ```bash
     alembic upgrade head
     ```

## Chạy ứng dụng

1. **Khởi động API**
   - Nếu dùng FastAPI:
     ```bash
     python main.py
     ```

2. **Truy cập API**
   - Mở trình duyệt và truy cập:  
     ```
     http://localhost:8000
     ```
   - Xem tài liệu API:  
     ```
     http://localhost:8000/docs
     ```

## Các API chính

- **Tạo nhân viên mới**
  - `POST /employees`
  - Body: `{ "name": "...", "email": "...", "position": "...", "department": "...", "start_date": "YYYY-MM-DD" }`

- **Lấy danh sách nhân viên theo phòng ban**
  - `GET /employees?department=...`

- **Cập nhật ca làm việc cho nhân viên**
  - `PUT /schedules`
  - Body: `{ "employee_id": ..., "work_day": "YYYY-MM-DD", "shift": "morning|afternoon|full_day" }`

## Kiến trúc dự án

- `src/api/`: Định nghĩa các route API
- `src/app/use_cases/`: Xử lý nghiệp vụ
- `src/domain/`: Định nghĩa model, port
- `src/infrastructure/`: Adapter cho database, service


**1. API tạo nhân viên mới**
Luồng xử lý:
- API Route
  Định nghĩa tại: employee.py
  Endpoint: POST /employees
  Nhận dữ liệu JSON từ client (name, email, position, department, start_date).
  
- Validation
  Được gọi từ: employee_validations.py
  Kiểm tra các trường bắt buộc, validate email, kiểm tra email đã tồn tại chưa.
  
- DTO (Data Transfer Object)
  Được tạo tại: create_employee.py
  Đóng gói dữ liệu hợp lệ để truyền vào use case.
  
- Use Case
  Được xử lý tại: create_employee.py
  Thực hiện logic nghiệp vụ: kiểm tra email, tạo mới nhân viên.
  
- Repository
  Tương tác với DB tại: employee_repository.py
  Thực hiện lưu nhân viên vào database.
  
- Model
  Định nghĩa cấu trúc nhân viên tại: employee.py
  Sử dụng SQLAlchemy để ánh xạ với bảng nhân viên.
  
- Response
  Trả về JSON thông tin nhân viên vừa tạo.

**2. API lấy danh sách nhân viên theo phòng ban**
Luồng xử lý:
- API Route
  Định nghĩa tại: employee.py
  Endpoint: GET /employees?department=...
  Nhận tham số truy vấn từ client.
  
- Validation
  Được gọi từ: employee_validations.py
  Kiểm tra tham số truy vấn, validate các tiêu chí lọc.
  
- DTO
  Được tạo tại: list_employee.py
  Đóng gói tiêu chí lọc, phân trang.
  
- Use Case
  Được xử lý tại: list_employee.py
  Thực hiện logic truy vấn danh sách nhân viên theo phòng ban, lọc, phân trang.
  
- Repository
  Tương tác với DB tại: employee_repository.py
  Truy vấn danh sách nhân viên theo điều kiện.
  
- Model
  Định nghĩa tại: employee.py
  Sử dụng để ánh xạ dữ liệu trả về.
  
- Response
  Trả về JSON danh sách nhân viên.

**3. API cập nhật ca làm việc cho nhân viên**
Luồng xử lý:
- API Route
  Định nghĩa tại: schedule.py
  Endpoint: PUT /schedules hoặc POST /schedules
  Nhận dữ liệu JSON (employee_id, work_day, shift).
  
- Validation
  Được gọi từ: schedule_validations.py
  Kiểm tra dữ liệu đầu vào, validate ngày, ca làm việc.
  
- DTO
  Được tạo tại: update_schedule.py
  Đóng gói dữ liệu hợp lệ.
  
- Use Case
  Được xử lý tại: update_schedule.py
  Kiểm tra lịch làm việc đã tồn tại chưa, cập nhật hoặc tạo mới.
  
- Repository
  Tương tác với DB tại: schedule_repository.py
  Truy vấn, cập nhật hoặc thêm mới lịch làm việc.
  
- Model
  Định nghĩa tại: schedule.py
  Sử dụng để ánh xạ dữ liệu lịch làm việc.
  
- Response
  Trả về thông báo đã cập nhật hoặc đã thêm mới.

