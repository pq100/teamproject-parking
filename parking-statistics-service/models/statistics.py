from datetime import datetime
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class VisitorStats(Base):
    __tablename__ = 'visitor_stats'

    sno = Column(Integer, primary_key=True, autoincrement=True, index=True)
    carnum = Column(String(10), nullable=False)
    month = Column(String(10), nullable=False)
    visitor_count = Column(Integer, nullable=False)


class PaymentStats(Base):
    __tablename__ = 'payment_stats'

    sno = Column(Integer, primary_key=True, autoincrement=True, index=True)
    month = Column(String(10), nullable=False)
    total_fee = Column(Float, nullable=False)
