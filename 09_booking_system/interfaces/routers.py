from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from infrastructure.database import get_db
from infrastructure.repository import SQLiteAppointmentRepository
from use_cases.booking import BookingUseCase
from domain.exceptions import OverlappingAppointmentError
from interfaces.schemas import AppointmentCreate, AppointmentResponse

router = APIRouter(prefix="/appointments", tags=["Appointments"])

@router.post("/", response_model=AppointmentResponse)
def create_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    """
    ==========================================
    INTERFACES (ARAYÜZLER / ROUTER)
    ==========================================
    Kullanıcıdan gelen web (HTTP) isteğini alır ve Use Case'e (İş kurallarına) fırlatır.
    İçinde ZERRE KADAR "Eğer başlangıç saati büyükse..." gibi bir kural veya 
    "db.query" gibi bir veritabanı kodu BARINDIRMAZ! O sadece bir "Trafik Polisi"dir.
    """
    # 1. Altyapı parçasını oluştur (Repository)
    repository = SQLiteAppointmentRepository(db)
    
    # 2. İş kuralları mekanizmasını (Use Case) oluştur ve içine kayıtçıyı tak (Dependency Injection)
    use_case = BookingUseCase(repository)

    try:
        # 3. İşi Use Case'e (Beyin Katmanına) devret!
        new_appointment = use_case.book_appointment(
            doctor_name=appointment.doctor_name,
            patient_name=appointment.patient_name,
            start_time=appointment.start_time,
            end_time=appointment.end_time
        )
        
        # Domain Entity'den dönen saf python sonucunu, Pydantic Schema ile Dış dünyaya döner.
        return new_appointment

    except OverlappingAppointmentError as e:
        # Eğer Çekirdek'ten "Bu saatler dolu!" özel hatası gelirse, bunu Web HTTP 400 hatasına çevir
        raise HTTPException(status_code=400, detail=e.message)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
