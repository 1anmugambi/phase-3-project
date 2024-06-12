from models import Base, engine
from models.location import Location

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Database and tables created.")
