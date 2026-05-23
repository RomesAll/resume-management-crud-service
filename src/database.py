from sqlalchemy import create_engine, text
from config import settings

engine = create_engine(
    url=settings.postgres.database_url,
    pool_size=5,
    max_overflow=10,
    pool_recycle=3600
)