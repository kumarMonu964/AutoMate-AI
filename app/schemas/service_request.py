from typing import Literal

from pydantic import BaseModel, Field


class VehicleDetails(BaseModel):

    car_name: str | None = Field(
        default=None,
        description="Car manufacturer, such as Hyundai or Maruti."
    )

    car_model: str | None = Field(
        default=None,
        description="Specific car model or variant."
    )

    manufacturing_year: int | None = Field(
        default=None,
        description="Vehicle manufacturing year."
    )

    fuel_type: str | None = Field(
        default=None,
        description="Fuel type such as Petrol, Diesel, CNG, Hybrid or Electric."
    )


class ServiceRequest(BaseModel):

    vehicle: VehicleDetails

    part_name: str | None = Field(
        default=None,
        description="The specific car part mentioned by the customer."
    )

    operation: Literal[
        "repair",
        "replacement",
        "comparison",
        "unknown"
    ] = "unknown"

    requested_information: Literal[
        "cost",
        "time",
        "repair_availability",
        "general_information",
        "unknown"
    ] = "unknown"