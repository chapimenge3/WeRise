from typing import Optional, Union

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import BaseModel

from .base import Base


class User(Base):
    __tablename__ = "users"

    first_name: Mapped[str] = mapped_column(String(255))
    telegram_id: Mapped[str] = mapped_column(String(255), unique=True, index=True)

    # Opional fields
    last_name: Mapped[Optional[str]] = mapped_column(String(255))
    username: Mapped[Optional[str]] = mapped_column(
        String(255)
    )
    email: Mapped[Optional[str]] = mapped_column(String(255))

    is_admin: Mapped[bool] = mapped_column(default=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    is_verified: Mapped[bool] = mapped_column(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"<User: {self.first_name} {self.last_name}>"


class UserSchema(BaseModel):
    first_name: str
    telegram_id: Union[str, int]
    last_name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    is_admin: bool = False
    is_active: bool = True
    is_verified: bool = False

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def from_orm(cls, user: User):
        return cls(
            first_name=user.first_name,
            telegram_id=user.telegram_id,
            last_name=user.last_name,
            username=user.username,
            email=user.email,
            is_admin=user.is_admin,
            is_active=user.is_active,
            is_verified=user.is_verified,
        )
