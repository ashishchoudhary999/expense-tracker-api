from fastapi import FastAPI

from app.database import engine, Base
from app.routes import expense
from app import models

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(expense.router)