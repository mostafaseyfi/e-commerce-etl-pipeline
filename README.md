E-commerce ETL Pipeline

🇬🇧 English

📌 Project Overview

E-commerce ETL Pipeline is a portfolio project that demonstrates how to build a simple and practical ETL (Extract, Transform, Load) data pipeline for an e-commerce system.

The project simulates an e-commerce data source using a FastAPI-based Fake API, extracts the data with Python, cleans and transforms it using Pandas, stores processed files as CSV, and finally loads the data into PostgreSQL for further analysis.

The project also includes automated tests using Pytest and containerized PostgreSQL using Docker Compose.

---

🏗️ Architecture

                ┌─────────────────┐
                │   Fake REST API │
                │    (FastAPI)    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │     Extract     │
                │    (Python)     │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │    Transform    │
                │    (Pandas)     │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Processed CSV   │
                │      Files      │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   PostgreSQL    │
                │    Database     │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ SQL Analytics   │
                └─────────────────┘

---

🚀 Features

- Extract data from REST API endpoints
- Data cleaning and validation with Pandas
- Convert data types and normalize text fields
- Remove duplicate records
- Validate numeric values and statuses
- Save transformed data as CSV
- Load data into PostgreSQL
- Relational database schema with foreign keys
- Dockerized PostgreSQL environment
- Automated tests with Pytest
- Environment-based database configuration
- Modular ETL architecture

---

📊 Data Entities

The project works with the following entities:

- Customers
- Products
- Orders
- Order Items
- Payments

Example relationships:

Customers
    │
    └── Orders
           │
           ├── Order Items ─── Products
           │
           └── Payments

---

🛠️ Technologies

Technology| Purpose
Python| ETL development
FastAPI| Fake REST API
Requests| API data extraction
Pandas| Data transformation
PostgreSQL| Data storage
SQLAlchemy| Database connection and loading
Pytest| Automated testing
Docker| Containerization
Docker Compose| PostgreSQL environment
SQL| Data modeling and analytics
python-dotenv| Environment configuration

---

📁 Project Structure

e-commerce-etl-pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── init.py
│   ├── api.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│
├── sql/
│   ├── schema.sql
│   └── analytics.sql
│
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .gitignore
├── pytest.ini
└── README.md

---

⚙️ Installation

1. Clone the repository

git clone <YOUR_GITHUB_REPOSITORY_URL>
cd e-commerce-etl-pipeline

2. Create a virtual environment

python -m venv .venv

Activate it on Windows:

.venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

---

🔐 Environment Variables

Create a ".env" file in the project root:

POSTGRES_HOST=localhost
POSTGRES_PORT=5433
POSTGRES_DB=ecommerce
POSTGRES_USER=ecommerce_user
POSTGRES_PASSWORD=ecommerce_password

«".env" should not be committed to GitHub. The project includes ".env.example" as a template.»

---

🐘 Start PostgreSQL

Make sure Docker Desktop is running.

Then:

docker compose up -d postgres

Check the container:

docker compose ps

The PostgreSQL container should show a healthy/running status.

---
🌐 Start the Fake API

Open a terminal in the project root:

uvicorn src.api:app --reload

The API will be available at:

http://127.0.0.1:8000

FastAPI documentation:

http://127.0.0.1:8000/docs

Available endpoints:

GET /customers
GET /products
GET /orders
GET /order-items
GET /payments

---

▶️ Run the ETL Pipeline

Keep the Fake API running and open another terminal.

Run:

python -m src.main

The pipeline performs these steps:

Extract
   ↓
Transform
   ↓
Save Processed CSV
   ↓
Load into PostgreSQL

Expected output:

Starting ETL pipeline...
Step 1: Extracting data...
Extract completed.
Step 2: Transforming data...
Transform completed.
Step 3: Saving processed data...
Processed data saved.
Step 4: Loading data into PostgreSQL...
Clearing existing data...
Loading customers...
Loading products...
Loading orders...
Loading order_items...
Loading payments...
All data loaded successfully.
Load completed.
ETL pipeline completed successfully!

---

🧪 Run Tests

Run all tests with:

pytest -v

The test suite covers:

- API extraction
- Customer transformation
- Product transformation
- Order transformation
- Order item transformation
- Payment transformation
- PostgreSQL connection

Example:

7 passed

---

📈 SQL Analytics

The "sql/analytics.sql" file contains SQL queries for analyzing the e-commerce data.

Possible analytical questions include:

