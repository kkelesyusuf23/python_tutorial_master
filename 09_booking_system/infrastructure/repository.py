from sqlalchemy.orm import Session
from datetime import datetime
from infrastructure.models import AppointmentModel
from domain.entities import AppointmentEntity

class SQLiteAppointmentRepository:
    """
    ==========================================
    INFRASTRUCTURE (ALTYAPI / REPOSITORY)
    ==========================================
    İş kuralları (Use Cases) bu sınıfa emir verir ("Git kaydet", "Çakışma var mı bak"), 
    bu sınıf da SQLAlchemy kodlarını kullanarak veritabanına gider.
    Yarın veritabanı SQLite'dan Mongo'ya geçerse SADECE BU DOSYA DEĞİŞİR!
    """
    def __init__(self, db: Session):
        self.db = db

    def check_overlap(self, doctor_name: str, start_time: datetime, end_time: datetime) -> bool:
        # RACE CONDITION (Yarış Durumu) ÖNLEMİ:
        # Seçilen doktorun o saatler aralığında başka bir randevusu var mı sorgusu.
        # Eğer Postgres kullansaydık, aynı anda 2 kişinin almasını engellemek için
        # sorgunun sonuna .with_for_update() (Satır Kilidi / Row Lock) eklerdik!
        overlapping = self.db.query(AppointmentModel).filter(
            AppointmentModel.doctor_name == doctor_name,
            AppointmentModel.start_time < end_time,
            AppointmentModel.end_time > start_time
        ).first()
        
        return overlapping is not None

    def save(self, doctor_name: str, patient_name: str, start_time: datetime, end_time: datetime) -> AppointmentEntity:
        new_app = AppointmentModel(
            doctor_name=doctor_name,
            patient_name=patient_name,
            start_time=start_time,
            end_time=end_time
        )
        self.db.add(new_app)
        self.db.commit()
        self.db.refresh(new_app)
        
        # ==========================================
        # CLEAN ARCHITECTURE'NIN ZİRVESİ:
        # İş kuralları (Domain) katmanı SQL modeli bilmesin, lekelenmesin diye,
        # veritabanından dönen SQL nesnesini, kendi yazdığımız 
        # saf Python 'AppointmentEntity' nesnesine dönüştürüp (Map) yukarıya yolluyoruz!
        # ==========================================
        return AppointmentEntity(
            id=new_app.id,
            doctor_name=new_app.doctor_name,
            patient_name=new_app.patient_name,
            start_time=new_app.start_time,
            end_time=new_app.end_time
        )
