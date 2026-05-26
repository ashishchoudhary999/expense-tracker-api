from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import engine, Base, get_db
from app import models, schemas

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/expense")
def create_expense(
    expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db)
):
    new_expense = models.Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense

@app.get("/expenses")
def get_expenses(db: Session = Depends(get_db)):
    expenses = db.query(models.Expense).all()

    return expenses