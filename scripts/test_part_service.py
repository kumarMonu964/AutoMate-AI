from pprint import pprint

from app.database.connection import SessionLocal
from app.services.part_service import find_part_and_check_repair


def main():

    with SessionLocal() as db:

        result = find_part_and_check_repair(
            db=db,
            car_name="Hyundai",
            car_model="Creta SX",
            manufacturing_year=2021,
            fuel_type="Petrol",
            part_keyword="Shock Absorber"
        )

        pprint(result)


if __name__ == "__main__":
    main()