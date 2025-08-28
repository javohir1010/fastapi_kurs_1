from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import declared_attr, mapped_column, Mapped, relationship

if TYPE_CHECKING:
    from .user import User


class UserRelationMixin:
    _user_id_unique: bool = False
    _user_back_populates: str | None = None
    _user_id_nullable: bool = False

    @declared_attr
    def user_id(cls) -> Mapped[int]:
        return mapped_column(
            Integer,
            ForeignKey("users.id"),
            unique=cls._user_id_unique,
            nullable=cls._user_id_nullable,
        )

    @declared_attr
    def user(cls) -> Mapped["User"]:
        return relationship(
            argument="User",
            back_populates=cls._user_back_populates,
        )
