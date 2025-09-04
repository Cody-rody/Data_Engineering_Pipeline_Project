  # Data Engineering Pipeline Project

## Overview
This project demonstrates a simple data pipeline using **Python (Pandas + SQLite)**.  
The pipeline loads raw sales data (JSON), audits it, cleans it, stores it in a SQLite database,  
and performs analysis with SQL queries.

## Steps
1. **Audit Raw Data** → (`data_audit.py`)
2. **Clean Data** → (`explore_data.py`)
3. **Load into SQLite** → (`load_to_sql.py`)
4. **SQL Analysis** → (`query_sql.py`)

## Folder Structure
- `data/` → raw, cleaned, and database files
- `scripts/` → Python scripts for each stage
- `requirements.txt` → Python dependencies

## Run the Project
```bash
# 1. Activate virtual environment (if not already active)
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Mac/Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run step by step
python scripts/data_audit.py
python scripts/explore_data.py
python scripts/load_to_sql.py
python scripts/query_sql.py
