from sqlalchemy import Integer, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base

class CarPart(Base):

    __tablename__ = "car_parts"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key = True,
        autoincrement= True
    )

    car_name: Mapped[str] = mapped_column(String(100), nullable = False)

    car_model: Mapped[str] = mapped_column(String(150), nullable=False)

    fuel_type: Mapped[str] = mapped_column(String(30), nullable=False)

    manufacturing_year: Mapped[int] = mapped_column(Integer, nullable=False)

    car_part: Mapped[str] = mapped_column(String(150), nullable=False)

    part_cost_inr: Mapped[int] = mapped_column(Integer, nullable=False)

    fitting_installation_charges_inr: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    fixing_repair_charges_inr: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    labour_cost_per_hr_inr: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    approx_fixing_time_hrs: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    def __repr__(self):
        return (
            f"carPart(id={self.id}), "
            f"car={self.car_name}, "
            f"model={self.car_model}, "
            f"part={self.car_part}"
        )