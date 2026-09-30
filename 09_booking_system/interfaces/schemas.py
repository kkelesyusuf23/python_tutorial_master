from pydantic import BaseModel
from datetime import datetime

class AppointmentCreate(BaseModel):
    doctor_name: str
    patient_name: str
    start_time: datetime
    end_time: datetime

class AppointmentResponse(BaseModel):
    id: int
    doctor_name: str
    patient_name: str
    start_time: datetime
    end_time: datetime
