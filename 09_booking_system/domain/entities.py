from datetime import datetime
from dataclasses import dataclass

@dataclass
class AppointmentEntity:
    """
    ==========================================
    DOMAIN KATMANI (VARLIKLAR / ENTITIES)
    ==========================================
    SEBEP: Clean Architecture'da 'Domain' katmanı sistemin kalbidir. En iç halkadır.
    Burada hiçbir kütüphane veya framework (FastAPI, SQLAlchemy, Pydantic) KULLANILAMAZ!
    Sadece şirketin iş yaptığı "Nesneler" (Saf Python Dataclass) bulunur.
    Yarın veritabanını SQLite'dan PostgreSQL'e çeksek bile bu dosya ASLA değişmez!
    """
    id: int
    doctor_name: str
    patient_name: str
    start_time: datetime
    end_time: datetime

    def duration_minutes(self) -> int:
        """İş Kuralı (Business Logic): Randevunun kaç dakika süreceğini hesaplar."""
        delta = self.end_time - self.start_time
        return int(delta.total_seconds() / 60)
