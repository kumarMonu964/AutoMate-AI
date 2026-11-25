from sqlalchemy import select, func

from app.database.connection import SessionLocal
from app.database.models import CarPart

def main():

    with SessionLocal() as session:

        # Total number of records
        total = session.scalar(
            select(func.count()).select_from(CarPart)

        )

        print(f"\nTotal records: {total}")

        # Fetch first five records
        statement = select(CarPart).limit(5)

        results = session.scalars(statement).all()

        for record in results:

            print(
                f"ID: {record.id} | "
                f"Car: {record.car_name} | "
                f"Model: {record.car_model} | "
                f"Part: {record.car_part} | "
                f"Price: ₹{record.part_cost_inr}"
            
            )

if __name__ == "__main__":
    main()

