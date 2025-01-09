from fastapi import APIRouter
from app.utils.fhir_api import get_patient_records

router = APIRouter()

@router.get("/health-records")
async def health_records(patient_id: str):
    try:
        records = get_patient_records(patient_id)
        return {"records": records}
    except Exception as e:
        return {"error": str(e)}
