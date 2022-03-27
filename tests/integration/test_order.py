from tests.integration.base import BaseTest
from app.config.settings import settings
import json


class TestOrders(BaseTest):
    def test_orders__insert_order_to_equipment__expected_201(
        self
    ):
        # FIXTURE
        vessel_code = 'MV300'

        _equipment = {
            "name": "Compressor",
            "code": "5310B9D1",
            "location": "Brazil",
            "vessel_code": vessel_code
        }
        equipment_code = _equipment["code"]

        _order = {
            "type": "fix",
            "cost": 20000
        }

        self.create_vessel(code=vessel_code)
        self.create_equipment(equipment=_equipment)

        # EXERCISE
        result = self.client.post(
            f"{settings.API_V1}/orders/{equipment_code}", 
            data=json.dumps(_order)
        )

        # ASSERTS
        assert result.status_code == 201

        resp = result.json()

        assert resp["type"] == _order["type"]
        assert resp["cost"] == _order["cost"]
        assert resp["equipment_code"] == equipment_code