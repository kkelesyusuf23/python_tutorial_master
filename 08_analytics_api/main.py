from fastapi import FastAPI, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List

from database import Base, engine, get_db
from schemas import LogCreate, StatResponse
from cqrs.commands import LogCommands
from cqrs.queries import LogQueries

# Uygulama ayağa kalkarken models.py'deki tüm tabloları veritabanında oluşturur
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Analitik ve Loglama API (CQRS)",
    description="Command Query Responsibility Segregation (CQRS) mimarisi ile tasarlanmış performanslı analitik sistemi.",
    version="1.0.0"
)

# ==========================================
# KOMUT (COMMAND) UÇ NOKTASI: SADECE YAZAR
# ==========================================
@app.post("/logs", status_code=202)
def log_event(log_data: LogCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """
    Sisteme (Diğer servislerden vb.) gelen performans loglarını kaydeder.
    
    SEBEP: Yüksek performanslı bir log API'sinde veritabanı yavaşlıkları 
    sistemi tıkamasın diye, kayıt işlemi "BackgroundTasks" ile arkaplana fırlatılır. 
    API, verinin kaydedilmesini beklemeden saniyesinde "Log alındı" der!
    """
    background_tasks.add_task(LogCommands.create_log, db, log_data)
    return {"status": "success", "message": "Log arka planda kaydedilmek üzere kuyruğa eklendi."}

# ==========================================
# SORGU (QUERY) UÇ NOKTASI: SADECE OKUR
# ==========================================
@app.get("/stats", response_model=List[StatResponse])
def get_statistics(db: Session = Depends(get_db)):
    """
    Sistem yöneticisinin uç noktaların (endpoints) hız performansını 
    ölçmek için çağırdığı istatistik (okuma/analiz) noktasıdır.
    """
    return LogQueries.get_endpoint_statistics(db)
