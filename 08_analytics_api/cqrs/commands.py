from sqlalchemy.orm import Session
from models import LogRecord
from schemas import LogCreate

class LogCommands:
    """
    ==========================================
    CQRS - SADECE YAZMA İŞLEMLERİ (COMMANDS)
    ==========================================
    SEBEP: Bu sınıfın tek amacı sisteme gelen ham veriyi olabildiğince 
    hızlı bir şekilde veritabanına KAYDETMEKTİR.
    İçerisinde analiz yapacak, veriyi gruplayacak veya ortalama çıkaracak 
    hiçbir ağır okuma (SELECT) kodu bulunamaz! İşi sadece "Yaz"maktır.
    """
    @staticmethod
    def create_log(db: Session, log_data: LogCreate):
        new_log = LogRecord(
            endpoint=log_data.endpoint,
            method=log_data.method,
            response_time_ms=log_data.response_time_ms
        )
        db.add(new_log)
        db.commit()
        db.refresh(new_log)
        return new_log
