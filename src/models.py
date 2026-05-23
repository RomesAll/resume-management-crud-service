from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import MetaData, text, ForeignKey
from typing import Annotated
from datetime import datetime
from enum import Enum

time_zone = text("TIMEZONE('utc', now())")
int_pk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]

class Base(DeclarativeBase):
    metadata = MetaData()
    
    created_at: Mapped[datetime] = mapped_column(
        server_default = time_zone
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default = time_zone,
        onupdate = time_zone,
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