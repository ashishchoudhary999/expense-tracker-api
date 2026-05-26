from fastapi import FastAPI, Depends, HTTPException
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

@app.get("/expense/{expense_id}")
def get_expense(
    expense_id: int,
    db:Session = Depends(get_db)
):
    
    expense = db.query(models.Expense).filter(
        models.Expense.id == expense_id
    ).first()

    if expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return expense


@app.put("/expense/{expense_id}")
def update_expense(
    expense_id:int,
    updated_expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db)
):
    expense = db.query(models.Expense).filter(
        models.Expense.id == expense_id
    ).first()

    if expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )
    
    expense.title = updated_expense.title
    expense.amount = updated_expense.amount
    expense.category = updated_expense.category

    db.commit()
    db.refresh(expense)

    return expense