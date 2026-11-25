def find_missing_information(request):

    missing = []

    vehicle = request.vehicle

    if not vehicle.car_name:
        missing.append("car_name")

    if not vehicle.car_model:
        missing.append("car_model")

    if not vehicle.manufacturing_year:
        missing.append("manufacturing_year")

    if not vehicle.fuel_type:
        missing.append("fuel_type")

    if not request.part_name:
        missing.append("part_name")

    if request.operation == "unknown":
        missing.append("operation")

    return missing