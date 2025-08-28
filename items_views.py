from typing import Annotated
from fastapi import APIRouter, Path

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("/")
async def list_items():
    return {"item1", "item2"}


@router.get("/latest/")
async def latest_item():
    return {"id": 0, "name": "latest"}


@router.get("/{item_id}/")
async def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {"item": {"id": item_id}}
