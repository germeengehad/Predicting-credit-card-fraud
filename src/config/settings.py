from typing import Any, Dict, Optional
from pydantic_settings import BaseSettings 
from pydantic import validator, PostgresDsn

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    APP_NAME: Optional[str] = None
    DOMAIN: Optional[str] = "localhost"
    DEBUG_MODE: bool = True
    BACKEND_PORT: int = 8000

    @validator("BACKEND_PORT", pre=True)
    def set_port_default(cls, v: str):
        if v:
            return v
        return 8000

settings = Settings()  