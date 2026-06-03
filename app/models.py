from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

# Association table for group members
group_members = Table(
    'group_members',
    Base.metadata,
    Column('group_id', Integer, ForeignKey('groups.id')),
    Column('user_id', Integer, ForeignKey('users.id'))
)

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    hashed_password = Column(String)
    reset_token = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    groups = relationship("Group", secondary=group_members, back_populates="members")
    expenses_paid = relationship("Expense", foreign_keys="Expense.paid_by_id", back_populates="paid_by")
    splits = relationship("ExpenseSplit", back_populates="user")

class Group(Base):
    __tablename__ = "groups"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String, nullable=True)
    created_by_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    members = relationship("User", secondary=group_members, back_populates="groups")
    expenses = relationship("Expense", back_populates="group", cascade="all, delete-orphan")
    created_by = relationship("User", foreign_keys=[created_by_id])

class Expense(Base):
    __tablename__ = "expenses"
    
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    amount = Column(Float)
    paid_by_id = Column(Integer, ForeignKey("users.id"))
    group_id = Column(Integer, ForeignKey("groups.id"))
    category = Column(String, default="Other")
    created_at = Column(DateTime, default=datetime.utcnow)
    
    paid_by = relationship("User", foreign_keys=[paid_by_id])
    group = relationship("Group", back_populates="expenses")
    splits = relationship("ExpenseSplit", back_populates="expense", cascade="all, delete-orphan")

class ExpenseSplit(Base):
    __tablename__ = "expense_splits"
    
    id = Column(Integer, primary_key=True, index=True)
    expense_id = Column(Integer, ForeignKey("expenses.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    amount_owed = Column(Float)
    
    expense = relationship("Expense", back_populates="splits")
    user = relationship("User", back_populates="splits")