import pandas as pd

from sqlalchemy import func

from app.data.loader import load_csv
from app.data.validator import validate_data

from app.database.connection import Base, engine, SessionLocal
from app.database.models import CarPart


def transform_records(df: pd.DataFrame) -> list[dict]:

    records = df.to_dict(orient="records")

    # Convert Pandas NaN values into Python None
    for record in records:
        for column, value in record.items():
            if pd.isna(value):
                record[column] = None

    return records


def ingest_data():

    print("\nLoading CSV...")

    df = load_csv()

    print(f"Loaded {len(df)} records.")

    print("\nValidating data...")

    validate_data(df)

    print("\nTransforming records...")

    records = transform_records(df)

    # Mapping CSV column names to database column names
    transformed_records = []

    for record in records:

        transformed_records.append({

            "car_name": record["Car_Name"],

            "car_model": record["Car_Model"],

            "fuel_type": record["Fuel_Type"],

            "manufacturing_year": record["Manufacturing_Year"],

            "car_part": record["Car_Part"],

            "part_cost_inr": record["Part_Cost_INR"],

            "fitting_installation_charges_inr":
                record["Fitting_Installation_Charges_INR"],

            "fixing_repair_charges_inr":
                record["Fixing_Repair_Charges_INR"],

            "labour_cost_per_hr_inr":
                record["Labour_Cost_Per_Hr_INR"],

            "approx_fixing_time_hrs":
                record["Approx_Fixing_Time_Hrs"]

        })

    print(f"Transformed {len(transformed_records)} records.")

    print("\nInserting records into SQLite...")

    Base.metadata.create_all(bind=engine)

    with SessionLocal() as session:

        try:

            # Replace existing imported records
            session.query(CarPart).delete()

            session.add_all([
                CarPart(**record)
                for record in transformed_records
            ])

            session.commit()

            print("\nData ingestion successful!")

            total_records = session.scalar(
                func.count(CarPart.id)
            )

            print(f"Records inserted: {total_records}")

        except Exception:

            session.rollback()

            raise


if __name__ == "__main__":
    ingest_data()