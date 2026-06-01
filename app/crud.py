from sqlalchemy.orm import Session
from . import models, schemas
from .models import User


def create_expense(
    db: Session,
    expense: schemas.ExpenseCreate,
    current_user: User
):

    new_expense = models.Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category,
        user_id=current_user.id

    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense


def get_expenses(db: Session, current_user: User):
    return db.query(models.Expense).filter(
        models.Expense.user_id == current_user.id
    ).all()


def get_expense(
    db: Session,
    expense_id: int,
    current_user: User
):

    return db.query(models.Expense).filter(
        models.Expense.id == expense_id,
        models.Expense.user_id == current_user.id
    ).first()


def update_expense(
    db: Session,
    expense_id: int,
    updated_expense: schemas.ExpenseCreate,
    current_user: User
):

    expense = db.query(models.Expense).filter(
        models.Expense.id == expense_id,
        models.Expense.user_id == current_user.id
    ).first()

    expense.title = updated_expense.title
    expense.amount = updated_expense.amount
    expense.category = updated_expense.category

    db.commit()
    db.refresh(expense)

    return expense


def delete_expense(
    db: Session,
    expense_id: int,
    current_user: User
):

    expense = db.query(models.Expense).filter(
        models.Expense.id == expense_id,
        models.Expense.user_id == current_user.id
    ).first()

    db.delete(expense)
    db.commit()

    return {"message": "Expense deleted successfully"}