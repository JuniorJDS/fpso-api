from tests.integration.base import BaseTest
from app.config.settings import settings
import json


class TestVessel(BaseTest):

    def test_vessel__register_new_valid_vessel__expected_201(self):
        # FIXTURE
        new_vessel = {
            "code": "MV100"
        }
        # EXERCISE
        result = self.client.post(f"{settings.API_V1}/vessel", data=json.dumps(new_vessel))

        # ASSERTS
        assert result.status_code == 201
        res = result.json()
        assert res["code"] == 'MV100'

    def test_vessel__register_duplicated_vessel__expected_400(self):
        # FIXTURE
        new_vessel = {
            "code": "MV100"
        }
        # EXERCISE
        result = self.client.post(f"{settings.API_V1}/vessel", data=json.dumps(new_vessel))

        # ASSERTS
        assert result.status_code == 400
        res = result.json()
        assert res == {'detail': 'Não foi possível inserir.'}
