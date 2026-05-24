from models import Base
from database import engine, session_factory
from sqlalchemy import text
from datetime import datetime, timezone
from models import WorkLoad, Worker, Resume
from schemas import ResumeGet, WorkerGet, WorkerRel
import time

with engine.connect() as connection:
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    connection.commit()

with engine.connect() as connection:
    stmt1 = text("INSERT INTO worker (username) VALUES (:username1), "
                "(:username2), (:username3)").bindparams(
        username1='bob',
        username2='roman',
        username3='nikita'
    )
    connection.execute(stmt1)
    stmt2 = text("INSERT INTO resume "
                "(id, workload, worker_id) "
                "VALUES "
                "(:id1, :workload1, :worker_id1),"
                "(:id2, :workload2, :worker_id2),"
                "(:id3, :workload3, :worker_id3)").bindparams(
        id1='1', workload1=WorkLoad.part_time.value, worker_id1='1',
        id2='2', workload2=WorkLoad.full_time.value, worker_id2='1',
        id3='3', workload3=WorkLoad.part_time.value, worker_id3='2',
    )
    connection.execute(stmt2)
    stmt3 = text(
        "INSERT INTO vacancy VALUES "
        "(:id1, :title1, :compensation1),"
        "(:id2, :title2, :compensation2),"
        "(:id3, :title3, :compensation3)"
    ).bindparams(
        id1='1', title1='python backend', compensation1=30_000,
        id2='2', title2='frontend', compensation2=560_000,
        id3='3', title3='data science', compensation3=120_000
    )
    connection.execute(stmt3)
    connection.commit()
