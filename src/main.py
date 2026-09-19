from src.extract import extract_all

from src.transform import (transform_all , save_processed)

from src.load import load_all

def run_pipeline():
    print("Starting ETL pipeline...")
    print("Step 1: Extract")

    raw_data = extract_all()

    print("Step 2: Transform")

    processed_data = transform_all(raw_data)

    print("Step 3: Save Processed")

    save_processed(processed_data)

    print("Step 4: Load info PostgreSQL")

    load_all(processed_data)

    print("ETL pipeline completed successfuly")

if __name__ == "__main__":
    run_pipeline()