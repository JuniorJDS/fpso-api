from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from app.schemas.schema import Equipment, VesselEquipment, EquipmentsCode
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from app.database import get_db
from app.repositories.vessels import vesselsDB
from app.repositories.equipments import equipmentsDB
from sqlalchemy.exc import IntegrityError


router = APIRouter()


@router.post(
    '/{vessel_code}', 
    summary='Insert equipment in a Vessel',
    status_code=HTTP_201_CREATED
)
async def post_equipment(
    vessel_code: str,
    equipment: Equipment,
    db: Session = Depends(get_db)
):
    """
    Inserir equipamento em vessel
    default status: active
    {"name": "compressor", "code": "5310B9D7", "location": "Brazil"}
    """
    _vessel = vesselsDB.get_by_code(db, vessel_code)
    if not _vessel:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, 
            detail="vessel not found."
        )

    equipment_by_vessel = {
        **equipment.dict(), 
        "vessel_code": vessel_code
    }

    try:
        obj = equipmentsDB.create(
            db, equipment=VesselEquipment(**equipment_by_vessel)
        )
    except IntegrityError as e:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, 
            detail="Não foi possível inserir."
        )


    return obj


@router.patch('/equipments-code/inactivate', summary='Inactive a list of equipment')
async def patch_status(
    code: EquipmentsCode
):
    """ 
    Inativar um ou uma lista de equipamentos.
    """
    if not code.equipments_code:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, 
            detail="Lista de equipamentos vazia."
        )

    return code


@router.get('/{vessel_code}', summary='List all active equipments by vessel')
async def get_equipments_by_vessel(
    vessel_code: str,
    db: Session = Depends(get_db)
):
    obj = equipmentsDB.get_by_vessel(db, vessel_code)
    return obj