from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from .database import engine, Base
from .routes import expense, user
from . import models

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(expense.router)
app.include_router(user.router)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title="Expense Tracker API",
        version="1.0.0",
        routes=app.routes,
    )
    
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"BearerAuth": []}]
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi