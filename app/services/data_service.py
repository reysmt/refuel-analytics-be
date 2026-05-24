from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.core.configsql import engine
from app.models.rig import Rig
from app.models.rigprice import RigPrice
from app.models.rigpricehistory import RigPriceHistory

def get_rig_price_history(rig_id: int):
    """Get price history for a specific rig"""
    with Session(engine) as session:
        stmt = select(RigPriceHistory).where(RigPriceHistory.rig_id == rig_id)
        result = session.execute(stmt)
        return result.scalars().all()

def get_all_rigs():
    """Get all rigs"""
    with Session(engine) as session:
        stmt = select(Rig)
        result = session.execute(stmt)
        return result.scalars().all()

def get_rig_price(rig_id: int):
    """Get price for a specific rig"""
    with Session(engine) as session:
        stmt = select(RigPrice).where(RigPrice.rig_id == rig_id)
        result = session.execute(stmt)
        return result.scalars().all()

def get_rig_pricehistory_all():
    """Get all price history """
    with Session(engine) as session:
        stmt = select(RigPriceHistory)
        result = session.execute(stmt)
        return result.scalars().all()

def test():
    with Session(engine) as session:
        stmt = select(RigPriceHistory).where(RigPriceHistory.rig_id ==  62144)
        result = session.execute(stmt).scalars().all()
        for row in result:
            print(row.rig)
