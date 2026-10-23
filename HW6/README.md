# Homework 6: Docker Microservices System

本專案實作了一個基於 Docker 與 Docker Compose 的微服務架構系統，包含 Web 伺服器、反向代理、資料庫與後端執行環境。

## 系統元件
1. **Nginx**: 作為反向代理伺服器（Reverse Proxy），統一對外提供服務並將請求轉發至後端。
2. **Python (Flask)**: 後端應用程式與網頁介面伺服器，負責處理商業邏輯。
3. **PostgreSQL**: 關聯式資料庫，用於儲存資料並透過 Docker Volume 達到持久化。

## 快速啟動
在根目錄執行以下指令：
```bash
docker-compose up --build

啟動後，請打開瀏覽器訪問：http://localhost:8080

---

### 2. `docker-compose.yml` (根目錄)
```yaml
version: '3.8'

services:
  db:
    image: postgres:15-alpine
    container_name: hw6_db
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  python-app:
    build: ./python-app
    container_name: hw6_python_app
    environment:
      - DB_HOST=db
      - DB_NAME=mydb
      - DB_USER=myuser
      - DB_PASS=mypassword
    depends_on:
      - db
    ports:
      - "5000:5000"

  nginx:
    image: nginx:alpine
    container_name: hw6_nginx
    ports:
      - "8080:80"
    volumes:
      - ./nginx/default.conf:/etc/nginx/conf.d/default.conf
    depends_on:
      - python-app

volumes:
  postgres_data: