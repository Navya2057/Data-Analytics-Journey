# Mini ETL Pipeline

## 📌 Project Overview
This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using Python, Pandas, and SQLite.

## 🚀 Workflow
1. Extract data from a CSV file.
2. Transform the data by removing duplicates and updating values.
3. Load the cleaned data into a SQLite database.

## 🛠️ Technologies Used
- Python
- Pandas
- SQLite

## 📂 Project Structure

mini-etl-pipeline/
├── data/
│   └── employees.csv
├── output/
│   └── employees.db
├── etl.py
├── requirements.txt
└── README.md

## 🔄 ETL Architecture

CSV File
↓
Extract (Pandas)
↓
Transform (Clean Data)
↓
Load (SQLite Database)

## ▶️ How to Run

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the ETL pipeline:
   ```
   python etl.py
   ```

## 📊 Output
The processed data is stored in a SQLite database (`employees.db`).

## 👩‍💻 Author
Navya Vashishth
