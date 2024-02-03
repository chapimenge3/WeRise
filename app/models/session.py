
from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Session(Base):
    __tablename__ = "sessions"

    telegram_id: Mapped[str] = mapped_column(String(255))
    token: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    data: Mapped[Optional[str]] = mapped_column(String(255))

    def __str__(self):
        return f"{self.telegram_id}"

    def __repr__(self):
        return f"<Session: {self.telegram_id}>"
