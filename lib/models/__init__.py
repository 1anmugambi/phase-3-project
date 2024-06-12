# lib/models/__init__.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .location import Location, Base

engine = create_engine('sqlite:///locations.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
