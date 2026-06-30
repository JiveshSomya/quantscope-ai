from datetime import datetime

from sqlalchemy import ForeignKey, Float, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


class Portfolio(Base):
    __tablename__ = "portfolio"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    ticker: Mapped[str] = mapped_column(
        String(10)
    )

    quantity: Mapped[float] = mapped_column(
        Float
    )

    buy_price: Mapped[float] = mapped_column(
        Float
    )

    purchase_date: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    user = relationship(
    "User",
    back_populates="portfolio"
)