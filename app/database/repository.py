from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models import CarPart


def find_vehicle_options(
    db: Session,
    car_name: str,
    car_model: str
):
    """
    Find available vehicle variants matching the given
    car manufacturer and model.
    """

    statement = (
        select(
            CarPart.car_name,
            CarPart.car_model,
            CarPart.manufacturing_year,
            CarPart.fuel_type
        )
        .where(
            CarPart.car_name.ilike(car_name),
            CarPart.car_model.ilike(car_model)
        )
        .distinct()
        .order_by(
            CarPart.manufacturing_year,
            CarPart.fuel_type
        )
    )

    return db.execute(statement).all()


def get_parts_for_vehicle(
    db: Session,
    car_name: str,
    car_model: str,
    manufacturing_year: int,
    fuel_type: str
):
    """
    Retrieve all available parts for a specific vehicle.
    """

    statement = select(CarPart).where(
        CarPart.car_name.ilike(car_name),
        CarPart.car_model.ilike(car_model),
        CarPart.manufacturing_year == manufacturing_year,
        CarPart.fuel_type.ilike(fuel_type)
    )

    return db.scalars(statement).all()

def search_parts_for_vehicle(
    db: Session,
    car_name: str,
    car_model: str,
    manufacturing_year: int,
    fuel_type: str,
    part_keyword: str
):
    """
    Search for parts belonging to a specific vehicle.
    Supports partial part-name matching.
    """

    statement = select(CarPart).where(
        CarPart.car_name.ilike(car_name),
        CarPart.car_model.ilike(car_model),
        CarPart.manufacturing_year == manufacturing_year,
        CarPart.fuel_type.ilike(fuel_type),
        CarPart.car_part.ilike(f"%{part_keyword}%")
    )

    return db.scalars(statement).all()