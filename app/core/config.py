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

    # Lista de orígenes permitidos para CORS.
    # Es crucial agregar la URL de tu frontend de Vercel aquí una vez que la tengas.
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost",
        "http://localhost:3000",
        "http://localhost:8080",
    ]

    class Config:
        case_sensitive = True
        # El archivo .env debe estar en la raíz del directorio 'backend'
        env_file = ".env"
        env_file_encoding = 'utf-8'

# Instancia de la configuración que será importada en otros módulos
settings = Settings()
