from tests.integration.base import BaseTest
from app.config.settings import settings
import json


class TestEquipments(BaseTest):
    def test_equipments__register_equipment_to_valid_vessel__expected_201(
        self
    ):
        # FIXTURE
        vessel_code = 'MV100'

        equipment = {
            "name": "Compressor",
            "code": "5310B9D1",
            "location": "Brazil"
        }

        self.create_vessel(code=vessel_code)
        # EXERCISE
        result = self.client.post(
            f"{settings.API_V1}/equipments/{vessel_code}", 
            data=json.dumps(equipment)
        )

        # ASSERTS
        assert result.status_code == 201

        resp = result.json()

        assert resp["name"] == equipment["name"]
        assert resp["equipment_code"] == equipment["code"]
        assert resp["location"] == equipment["location"]
        assert resp["vessel_code"] == vessel_code
        assert resp["active"] == True

    def test_equipments__register_equipment_to_inexistent_vessel__expected_404(
        self
    ):
        # FIXTURE
        vessel_code = 'MV200'

        equipment = {
            "name": "Compressor",
            "code": "5310B9D1",
            "location": "Brazil"
        }

        # EXERCISE
        result = self.client.post(
            f"{settings.API_V1}/equipments/{vessel_code}", 
            data=json.dumps(equipment)
        )

        # ASSERTS
        assert result.status_code == 404
        assert result.text == '{"detail":"vessel not found."}'

    def test_equipments__list_all_active_equipments_of_a_vessel__expected_200(
        self
    ):
        # FIXTURE
        vessel_code = 'MV100'

        # EXERCISE
        result = self.client.get(
            f"{settings.API_V1}/equipments/{vessel_code}"
        )

        # ASSERTS
        assert result.status_code == 200
        resp = result.json()
        assert len(resp) == 1

        assert resp[0]["name"] == 'Compressor'
        assert resp[0]["equipment_code"] == '5310B9D1'
        assert resp[0]["location"] == 'Brazil'
        assert resp[0]["vessel_code"] == vessel_code
        assert resp[0]["active"] == True

    def test_equipments__list_all_active_equipments_of_a_non_existent_vessel__expected_200_and_empty_list(
        self
    ):
        # FIXTURE
        vessel_code = 'MV200'

        # EXERCISE
        result = self.client.get(
            f"{settings.API_V1}/equipments/{vessel_code}"
        )

        # ASSERTS
        assert result.status_code == 200
        resp = result.json()
        assert not resp