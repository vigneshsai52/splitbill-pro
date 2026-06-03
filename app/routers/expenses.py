from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import csv, io
from fastapi.responses import StreamingResponse
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
        group_id=expense.group_id,
        category=expense.category or "Other"
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

@router.get("/export/{group_id}")
def export_csv(group_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    group = db.query(models.Group).filter(models.Group.id == group_id).first()
    if not group or current_user not in group.members:
        raise HTTPException(status_code=404, detail="Group not found")
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Description", "Amount", "Category", "Paid By", "Date"])
    for e in group.expenses:
        writer.writerow([e.description, e.amount, e.category or "Other", e.paid_by.name if e.paid_by else "Unknown", e.created_at.strftime("%Y-%m-%d")])
    output.seek(0)
    return StreamingResponse(io.BytesIO(output.getvalue().encode()), media_type="text/csv", headers={"Content-Disposition": f"attachment; filename=expenses_{group_id}.csv"})