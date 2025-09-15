import pandas as pd

def data_audit(file_path):
    # Load data (auto-detect format by file extension)
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
    elif file_path.endswith(".json"):
        df = pd.read_json(file_path)
    elif file_path.endswith(".xlsx") or file_path.endswith(".xls"):
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Use CSV, JSON, or Excel.")

    print("\n" + "="*40)
    print(" 🔎 DATA AUDIT REPORT ")
    print("="*40)

    print("\n--- Preview (first 5 rows) ---")
    print(df.head())

    print("\n--- Shape ---")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    print("\n--- Column Names ---")
    print(df.columns.tolist())

    print("\n--- Data Types ---")
    print(df.dtypes)

    print("\n--- Missing Values ---")
    print(df.isnull().sum())

    print("\n--- Duplicate Rows ---")
    print(df.duplicated().sum())

    print("\n--- Summary Stats ---")
    try:
         print(df.describe(include="all").transpose())
    except Exception as e:
        print("Could not generate summary stats:", e)


    print("\n✅ Audit complete!")

# Example usage
if __name__ == "__main__":
    file_path = "data/sales.json"   # Change path to your file
    data_audit(file_path)
