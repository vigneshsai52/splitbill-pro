from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

# User schemas
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    name: str

    class Config:
        from_attributes = True


# Group schemas
class GroupCreate(BaseModel):
    name: str
    description: Optional[str] = None
    member_emails: List[str]

class GroupResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    created_at: datetime
    members: List[UserResponse]

    class Config:
        from_attributes = True


# Expense schemas
class ExpenseSplitCreate(BaseModel):
    user_id: int
    amount_owed: float

class ExpenseCreate(BaseModel):
    description: str
    amount: float
    paid_by_id: int
    splits: List[ExpenseSplitCreate]

class ExpenseResponse(BaseModel):
    id: int
    description: str
    amount: float
    paid_by_id: int
    created_at: datetime

    class Config:
        from_attributes = True


# Balance schema
class BalanceResponse(BaseModel):
    user_id: int
    user_name: str
    amount: float