from abc import ABC
from .orm import Base
from typing import TypeVar, Type

ModelType = TypeVar("ModelType", bound=Base)


class AbstractRepository(ABC):

    def __init__(self, order=None, vessel=None, equipment=None) -> None:
        if vessel:
            self._vessel = vessel

        if order:
            self._order = order

        if equipment:
            self._equipment = equipment