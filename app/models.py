from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from .database import Base
from datetime import datetime
class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, index=True)
    amount = Column(Float)
    category = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)