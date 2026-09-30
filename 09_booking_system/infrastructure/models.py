from sqlalchemy import Column, Integer, String, DateTime
from infrastructure.database import Base

class AppointmentModel(Base):
    """
    ==========================================
    INFRASTRUCTURE (ALTYAPI / VERİTABANI MODELİ)
    ==========================================
    Domain katmanındaki (Çekirdekteki) saf Python 'AppointmentEntity' nesnemizin 
    veritabanındaki (Tablo) karşılığıdır.
    SQLAlchemy kütüphanesine bağımlı olan her şey sadece bu dış katmandadır.
    """
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    doctor_name = Column(String, index=True)
    patient_name = Column(String)
    start_time = Column(DateTime, index=True)
    end_time = Column(DateTime)
