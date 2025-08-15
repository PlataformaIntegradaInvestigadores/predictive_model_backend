# backend/app/core/config.py

from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    """
    Clase para gestionar la configuración de la aplicación.
    Lee las variables de entorno desde un archivo .env.
    """
    PROJECT_NAME: str = "Centinela Predictivo de Publicaciones Científicas"
    API_V1_STR: str = "/api/v1"

    
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "https://centinela.epn.edu.ec"
    ]

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()