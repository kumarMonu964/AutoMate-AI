from app.database.connection import SessionLocal
from app.database.repository import (
    find_vehicle_options,
    get_parts_for_vehicle
)


def main():

    with SessionLocal() as db:

        print("\nSearching for vehicle options...")

        vehicles = find_vehicle_options(
            db=db,
            car_name="Hyundai",
            car_model="Creta SX"
        )

        for vehicle in vehicles:
            print(vehicle)

        print("\nFetching parts for a specific vehicle...")

        parts = get_parts_for_vehicle(
            db=db,
            car_name="Hyundai",
            car_model="Creta SX",
            manufacturing_year=2021,
            fuel_type="Petrol"
        )

        print(f"\nTotal parts found: {len(parts)}")

        for part in parts:
            print(
                f"{part.car_part} | "
                f"Part Cost: ₹{part.part_cost_inr} | "
                f"Installation: ₹{part.fitting_installation_charges_inr} | "
                f"Repair: {part.fixing_repair_charges_inr}"
            )


if __name__ == "__main__":
    main()