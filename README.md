# Expense Tracker API

A backend Expense Tracker API built using FastAPI, SQLAlchemy, and SQLite.

This project allows users to:
- Create expenses
- View all expenses
- View a single expense
- Update expenses
- Delete expenses

The project follows modular backend architecture using:
- Routes layer
- CRUD layer
- Models
- Schemas

---

# Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

---

# Project Structure

```bash
app/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
│
└── routes/
    ├── __init__.py
    └── expense.py