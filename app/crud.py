from sqlalchemy.orm import Session
from . import models, schemas
from .models import Expense, User
from sqlalchemy import func, extract
from typing import List
from .schemas import CategorySummary, MonthlySummary, ExpenseStats

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

def get_category_summary(
        db: Session,
        current_user: User
):

    results = db.query(
        Expense.category.label("category"), 
        func.sum(Expense.amount).label("total")
    ).filter(
        Expense.user_id == current_user.id
    ).group_by(
        Expense.category
        ).all()

    return results

def get_monthly_summary(
        db: Session,
        current_user: User
):
    results = db.query(
        extract("year", Expense.created_at).label("year"),
        extract("month", Expense.created_at).label("month"),
        func.sum(Expense.amount).label("total")
    ).filter(
        Expense.user_id == current_user.id
    ).group_by(
        extract("year", Expense.created_at),
        extract("month", Expense.created_at)
    ).all()

    summary = []
    for row in results:
        month_str = f"{int(row.year)}-{int(row.month):02d}"
        summary.append({
            "month": month_str,
            "total": row.total
        })

    return summary


def get_expense_stats(db: Session, current_user: User):
    stats = db.query(
        func.max(Expense.amount).label("highest"),
        func.avg(Expense.amount).label("average"),
        func.count(Expense.id).label("count")
    ).filter(
        Expense.user_id == current_user.id
    ).first()

    top_category = db.query(
    Expense.category,
    func.count(Expense.id).label("cnt")
    ).filter(
        Expense.user_id == current_user.id
    ).group_by(
        Expense.category
    ).order_by(
        func.count(Expense.id).desc()
    ).first()

    most_used = top_category.category if top_category else "None"

    return {
        "highest_expense": stats.highest,
        "average_expense": round(stats.average, 2) if stats.average else 0,
        "most_used_category": most_used,
        "total_count": stats.count
    }