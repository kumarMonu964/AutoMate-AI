from pprint import pprint

from app.services.extraction_service import extract_service_request
from app.services.validation_service import find_missing_information


def main():

    test_messages = [

        "My 2021 Hyundai Creta SX Petrol needs a rear shock absorber replacement. How much will it cost?",

        "How much will my shock absorber cost?",

        "I have a Maruti Swift Diesel. How long does brake pad replacement take?",

        "My suspension is making noise."
    ]

    for message in test_messages:

        print("\n" + "=" * 60)
        print("CUSTOMER:", message)

        result = extract_service_request(message)

        print("\nEXTRACTED INFORMATION:")
        pprint(result.model_dump())

        missing = find_missing_information(result)

        print("\nMISSING INFORMATION:")
        print(missing)


if __name__ == "__main__":
    main()