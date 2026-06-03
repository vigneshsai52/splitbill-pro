import os

# Delete old database so new schema (category column) works
if os.path.exists("splitbill.db"):
    os.remove("splitbill.db")
    print("Deleted old database")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import auth, groups, expenses

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(groups.router, prefix="/groups", tags=["groups"])
app.include_router(expenses.router, prefix="/expenses", tags=["expenses"])

@app.get("/")
@app.head("/")
def root():
    return {"message": "API running"}

@app.get("/health")
@app.head("/health")
def health_check():
    return {"status": "ok"}