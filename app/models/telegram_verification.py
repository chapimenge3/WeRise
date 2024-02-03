import datetime
import enum
from typing import Dict, Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, Column, Enum
from sqlalchemy.dialects.postgresql import JSON

from pydantic import BaseModel

from app.models.base import Base
from app.models.user import User


class StatusEnum(enum.Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"


class TelegramVerification(Base):
    __tablename__ = "telegram_verifications"

    # user = ForeignKeyField(User, backref="telegram_verifications")
    user: Mapped[User] = relationship(backref="telegram_verifications")

    telegram_id: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    phone_number: Mapped[Optional[str]] = mapped_column(String(255))
    passport_data: Mapped[Optional[dict]] = mapped_column(JSON())
    personal_details: Mapped[Optional[dict]] = mapped_column(JSON())
    driver_license: Mapped[Optional[dict]] = mapped_column(JSON())
    identity_card: Mapped[Optional[dict]] = mapped_column(JSON())
    utility_bill: Mapped[Optional[dict]] = mapped_column(JSON())
    bank_statement: Mapped[Optional[dict]] = mapped_column(JSON())
    address: Mapped[Optional[dict]] = mapped_column(JSON())
    address_documents: Mapped[Optional[dict]] = mapped_column(JSON())
    identity_front_side: Mapped[Optional[str]] = mapped_column(String(255))
    identity_reverse_side: Mapped[Optional[str]] = mapped_column(
        String(255),
    )
    selfie: Mapped[Optional[str]] = mapped_column(String(255))

    # Server side fields
    status: Mapped[str] = mapped_column(
        Enum(StatusEnum),
        default="pending",
    )
    rejected_reason: Mapped[Optional[str]] = Column(Text())
    approved_at: Mapped[Optional[datetime.datetime]] = mapped_column()
    rejected_at: Mapped[Optional[datetime.datetime]] = mapped_column()

    def __str__(self):
        return f"{self.telegram_first_name} {self.telegram_last_name}"

    def __repr__(self):
        return f"<TelegramVerification: {self.telegram_first_name} {self.telegram_last_name}>"


class TelegramVerificationSchema(BaseModel):
    telegram_id: str
    phone_number: Optional[str] = None
    passport_data: Optional[Dict] = None
    personal_details: Optional[Dict] = None
    driver_license: Optional[Dict] = None
    identity_card: Optional[Dict] = None
    utility_bill: Optional[Dict] = None
    bank_statement: Optional[Dict] = None
    address: Optional[Dict] = None
    address_documents: Optional[Dict] = None
    identity_front_side: Optional[str] = None
    identity_reverse_side: Optional[str] = None
    selfie: Optional[str] = None

    # Server side fields
    status: str = "pending"
    rejected_reason: Optional[str] = None
    approved_at: Optional[datetime.datetime] = None
    rejected_at: Optional[datetime.datetime] = None

    def __str__(self):
        return f"{self.telegram_first_name} {self.telegram_last_name}"

    @classmethod
    def from_orm(cls, telegram_verification: TelegramVerification):
        return cls(
            telegram_id=telegram_verification.telegram_id,
            phone_number=telegram_verification.phone_number,
            passport_data=telegram_verification.passport_data,
            personal_details=telegram_verification.personal_details,
            driver_license=telegram_verification.driver_license,
            identity_card=telegram_verification.identity_card,
            utility_bill=telegram_verification.utility_bill,
            bank_statement=telegram_verification.bank_statement,
            address=telegram_verification.address,
            address_documents=telegram_verification.address_documents,
            identity_front_side=telegram_verification.identity_front_side,
            identity_reverse_side=telegram_verification.identity_reverse_side,
            selfie=telegram_verification.selfie,
            status=telegram_verification.status,
            rejected_reason=telegram_verification.rejected_reason,
            approved_at=telegram_verification.approved_at,
            rejected_at=telegram_verification.rejected_at,
        )
