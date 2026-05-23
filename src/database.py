from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings

engine = create_engine(
    url=settings.postgres.database_url,
    pool_size=5,
    max_overflow=10,
    pool_recycle=3600
)

session_factory = sessionmaker(bind=engine, expire_on_commit=True)