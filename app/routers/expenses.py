from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import csv
import io
from fastapi.responses import StreamingResponse
from app import models, schemas, auth, database

router = APIRouter()

@router.post("/", response_model=schemas.ExpenseResponse)
def create_expense(
    expense: schemas.ExpenseCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    group_id = expense.group_id
    
    group = db.query(models.Group).filter(models.Group.id == group_id).first()
    if not group or current_user not in group.members:
        raise HTTPException(status_code=404, detail="Group not found")

    db_expense = models.Expense(
        description=expense.description,
        amount=expense.amount,
        paid_by_id=expense.paid_by_id,
        group_id=group_id,
        category=expense.category or "Other"
    )
    db.add(db_expense)
    db.flush()

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

    balances = {}
    for member in group.members:
        balances[member.id] = {"name": member.name, "amount": 0.0}

    for expense in group.expenses:
        balances[expense.paid_by_id]["amount"] += expense.amount
        for split in expense.splits:
            balances[split.user_id]["amount"] -= split.amount_owed

    return balances

@router.get("/export/{group_id}")
def export_expenses_csv(
    group_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    group = db.query(models.Group).filter(models.Group.id == group_id).first()
    if not group or current_user not in group.members:
        raise HTTPException(status_code=404, detail="Group not found")

    output = io.StringIO()
    writer = csv.writer(output)
    
    # Header
    writer.writerow(["Description", "Amount", "Category", "Paid By", "Date"])
    
    # Data
    for expense in group.expenses:
        payer = expense.paid_by.name if expense.paid_by else "Unknown"
        writer.writerow([
            expense.description,
            expense.amount,
            expense.category or "Other",
            payer,
            expense.created_at.strftime("%Y-%m-%d")
        ])
    
    output.seek(0)
    
    return StreamingResponse(
        io.BytesIO(output.getvalue().encode()),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=expenses_group_{group_id}.csv"}
    )