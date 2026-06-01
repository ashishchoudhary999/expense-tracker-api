from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. database import get_db
from .. import schemas, crud
from ..auth import get_current_user
from ..models import User
from typing import List

router = APIRouter()


@router.post("/expense")
def create_expense(
    expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return crud.create_expense(db, expense, current_user)


@router.get("/expenses")
def get_expenses(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return crud.get_expenses(db, current_user)


@router.get("/expense/{expense_id}")
def get_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):


    expense = crud.get_expense(db, expense_id, current_user)

    if expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return expense


@router.get("/expenses/summary/category",
             response_model=List[schemas.CategorySummary])
def category_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    crud.get_category_summary(db,current_user)

    return crud.get_category_summary(db,current_user)

@router.get("/expenses/summary/monthly",
            response_model=List[schemas.MonthlySummary])
def monthly_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user) 
):
    return crud.get_monthly_summary(db, current_user)


@router.put("/expense/{expense_id}")
def update_expense(
    expense_id: int,
    updated_expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    expense = crud.get_expense(db, expense_id, current_user)

    if expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return crud.update_expense(
        db,
        expense_id,
        updated_expense,
        current_user
    )


@router.delete("/expense/{expense_id}")
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    expense = crud.get_expense(db, expense_id, current_user)

    if expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return crud.delete_expense(db, expense_id, current_user)