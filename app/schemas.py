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

