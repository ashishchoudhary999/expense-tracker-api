from sqlalchemy.orm import Session
from app import models, schemas


def create_expense(
    db: Session,
    expense: schemas.ExpenseCreate
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


def get_expenses(db: Session):

    return db.query(models.Expense).all()


def get_expense(
    db: Session,
    expense_id: int
):

    return db.query(models.Expense).filter(
        models.Expense.id == expense_id
    ).first()


def update_expense(
    db: Session,
    expense_id: int,
    updated_expense: schemas.ExpenseCreate
):

    expense = db.query(models.Expense).filter(
        models.Expense.id == expense_id
    ).first()

    expense.title = updated_expense.title
    expense.amount = updated_expense.amount
    expense.category = updated_expense.category

    db.commit()
    db.refresh(expense)

    return expense


def delete_expense(
    db: Session,
    expense_id: int
):

    expense = db.query(models.Expense).filter(
        models.Expense.id == expense_id
    ).first()

    db.delete(expense)
    db.commit()

    return {"message": "Expense deleted successfully"}