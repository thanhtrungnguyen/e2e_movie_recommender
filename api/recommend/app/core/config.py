from pydantic import BaseSettings

class Settings(BaseSettings):
    db_url: str
    model_path: str

settings = Settings()