- Total revenue
- Number of orders
- Revenue by customer
- Revenue by product
- Best-selling products
- Orders by status
- Payment analysis
- Customer purchase behavior

---

🔄 ETL Design

Extract

Data is retrieved from the FastAPI endpoints using Python and the "requests" library.

Transform

Data is cleaned and validated using Pandas.

Examples:

- Normalize email addresses
- Remove unnecessary whitespace
- Convert dates
- Convert numeric columns
- Validate order statuses
- Remove duplicate records
- Remove invalid prices and quantities

Load

The transformed data is written to PostgreSQL using SQLAlchemy and Pandas.

The loading process uses a full refresh approach for this portfolio project: existing records are cleared before loading the latest dataset.

---

🎯 Project Goals

This project was created to demonstrate practical skills in:

- Python programming
- ETL development
- Data cleaning
- REST API integration
- Relational database design
- SQL
- PostgreSQL
- Docker
- Automated testing
- Data engineering fundamentals

---

🔮 Future Improvements

Possible future improvements include:

- Incremental data loading
- Airflow orchestration
- Logging and monitoring
- Retry mechanisms for API failures
- Data quality checks
- CI/CD with GitHub Actions
- Cloud deployment
- Advanced SQL analytics
- Data warehouse integration

---

🇮🇷 فارسی

📌 معرفی پروژه

پروژه E-commerce ETL Pipeline یک پروژه Portfolio برای نمایش نحوه ساخت یک Pipeline پردازش داده به روش ETL در یک سیستم فروشگاهی است.

در این پروژه یک Fake API با استفاده از FastAPI ایجاد شده که نقش منبع داده فروشگاه را شبیه‌سازی می‌کند.

داده‌ها توسط Python دریافت می‌شوند، با استفاده از Pandas پاک‌سازی و تبدیل می‌شوند، به صورت CSV ذخیره می‌شوند و در نهایت داخل PostgreSQL قرار می‌گیرند تا برای تحلیل‌های SQL آماده باشند.

همچنین برای پروژه تست‌های خودکار با Pytest و محیط PostgreSQL با Docker Compose در نظر گرفته شده است.

---

🏗️ معماری پروژه

             Fake API
             FastAPI
                │
                ▼
             Extract
              Python
                │
                ▼
            Transform
              Pandas
                │
                ▼
          Processed CSV
                │
                ▼
           PostgreSQL
                │
                ▼
          SQL Analytics

---

🚀 قابلیت‌های پروژه

- دریافت داده از REST API
- پاک‌سازی داده‌ها با Pandas
- اعتبارسنجی داده‌ها
- تبدیل نوع داده‌ها
- استانداردسازی متن و ایمیل
- حذف رکوردهای تکراری
- اعتبارسنجی قیمت، موجودی و تعداد
- ذخیره داده‌های پردازش‌شده به صورت CSV
- انتقال داده به PostgreSQL
- طراحی دیتابیس رابطه‌ای
- استفاده از Foreign Key
- اجرای PostgreSQL با Docker
- تست خودکار با Pytest
- مدیریت تنظیمات با Environment Variables
- ساختار ماژولار برای Pipeline

---

📊 موجودیت‌های داده

پروژه شامل پنج موجودیت اصلی است:

- Customers — مشتریان
- Products — محصولات
- Orders — سفارش‌ها
- Order Items — آیتم‌های سفارش
- Payments — پرداخت‌ها

ارتباط کلی داده‌ها:

Customers
    │
    └── Orders
           │
           ├── Order Items ─── Products
           │
           └── Payments

---

🛠️ تکنولوژی‌های استفاده‌شده

تکنولوژی| کاربرد
Python| توسعه ETL
FastAPI| ساخت Fake API
Requests| دریافت داده از API
Pandas| پاک‌سازی و Transform
PostgreSQL| ذخیره‌سازی داده
SQLAlchemy| اتصال و Load داده
Pytest| تست خودکار
Docker| Containerization
Docker Compose| اجرای PostgreSQL
SQL| طراحی و تحلیل داده
python-dotenv| مدیریت تنظیمات

---

📁 ساختار پروژه

e-commerce-etl-pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── init.py
│   ├── api.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│
├── sql/
│   ├── schema.sql
│   └── analytics.sql
│
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .gitignore
├── pytest.ini
└── README.md

---

⚙️ نصب و راه‌اندازی

1. دریافت پروژه

