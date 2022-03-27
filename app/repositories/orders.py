from app.repositories.base_repository import AbstractRepository
from sqlalchemy.orm import Session
from app.repositories.models import Orders, Equipments, Vessels
from app.schemas.schema import EquipmentOrder
from sqlalchemy.sql import func


class OrdersRepository(AbstractRepository):
    def create(self, db: Session, order: EquipmentOrder):
        obj = self._order(
            type=order.type,
            cost=order.cost,
            equipment_code=order.equipment_code

        )
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj
    
    def get_by_equipment(self, db: Session, code: str):
        return db.query(func.sum(self._order.cost).label('total')).filter(
            self._order.equipment_code == code).first()

    def list_avg_cost_of_all_vessels(self, db: Session):
        return db.query(
            self._vessel.code,
            func.avg(self._order.cost).label('total')
            ).join(
                self._equipment, self._equipment.vessel_code == self._vessel.code
            ).filter(
                self._order.equipment_code == self._equipment.equipment_code,
            ).group_by(self._vessel.code).all()
            
            
            
            
            



ordersDB = OrdersRepository(order=Orders, vessel=Vessels, equipment=Equipments)