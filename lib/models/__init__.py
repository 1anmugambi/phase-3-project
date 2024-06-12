from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.base import Base  # Ensure this import matches the new base.py
from lib.models.location import Location

DATABASE_URL = "sqlite:///locations.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
