from app.data.loader import load_csv
from app.data.validator import validate_data

def main():

    print("\nLoading CSV...")

    df = load_csv()

    print("\nDataset Shape:")
    print(df.shape)

    print("\nDataset Information:")
    print(df.info())

    print("\nFirst 5 records:")
    print(df.head())

    print("\nValidating Dataset...")

    validate_data(df)

    print("\nDuplicate Records:")
    print(df.duplicated().sum())

    print("\nDataset Summary:")
    print(df.describe())


if __name__ == "__main__":
    main()