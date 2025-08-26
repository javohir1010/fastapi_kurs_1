from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import Product, ProductCreate, ProductUpdatePartial, ProductUpdate
from core.models import db_helper
from .dependencies import product_by_id


router = APIRouter(
    tags=["Товары"],
)


@router.get(
    path="/",
    response_model=list[Product],
)
async def get_products(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_products(session=session)


@router.post(
    path="/",
    response_model=Product,
    status_code=status.HTTP_201_CREATED,
)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_product(session=session, product_in=product_in)


@router.get(
    path="/{product_id}/",
    response_model=Product,
)
async def get_product_by_id(product: Product = Depends(product_by_id)):
    return product


@router.put(
    path="/{product_id}/",
    response_model=Product,
)
async def update_product(
    product_udpate: ProductUpdate,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_udpate,
    )


@router.patch(
    path="/{product_id}/",
    response_model=Product,
)
async def update_product_partial(
    product_update: ProductUpdatePartial,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update,
        partial=True,
    )


@router.delete(
    path="/{product_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_product(
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_product(
        session=session,
        product=product,
    )
