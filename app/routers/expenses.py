from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.database import get_db
from app.routers.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.ExpenseResponse)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    group = db.query(models.Group).filter(models.Group.id == expense.group_id).first()
    if not group or current_user not in group.members:
        raise HTTPException(status_code=404, detail="Group not found")
    db_expense = models.Expense(
        description=expense.description,
        amount=expense.amount,
        paid_by_id=expense.paid_by_id,
        group_id=expense.group_id
    )
    db.add(db_expense)
    db.flush()
    for split in expense.splits:
        db.add(models.ExpenseSplit(expense_id=db_expense.id, user_id=split.user_id, amount_owed=split.amount_owed))
    db.commit()
    db.refresh(db_expense)
    return db_expense

@router.get("/group/{group_id}", response_model=List[schemas.ExpenseResponse])
def get_expenses(group_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    group = db.query(models.Group).filter(models.Group.id == group_id).first()
    if not group or current_user not in group.members:
        raise HTTPException(status_code=404, detail="Group not found")
    return group.expenses

@router.get("/balances/{group_id}")
def get_balances(group_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    group = db.query(models.Group).filter(models.Group.id == group_id).first()
    if not group or current_user not in group.members:
        raise HTTPException(status_code=404, detail="Group not found")
    balances = {}
    for m in group.members:
        balances[m.id] = {"name": m.name, "amount": 0.0}
    for e in group.expenses:
        balances[e.paid_by_id]["amount"] += e.amount
        for s in e.splits:
            balances[s.user_id]["amount"] -= s.amount_owed
    return balances