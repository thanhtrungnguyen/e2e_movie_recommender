from fastapi import APIRouter
from pydantic import BaseModel
from app.core.kafka_producer import publish

router = APIRouter(prefix="/interact")

class Event(BaseModel):
    userId: int
    movieId: int
    action: str

@router.post("/")
def post_event(event: Event):
    publish(event.dict())
    return {"status": "event published"}
