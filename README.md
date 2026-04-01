# ✈️ Flight Ticket Booking & Cancellation Analysis Dashboard

## 📌 Project Overview

This project is an **end-to-end data analytics dashboard** built using **Python, PostgreSQL, and Streamlit**.  
It analyzes airline ticket booking data to uncover insights like pricing trends, popular routes, airline performance, and travel patterns.

---

## 🚀 Features

- 📊 Booking trend analysis  
- 💰 Average ticket price insights  
- ✈️ Airline performance comparison  
- 🗺️ Popular routes (source → destination)  
- ⏱️ Peak travel hour analysis  
- 🔁 Stops vs price analysis  
- 📈 Interactive dashboard using Streamlit  

---

## 🏗️ Tech Stack

| Layer | Technology |
|------|----------|
| Data Processing | Python (Pandas, NumPy) |
| Database | PostgreSQL |
| Backend | Python (psycopg2) |
| Visualization | Streamlit |
| Charts | Plotly / Streamlit Charts |

---

## 📂 Project Structure

flight_project/
│
├── data/
│   ├── raw_data.csv
│   ├── cleaned_data.csv
│
├── processing/
│   └── data_cleaning.py
│
├── database/
│   ├── db_connection.py
│   ├── insert_data.py
│   ├── create_tables.sql
│
├── analysis/
│   └── queries.py
│
├── dashboard/
│   └── app.py
│
├── requirements.txt
└── README.md

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

git clone https://github.com/your-username/flight-analysis-dashboard.git
cd flight-analysis-dashboard

---

### 2️⃣ Create Virtual Environment

python -m venv venv
venv\Scripts\activate

---

### 3️⃣ Install Dependencies

pip install -r requirements.txt

---

### 4️⃣ Setup PostgreSQL

CREATE DATABASE flight_db;

---

### 5️⃣ Run Data Cleaning

python processing/data_cleaning.py

---

### 6️⃣ Insert Data

python database/insert_data.py

---

### 7️⃣ Run Dashboard

streamlit run dashboard/app.py

---

## 👨‍💻 Author

Bhavesh Naik
