from fastapi import APIRouter
from pydantic import BaseModel
from app.utils.dummy_data import dummy_hospitals

router = APIRouter()

class AppointmentRequest(BaseModel):
    hospital_id: str
    doctor_id: str
    patient_name: str
    date: str
    time: str

@router.get("/hospitals")
async def get_hospitals():
    return {"hospitals": dummy_hospitals}

@router.post("/book-appointment")
async def book_appointment(request: AppointmentRequest):
    try:
        appointment_details = {
            "hospital_id": request.hospital_id,
            "doctor_id": request.doctor_id,
            "patient_name": request.patient_name,
            "date": request.date,
            "time": request.time,
            "status": "Confirmed"
        }
        return {"message": "Appointment booked successfully", "appointment": appointment_details}
    except Exception as e:
        return {"error": str(e)}
