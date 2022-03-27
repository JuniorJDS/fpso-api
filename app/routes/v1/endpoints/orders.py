from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from app.schemas.schema import Order, EquipmentOrder
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from app.database import get_db
from app.repositories.vessels import vesselsDB
from app.repositories.equipments import equipmentsDB
from app.repositories.orders import ordersDB
from sqlalchemy.exc import IntegrityError


router = APIRouter()


@router.post(
    '/{equipment_code}', 
    summary='Insert Order to equipment', 
    status_code=HTTP_201_CREATED
)
async def post_order(
    equipment_code: str,
    order: Order,
    db: Session = Depends(get_db)
):
    """
    {"code": "5310B9D7", type: "replacement", "cost": "10000"}
    """
    _equipment = equipmentsDB.get_by_code(db, equipment_code)
    if not _equipment:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, 
            detail="Equipment não existe."
        )

    order_by_equipment = {
        **order.dict(), 
        "equipment_code": equipment_code
    }

    try:
        obj = ordersDB.create(
            db, order=EquipmentOrder(**order_by_equipment)
        )
    except IntegrityError as e:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, 
            detail="Não foi possível inserir."
        )


    return obj


@router.get('/total-cost/{equipment_code}', summary='Total Cost by Equipment')
async def get_total_cost_by_equipment(
    equipment_code: str,
    db: Session = Depends(get_db)
):
    """ 
    In
    """
    _equipment = equipmentsDB.get_by_code(db, equipment_code)
    if not _equipment:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, 
            detail="Equipment não existe."
        )

    obj = ordersDB.get_by_equipment(db, equipment_code)

    return obj


@router.get('/{vessel_code}/average-costs', summary='Average Cost of each Vessel')
async def get_average_cost(
    db: Session = Depends(get_db)
):
    """ 
    In
    """
    obj = ordersDB.list_avg_cost_of_all_vessels(db)

    return obj