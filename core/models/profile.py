from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import UserRelationMixin


class Profile(UserRelationMixin, Base):
    """
    _user_back_populates = "profile"
    _user_id_unique = True

    first_name: Mapped[str | None] = mapped_column(String(50))
    lastname_name: Mapped[str | None] = mapped_column(String(50))
    bio: Mapped[str | None]
    """

    _user_back_populates = "profile"
    _user_id_unique = True

    first_name: Mapped[str | None] = mapped_column(String(50))
    last_name: Mapped[str | None] = mapped_column(String(50))
    bio: Mapped[str | None]

    def __str__(self):
        return f"{self.__class__.__name__}(id = {self.id}, first_name = {self.first_name!r}, user_id = {self.user_id})"
    
    def __repr__(self):
        return str(self)