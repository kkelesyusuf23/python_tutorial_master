from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scalar_fastapi import add_scalar_reference

from database import engine, Base
from routers import auth, projects

# 1. Modellerdeki (SQLAlchemy) tabloları veritabanında oluştur
Base.metadata.create_all(bind=engine)

# 2. FastAPI Uygulaması
app = FastAPI(
    title="Gelişmiş Portfolio API",
    description="N-Katmanlı mimari ve JWT destekli API",
    version="2.0.0",
    docs_url=None,
    redoc_url=None
)

# 3. CORS Ayarları
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. Scalar Dokümantasyonu
add_scalar_reference(app, route="/scalar")

# 5. ROUTERS (Yönlendiricilerin Ana Uygulamaya Bağlanması)
app.include_router(auth.router)
app.include_router(projects.router)

@app.get("/")
def read_root():
    return {"message": "N-Katmanlı Portfolio API'ye Hoşgeldiniz! Lütfen dokümantasyon için /scalar adresine gidin."}
