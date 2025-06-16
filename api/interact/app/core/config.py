from pydantic import BaseSettings

class Settings(BaseSettings):
    kafka_bootstrap: str
    kafka_topic: str = "user-events"

settings = Settings()
