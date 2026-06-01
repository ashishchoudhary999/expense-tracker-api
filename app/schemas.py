from pydantic import BaseModel

class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category:str

class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(UserCreate):
    pass

class UserResponse(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True

class CategorySummary(BaseModel):
    category: str
    total: float

class MonthlySummary(BaseModel):
    month: str
    total: float

class ExpenseStats(BaseModel):
    highest_expense: float
    average_expense: float
    most_used_category: str
    total_count: int