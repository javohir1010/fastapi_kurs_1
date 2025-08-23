from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import uvicorn

from items_views import router as items_router

app = FastAPI()

app.include_router(items_router)


class CreateUser(BaseModel):
    email: EmailStr


@app.get("/")
def hello_world():
    return {"message": "Hello world"}


@app.get("/hello")
async def hello(name: str = "World"):
    name = name.strip().capitalize()
    return {"message": f"Hello {name}"}


@app.post("/email")
async def email_validator(user: CreateUser):
    return {"message": "OK", "email": user.email}


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
