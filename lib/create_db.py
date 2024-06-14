from lib.models import Base, engine
from lib.models.location import Location

# Create all tables in the database
Base.metadata.create_all(engine)
print("Database tables created.")
