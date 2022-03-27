from fastapi import APIRouter
from app.routes.v1.endpoints import equipments, vessel, orders


endpoint_router = APIRouter()


endpoint_router.include_router(vessel.router, prefix='/vessel', tags=['Vessel'])
endpoint_router.include_router(equipments.router, prefix='/equipments', tags=['Equipments'])
endpoint_router.include_router(orders.router, prefix='/orders', tags=['Orders'])