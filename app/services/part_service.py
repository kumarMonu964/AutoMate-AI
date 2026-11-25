from app.database.repository import search_parts_for_vehicle


def find_part_and_check_repair(
    db,
    car_name: str,
    car_model: str,
    manufacturing_year: int,
    fuel_type: str,
    part_keyword: str
):
    """
    Search for a vehicle part and determine
    whether repair or replacement is available.
    """

    parts = search_parts_for_vehicle(
        db=db,
        car_name=car_name,
        car_model=car_model,
        manufacturing_year=manufacturing_year,
        fuel_type=fuel_type,
        part_keyword=part_keyword
    )

    if not parts:
        return {
            "status": "not_found",
            "message": "No matching part found in our database."
        }

    results = []

    for part in parts:

        repair_available = (
            part.fixing_repair_charges_inr is not None
        )

        results.append({
            "part_id": part.id,
            "part_name": part.car_part,
            "part_cost": part.part_cost_inr,
            "installation_charges": (
                part.fitting_installation_charges_inr
            ),
            "repair_charges": (
                part.fixing_repair_charges_inr
            ),
            "repair_available": repair_available,
            "replacement_available": True
        })

    return {
        "status": "success",
        "total_matches": len(results),
        "parts": results
    }