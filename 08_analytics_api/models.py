from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base

class LogRecord(Base):
    """
    ==========================================
    LOG TABLOSU (VERİ MODELİ)
    ==========================================
    Analitik verilerinin (Logların) tutulduğu ana tablomuz.
    Örn: Başka bir servisten bize şu bilgi gelir:
    "Bir kullanıcı /api/products sayfasına GET isteği attı ve sunucu bu isteği 45ms'de tamamladı."
    """
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    endpoint = Column(String, index=True) # Hangi URL/adrese girildi? (Örn: /api/login)
    method = Column(String)               # İşlem tipi nedir? (Örn: GET, POST)
    response_time_ms = Column(Float)      # Sunucunun cevap verme süresi (Performans ölçümü)
    created_at = Column(DateTime, default=datetime.utcnow) # Logun atıldığı tarih/saat