git clone <YOUR_GITHUB_REPOSITORY_URL>
cd e-commerce-etl-pipeline

2. ساخت Virtual Environment

python -m venv .venv

فعال‌سازی در Windows:

.venv\Scripts\activate

3. نصب Dependencies

pip install -r requirements.txt

---

🔐 تنظیم Environment Variables

در root پروژه یک فایل ".env" بسازید:

POSTGRES_HOST=localhost
POSTGRES_PORT=5433
POSTGRES_DB=ecommerce
POSTGRES_USER=ecommerce_user
POSTGRES_PASSWORD=ecommerce_password

فایل ".env" نباید در GitHub قرار بگیرد.

به همین دلیل در پروژه فایل ".env.example" قرار داده شده است.

---

🐘 اجرای PostgreSQL

ابتدا مطمئن شوید Docker Desktop در حال اجرا است.

سپس:

docker compose up -d postgres

برای بررسی:

docker compose ps

---

🌐 اجرای Fake API

در root پروژه اجرا کنید:

uvicorn src.api:app --reload

API روی این آدرس اجرا می‌شود:

http://127.0.0.1:8000

مستندات FastAPI:

http://127.0.0.1:8000/docs

Endpointهای موجود:

GET /customers
GET /products
GET /orders
GET /order-items
GET /payments

---

▶️ اجرای ETL Pipeline

در حالی که Fake API در حال اجرا است، یک Terminal جدید باز کنید و:

python -m src.main

Pipeline به ترتیب مراحل زیر را انجام می‌دهد:

Extract
   ↓
Transform
   ↓
Save Processed CSV
   ↓
Load into PostgreSQL

در صورت اجرای موفق باید پیام زیر را ببینید:

ETL pipeline completed successfully!

---

🧪 اجرای تست‌ها

برای اجرای تمام تست‌ها:

pytest -v

تست‌ها بخش‌های زیر را بررسی می‌کنند:

- دریافت داده از API
- پاک‌سازی Customers
- پاک‌سازی Products
- پاک‌سازی Orders
- پاک‌سازی Order Items
- پاک‌سازی Payments
- اتصال به PostgreSQL

خروجی موفق نمونه:

7 passed

---

📈 تحلیل داده با SQL

فایل:

sql/analytics.sql

برای اجرای Queryهای تحلیلی پروژه استفاده می‌شود.

نمونه تحلیل‌ها:

- محاسبه درآمد کل
- تعداد سفارش‌ها
- درآمد هر مشتری
- درآمد هر محصول
- محصولات پرفروش
- بررسی وضعیت سفارش‌ها
- تحلیل پرداخت‌ها
- رفتار خرید مشتریان

---

🔄 مراحل ETL

Extract

داده‌ها از Endpointهای Fake API توسط Python و کتابخانه "requests" دریافت می‌شوند.

Transform

داده‌ها با Pandas پاک‌سازی و اعتبارسنجی می‌شوند.

برخی عملیات:

- استانداردسازی ایمیل
- حذف فاصله‌های اضافی
- تبدیل تاریخ‌ها
- تبدیل ستون‌های عددی
- اعتبارسنجی وضعیت سفارش
- حذف داده‌های تکراری
- حذف قیمت و تعداد نامعتبر

Load

داده‌های نهایی با استفاده از Pandas و SQLAlchemy داخل PostgreSQL قرار می‌گیرند.

در نسخه فعلی، برای سادگی پروژه Portfolio، روش Full Refresh استفاده شده است؛ یعنی قبل از Load کردن داده‌های جدید، داده‌های قبلی پاک می‌شوند.

---

🎯 هدف پروژه

هدف اصلی این پروژه نمایش مهارت‌های عملی در زمینه‌های زیر است:
- Python
- ETL
- Data Cleaning
- REST API
- PostgreSQL
- SQL
- Docker
- Automated Testing
- Relational Database Design
- مفاهیم پایه Data Engineering

---

🔮 توسعه‌های آینده

در نسخه‌های بعدی می‌توان قابلیت‌های زیر را اضافه کرد:

- Incremental Loading
- Apache Airflow
- Logging و Monitoring
- Retry برای خطاهای API
- Data Quality Checks
- CI/CD با GitHub Actions
- Cloud Deployment
- SQL Analytics پیشرفته‌تر
- Data Warehouse

---

👨‍💻 Author

Built as a portfolio project to demonstrate practical Python, ETL, SQL, PostgreSQL, Docker, and Data Engineering skills.