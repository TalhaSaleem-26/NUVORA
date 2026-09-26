from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    
    model_config = SettingsConfigDict(
        env_prefix="",
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

   
    DATABASE_URL:str
    APP_NAME:str
    ENVIRONMENT:str
    SECRET_KEY:str

    
settings=Settings()