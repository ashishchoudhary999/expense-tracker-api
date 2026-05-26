from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas, crud

router = APIRouter()


@router.post("/expense")
def create_expense(
    expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db)
):

    return crud.create_expense(db, expense)


@router.get("/expenses")
def get_expenses(db: Session = Depends(get_db)):

    return crud.get_expenses(db)


@router.get("/expense/{expense_id}")
def get_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):

    expense = crud.get_expense(db, expense_id)

    if expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return expense


@router.put("/expense/{expense_id}")
def update_expense(
    expense_id: int,
    updated_expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db)
):

    expense = crud.get_expense(db, expense_id)

    if expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return crud.update_expense(
        db,
        expense_id,
        updated_expense
    )


@router.delete("/expense/{expense_id}")
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):

    expense = crud.get_expense(db, expense_id)

    if expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return crud.delete_expense(db, expense_id)