from starlette.testclient import TestClient
from app.main import app
from tests.integration.help import helpDB
from fastapi.param_functions import Depends
from app.repositories.orm import SessionLocal
from typing import Dict


class BaseTest:
    @classmethod
    def setup_class(cls):
        cls.client = TestClient(app)
        cls.database = SessionLocal()

    def create_vessel(self, code: str):
        return helpDB.create(db=self.database, code=code)

    def create_equipment(self, equipment: Dict):
        return helpDB.create_equipment(
            db=self.database, equipment=equipment)

    @classmethod
    def teardown_class(cls):
        helpDB.remove_all(db=cls.database)