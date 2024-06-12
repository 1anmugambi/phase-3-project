from lib.base import Base  # Ensure the correct import of Base
from sqlalchemy import Column, Integer, String

class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    latitude = Column(String)  # Ensure latitude column is defined
    longitude = Column(String)  # Ensure longitude column is defined

    def __repr__(self):
        return f"<Location(id={self.id}, name={self.name}, latitude={self.latitude}, longitude={self.longitude})>"
