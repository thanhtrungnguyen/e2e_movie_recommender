from fastapi import APIRouter
from app.core.model import get_recs

router = APIRouter(prefix="/recommend")

@router.get("/{user_id}")
def recommend(user_id: int, n: int = 10):
    recs = get_recs(user_id, n)
    return {"recommendations": recs}
