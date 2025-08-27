from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .user import User


class Profile(Base):
    first_name: Mapped[str | None] = mapped_column(String(50))
    lastname_name: Mapped[str | None] = mapped_column(String(50))
    bio: Mapped[str | None]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), unique=True)
    
    user: Mapped["User"] = relationship(back_populates="profile")
