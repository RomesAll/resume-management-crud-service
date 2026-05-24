from sqlalchemy import select, insert, update, delete
from sqlalchemy import Engine

from src.database import engine
from src.schemas import WorkerCreate, WokerUpdate
from src.models import Worker

class WorkerRepository:

    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def select_workers(self):
        with self.engine.connect() as conn:
            query = select(Worker).options()
            result = conn.execute(query).all()
        return result

    def create_workers(self, worker: WorkerCreate):
        with self.engine.connect() as conn:
            stmt = insert(Worker).values(**worker.model_dump()).returning(Worker)
            result = conn.execute(stmt)
            conn.commit()
        return result.all()

    def update_workers(self, worker: WokerUpdate):
        with self.engine.connect() as conn:
            stmt = update(Worker).where(Worker.id == worker.id).values(**worker.model_dump()).returning(Worker)
            result = conn.execute(stmt)
            conn.commit()
        return result.all()

    def delete_workers(self, id: int):
        with self.engine.connect() as conn:
            stmt = delete(Worker).where(Worker.id == id).returning(Worker)
            result = conn.execute(stmt)
            conn.commit()
        return result.all()

w = WorkerRepository(engine)
a = w.select_workers()
print(a)