from fastapi import APIRouter
from app.utils.google_maps import get_nearby_hospitals

router = APIRouter()

@router.get("/hospitals")
async def hospitals(latitude: float, longitude: float):
    try:
        hospitals = get_nearby_hospitals(latitude, longitude)
        return {"hospitals": hospitals}
    except Exception as e:
        return {"error": str(e)}
