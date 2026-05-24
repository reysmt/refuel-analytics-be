from __future__ import annotations

from decimal import Decimal
from typing import Optional
from datetime import datetime

from sqlalchemy import String, Numeric, TIMESTAMP
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column


from app.models.base import Base


# an example mapping using the base
class Rig(Base):
    __tablename__ = "rig"
    __table_args__ = {"schema": "app"}  # importante!

    rig_id: Mapped[Decimal] = mapped_column(Numeric(24), primary_key=True)

    manager: Mapped[Optional[str]] = mapped_column(String(255))
    name: Mapped[Optional[str]] = mapped_column("name", String(255))
    address: Mapped[Optional[str]] = mapped_column(String(255))
    municipality: Mapped[Optional[str]] = mapped_column(String(255))
    province: Mapped[Optional[str]] = mapped_column(String(2))

    latitude: Mapped[Optional[Numeric]] = mapped_column(Numeric)
    longitude: Mapped[Optional[Numeric]] = mapped_column(Numeric)

    add_date: Mapped[Optional[datetime]] = mapped_column(TIMESTAMP(timezone=True))
    mod_date: Mapped[Optional[datetime]] = mapped_column(TIMESTAMP(timezone=True))

    rig_type: Mapped[Optional[str]] = mapped_column(String(255))
    flag: Mapped[Optional[str]] = mapped_column(String(255))

    rig_price: Mapped[Optional[list["RigPrice"]]] = relationship("RigPrice", back_populates="rig")
    rig_price_history: Mapped[Optional[list["RigPriceHistory"]]] = relationship("RigPriceHistory", back_populates="rig")

