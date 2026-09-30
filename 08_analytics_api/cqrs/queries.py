from sqlalchemy.orm import Session
from sqlalchemy import func
from models import LogRecord

class LogQueries:
    """
    ==========================================
    CQRS - SADECE OKUMA VE ANALİZ (QUERIES)
    ==========================================
    SEBEP: Bu sınıfın görevi veritabanına tek bir harf bile yazmamaktır!
    Tek işi, yönetici "Bana uç noktaların performans istatistiklerini getir" dediğinde,
    binlerce logu hızlıca tarayıp, toplayıp (count), ortalamasını (avg) çıkarıp
    bir rapor (StatResponse formunda) sunmaktır.
    """
    @staticmethod
    def get_endpoint_statistics(db: Session):
        # SQL Karşılığı: SELECT endpoint, COUNT(id), AVG(response_time_ms) FROM logs GROUP BY endpoint
        stats = db.query(
            LogRecord.endpoint,
            func.count(LogRecord.id).label('total_requests'),
            func.avg(LogRecord.response_time_ms).label('avg_response_time_ms')
        ).group_by(LogRecord.endpoint).all()

        # SQLAlchemy'nin döndürdüğü karmaşık veri yapısını API'nin anlayacağı temiz sözlüklere (dict) çeviriyoruz
        result = []
        for stat in stats:
            result.append({
                "endpoint": stat.endpoint,
                "total_requests": stat.total_requests,
                # Süre küsuratlı (24.5678) çıkabileceği için yuvarlıyoruz (24.57)
                "avg_response_time_ms": round(stat.avg_response_time_ms, 2) if stat.avg_response_time_ms else 0.0
            })
        return result
