from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.database import get_db
from app.routers.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.GroupResponse)
def create_group(group: schemas.GroupCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    db_group = models.Group(name=group.name, description=group.description, created_by_id=current_user.id)
    db_group.members.append(current_user)
    for email in group.member_emails:
        member = db.query(models.User).filter(models.User.email == email).first()
        if member and member not in db_group.members:
            db_group.members.append(member)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

@router.get("/", response_model=List[schemas.GroupResponse])
def get_groups(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return current_user.groups

@router.delete("/{group_id}")
def delete_group(group_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    group = db.query(models.Group).filter(models.Group.id == group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    if group.created_by_id != current_user.id:
        raise HTTPException(status_code=403, detail="Only creator can delete")
    db.delete(group)
    db.commit()
    return {"message": "Group deleted"}