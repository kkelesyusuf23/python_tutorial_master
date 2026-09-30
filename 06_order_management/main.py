from fastapi import FastAPI
from routers import orders
from adapters.database_adapter import Base, engine
from scalar_fastapi import add_scalar_reference

# Proje ayağa kalktığı anda SQLite içindeki tablolarımızı (orders) otomatik oluştur.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sipariş Yönetimi (Celery & RabbitMQ)",
    description="Arka plan görevleri ve Hexagonal Mimari kullanılarak tasarlanmış gelişmiş sipariş yönetim sistemi.",
    version="1.0.0",
    docs_url=None, 
    redoc_url=None
)

# API testlerimizi çok daha rahat yapmak için Scalar arayüzünü ekliyoruz
add_scalar_reference(app, route="/scalar")

# Sipariş Garsonumuzu (Router) restorana (Uygulamaya) dahil ediyoruz
app.include_router(orders.router)

@app.get("/")
def root():
    return {"message": "Sipariş Sistemine Hoşgeldiniz. Lütfen /scalar adresine gidip test yapın."}
