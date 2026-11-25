from app.database.connection import Base, engine
from app.database.models import CarPart

def main():

    print("Creating database tables...")

    Base.metadata.create_all(bind=engine)

    print(f"Database create successfully!")

if __name__ == "__main__":
    main()