from app.repositories.base_repository import AbstractRepository
from sqlalchemy.orm import Session
from app.repositories.models import Vessels
from app.schemas.schema import Vessel


class VesselsRepository(AbstractRepository):
    def create(self, db: Session, vessel: Vessel):
        obj = self._vessel(
            code=vessel.code
        )
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj
    
    def get_by_code(self, db: Session, code: str):
        return db.query(self._vessel).filter(self._vessel.code == code).first()

    def remove_all(self, db: Session):
        db.query(self._vessel).delete()


vesselsDB = VesselsRepository(vessel=Vessels)