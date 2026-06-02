from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas, auth, database

router = APIRouter()

@router.post("/", response_model=schemas.GroupResponse)
def create_group(
    group: schemas.GroupCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    # Create group
    db_group = models.Group(
        name=group.name,
        description=group.description,
        created_by_id=current_user.id
    )
    db_group.members.append(current_user)

    # Add other members by email
    for email in group.member_emails:
        member = db.query(models.User).filter(models.User.email == email).first()
        if member and member not in db_group.members:
            db_group.members.append(member)

    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

@router.get("/", response_model=List[schemas.GroupResponse])
def get_my_groups(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    return current_user.groups