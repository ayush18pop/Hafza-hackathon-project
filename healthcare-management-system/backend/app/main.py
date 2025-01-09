from fastapi import FastAPI
from app.routes import auth, map, appointments, health_records

app = FastAPI()

# Register routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(map.router, prefix="/map", tags=["Map"])
app.include_router(appointments.router, prefix="/appointments", tags=["Appointments"])
app.include_router(health_records.router, prefix="/health-records", tags=["Health Records"])

@app.get("/")
async def root():
    return {"message": "Healthcare Management System Backend"}
