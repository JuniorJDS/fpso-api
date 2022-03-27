from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from app.schemas.schema import Vessel
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from app.database import get_db
from app.repositories.vessels import vesselsDB
from sqlalchemy.exc import IntegrityError


router = APIRouter()


@router.post(
    '', 
    summary='Register a New Vessel', 
    status_code=HTTP_201_CREATED
)
def post_vessel(
    vessel: Vessel,
    db: Session = Depends(get_db)
):
    """ 
    Insert a new Vessel by Code.
    {"code": "MV102"}
    """
    try:
        obj = vesselsDB.create(db, vessel=vessel)
    except IntegrityError as e:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, 
            detail="Não foi possível inserir."
        )
    return obj
