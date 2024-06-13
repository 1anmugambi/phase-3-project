from . import Base
from sqlalchemy import Column, Integer, String, Float

class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

    def __repr__(self):
        return f"<Location(id={self.id}, name={self.name}, latitude={self.latitude}, longitude={self.longitude})>"