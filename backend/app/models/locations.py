import enum

from sqlalchemy import Column, Date, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.app.models.base import Base


class Location(Base):
    __tablename__ = "dim_locations"

    location_id = Column(Integer, primary_key=True, autoincrement=True)
    market = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    province = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
