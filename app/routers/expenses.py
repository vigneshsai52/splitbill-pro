from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas, auth, database

router = APIRouter()

@router.post("/", response_model=schemas.ExpenseResponse)
def create_expense(
    expense: schemas.ExpenseCreate,
    group_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    # Verify group exists and user is member
    group = db.query(models.Group).filter(models.Group.id == group_id).first()
    if not group or current_user not in group.members:
        raise HTTPException(status_code=404, detail="Group not found")

    # Create expense
    db_expense = models.Expense(
        description=expense.description,
        amount=expense.amount,
        paid_by_id=expense.paid_by_id,
        group_id=group_id
    )
    db.add(db_expense)
    db.flush()  # Get expense ID

    # Create splits
    for split in expense.splits:
        db_split = models.ExpenseSplit(
            expense_id=db_expense.id,
            user_id=split.user_id,
            amount_owed=split.amount_owed
        )
        db.add(db_split)

    db.commit()
    db.refresh(db_expense)
    return db_expense

@router.get("/group/{group_id}", response_model=List[schemas.ExpenseResponse])
def get_group_expenses(
    group_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    group = db.query(models.Group).filter(models.Group.id == group_id).first()
    if not group or current_user not in group.members:
        raise HTTPException(status_code=404, detail="Group not found")

    return group.expenses

@router.get("/balances/{group_id}")
def get_balances(
    group_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    group = db.query(models.Group).filter(models.Group.id == group_id).first()
    if not group or current_user not in group.members:
        raise HTTPException(status_code=404, detail="Group not found")

    # Calculate balances
    balances = {}
    for member in group.members:
        balances[member.id] = {"name": member.name, "amount": 0.0}

    for expense in group.expenses:
        # Payer is owed money
        balances[expense.paid_by_id]["amount"] += expense.amount

        # Others owe money
        for split in expense.splits:
            balances[split.user_id]["amount"] -= split.amount_owed

    return balances