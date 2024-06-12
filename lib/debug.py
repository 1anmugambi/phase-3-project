from lib.models import Base, engine
from lib.models.location import Location

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Database and tables created.")
