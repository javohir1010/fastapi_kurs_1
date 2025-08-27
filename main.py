from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

from items_views import router as items_router
from users.views import router as users_router
from api_v1 import router as router_v1
from core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    yield
        


app = FastAPI(lifespan=lifespan)

app.include_router(router=router_v1, prefix=settings.api_v1_prefix)
app.include_router(items_router)
app.include_router(users_router)





@app.get("/")
def hello_world():
    return {"message": "Hello world"}


@app.get("/hello/")
async def hello(name: str = "World"):
    name = name.strip().capitalize()
    return {"message": f"Hello {name}"}





if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True,)
