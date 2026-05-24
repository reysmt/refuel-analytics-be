from __future__ import annotations

from decimal import Decimal
from typing import Optional
from datetime import datetime

from sqlalchemy import String, Numeric, TIMESTAMP, ForeignKey, Float, Boolean
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.rig import Rig
from app.models.rigfueltype import RigFuelType

from app.models.base import Base


# an example mapping using the base
class RigPrice(Base):
    __tablename__ = "rig_price"
    __table_args__ = {"schema": "app"}

    price_id: Mapped[Decimal] = mapped_column(
        Numeric(24),
        primary_key=True
    )

    rig_id: Mapped[Decimal] = mapped_column(
        Numeric(24),
        ForeignKey("app.rig.rig_id")
    )

    rig_fuel_type_id: Mapped[Decimal] = mapped_column(
        Numeric(24),
        ForeignKey("app.rig_fuel_type.rig_fuel_type_id")
    )

    comu_date: Mapped[Optional[datetime]] = mapped_column(
        TIMESTAMP(timezone=True)
    )

    add_date: Mapped[Optional[datetime]] = mapped_column(
        TIMESTAMP(timezone=True)
    )

    mod_date: Mapped[Optional[datetime]] = mapped_column(
        TIMESTAMP(timezone=True)
    )

    price: Mapped[Optional[float]] = mapped_column(Float)
    is_self: Mapped[Optional[bool]] = mapped_column(Boolean)

    # 🔗 RELAZIONI
    rig: Mapped[Optional[Rig]] = relationship("Rig", back_populates="rig_price")
    rig_fuel_type: Mapped[Optional[list["RigFuelType"]]] = relationship("RigFuelType", back_populates="rig_price")