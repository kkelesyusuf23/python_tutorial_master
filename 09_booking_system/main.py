from fastapi import FastAPI
from infrastructure.database import Base, engine
from interfaces import routers

# Uygulama başlatılırken SQLite tablolarını oluştur
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Rezervasyon Sistemi (Clean Architecture)",
    description="Domain, Use Cases, Interfaces ve Infrastructure katmanlarına bölünmüş kurumsal mimari.",
    version="1.0.0"
)

# Arayüz katmanında yazdığımız Router'ı ana uygulamamıza bağlıyoruz
app.include_router(routers.router)

@app.get("/")
def root():
    return {"message": "Rezervasyon Sistemi API'sine Hoşgeldiniz. Lütfen /docs adresinden test yapın."}
