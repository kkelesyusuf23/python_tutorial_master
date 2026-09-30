from pydantic import BaseModel
from datetime import datetime

# ==========================================
# PYDANTIC ŞEMALARI
# ==========================================

class LogCreate(BaseModel):
    """Sisteme dışarıdan (başka bir servisten) log yollanırken beklediğimiz veri yapısı"""
    endpoint: str
    method: str
    response_time_ms: float

class LogResponse(LogCreate):
    """Sisteme kaydedilen bir logun geri döndürülme yapısı"""
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class StatResponse(BaseModel):
    """
    CQRS MİMARİSİ İÇİN ÖZEL ŞEMA!
    Veritabanında StatResponse diye bir tablo YOKTUR! 
    Sadece Query (Okuma) kısmı, binlerce logu okuyup analiz ettikten sonra
    veriyi bu formata sokup (Örn: ortalama süre) müşteriye gönderir.
    """
    endpoint: str
    total_requests: int
    avg_response_time_ms: float
