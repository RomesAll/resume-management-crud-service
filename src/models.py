from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import MetaData, text, ForeignKey, DateTime, func
from typing import Annotated
from datetime import datetime, timezone

from enum import Enum

time_zone = text("TIMEZONE('utc', now())")
int_pk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]

class Base(DeclarativeBase):
    metadata = MetaData()
    __abstract__ = True
    __mapper_args__ = {
        'confirm_deleted_rows': False,
    }

    def __repr__(self):
        return f'<{self.__class__.__name__}>'

    def to_dict(self) -> dict:
        result = {}
        for column in self.__table__.columns:
            value = getattr(self, column.name)
            result[column.name] = value
        return result

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default = func.timezone('utc', func.now())
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default = func.timezone('utc', func.now()),
        onupdate=lambda: datetime.now(timezone.utc)
    )

class WorkLoad(Enum):
    part_time = "part_time"
    full_time = "full_time"

class Worker(Base):
    __tablename__ = "worker"
    id: Mapped[int_pk]
    username: Mapped[str]

class Resume(Base):
    __tablename__ = "resume"
    id: Mapped[int_pk]
    title: Mapped[str]
    workload: Mapped[WorkLoad]
    worker_id: Mapped[int] = mapped_column(
        ForeignKey('worker.id',
                   ondelete="CASCADE"),
    )

class Vacancy(Base):
    __tablename__ = "vacancy"
    id: Mapped[int_pk]
    title: Mapped[str]