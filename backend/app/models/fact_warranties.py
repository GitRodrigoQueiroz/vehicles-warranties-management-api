import enum

from sqlalchemy import Column, Date, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.app.models.base import Base


class Warranty(Base):
    __tablename__ = "fact_warranties"

    claim_key = Column(Integer, primary_key=True, autoincrement=True)
    vehicle_id = Column(
        Integer, ForeignKey("dim_vehicle.vehicle_id"), nullable=False, unique=True
    )
    repair_date = Column(Date, nullable=False)
    client_comment = Column(String)
    tech_comment = Column(String, nullable=False)
    part_id = Column(Integer, ForeignKey("dim_parts.part_id"), nullable=False)
    classifed_failured = Column(String(50), nullable=False)
    location_id = Column(
        Integer, ForeignKey("dim_locations.location_id"), nullable=False
    )
    purchance_id = Column(
        Integer, ForeignKey("dim_purchances.purchance_id"), nullable=False
    )

    vehicle = relationship("Vehicle")
    part = relationship("Part")
    location = relationship("Location")
    purchance = relationship("Purchase")
