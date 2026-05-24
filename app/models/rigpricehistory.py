from __future__ import annotations

from decimal import Decimal
from typing import Optional
from datetime import datetime

from sqlalchemy import String, Numeric, TIMESTAMP, ForeignKey, Float, Boolean
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from app.models.base import Base

class RigPriceHistory(Base):
    __tablename__ = "rig_price_history"
    __table_args__ = {"schema": "app"}

    price_history_id: Mapped[Decimal] = mapped_column(Numeric(24), primary_key=True)
    rig_id: Mapped[Decimal] = mapped_column(Numeric(24), ForeignKey("app.rig.rig_id"), primary_key=True)
    rig_fuel_type_id: Mapped[Decimal] = mapped_column(Numeric(24), ForeignKey("app.rig_fuel_type.rig_fuel_type_id"), nullable=True)
    comu_date: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True))
    add_date: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), primary_key=True)
    mod_date: Mapped[Optional[datetime]] = mapped_column(TIMESTAMP(timezone=True))
    price: Mapped[Optional[float]] = mapped_column(Float)
    is_self: Mapped[Optional[bool]] = mapped_column(Boolean)

    # Relationships
    rig: Mapped[Rig] = relationship("Rig", back_populates="rig_price_history")
    rig_fuel_type: Mapped[Optional[RigFuelType]] = relationship("RigFuelType", back_populates="rig_price_history")
