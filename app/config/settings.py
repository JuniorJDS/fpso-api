import os
from pydantic import BaseSettings
from dotenv import load_dotenv


load_dotenv()

class Settings(BaseSettings):
    """ Configurações globais """

    API_V1: str = "/api/v1"
    SQLALCHEMY_DATABASE_URI: str = os.getenv('SQLALCHEMY_DATABASE_URI')


settings = Settings()