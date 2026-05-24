from typing import Optional

from sqlalchemy import String, Numeric, TIMESTAMP, ForeignKey, Float, Boolean, VARCHAR, Column

from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column


from app.models.base import Base


# an example mapping using the base
class RigFuelType(Base):
    __tablename__ = "rig_fuel_type"
    __table_args__ = {"schema": "app"}

    rig_fuel_type_id: Mapped[Numeric] = mapped_column(Numeric,primary_key = True)
    fuel_type: Mapped[VARCHAR] = Column(String(255))

    rig_price: Mapped[Optional[list["RigPrice"]]] = relationship("RigPrice", back_populates="rig_fuel_type")
    rig_price_history: Mapped[Optional[list["RigPriceHistory"]]] = relationship("RigPriceHistory", back_populates="rig_fuel_type")
