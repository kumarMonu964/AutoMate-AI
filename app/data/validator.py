import pandas as pd

EXPECTED_COLUMNS = [
    "Car_Name",
    "Car_Model",
    "Fuel_Type",
    "Manufacturing_Year",
    "Car_Part",
    "Part_Cost_INR",
    "Fitting_Installation_Charges_INR",
    "Fixing_Repair_Charges_INR",
    "Labour_Cost_Per_Hr_INR",
    "Approx_Fixing_Time_Hrs",
]


NUMERIC_COLUMNS = [
    "Manufacturing_Year",
    "Part_Cost_INR",
    "Fitting_Installation_Charges_INR",
    "Fixing_Repair_Charges_INR",
    "Labour_Cost_Per_Hr_INR",
    "Approx_Fixing_Time_Hrs",
]

def validate_columns(df: pd.DataFrame) -> None:

    missing_columns = set(EXPECTED_COLUMNS) - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )


def validate_data_types(df: pd.DataFrame) -> None:

    for column in NUMERIC_COLUMNS:

        if not pd.api.types.is_numeric_dtype(df[column]):
            raise TypeError(
                f"{column} must contain numeric values."
            )


def validate_missing_values(df: pd.DataFrame) -> None:

    missing_values = df.isnull().sum()

    if missing_values.sum() > 0:
        print("Warning: Missing values detected:")
        print(missing_values[missing_values > 0])


def validate_data(df: pd.DataFrame) -> None:

    validate_columns(df)

    validate_data_types(df)