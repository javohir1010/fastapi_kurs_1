from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import uvicorn

from items_views import router as items_router
from users.views import router as users_router

app = FastAPI()

app.include_router(items_router)
app.include_router(users_router)





@app.get("/")
def hello_world():
    return {"message": "Hello world"}


@app.get("/hello")
async def hello(name: str = "World"):
    name = name.strip().capitalize()
    return {"message": f"Hello {name}"}





if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
