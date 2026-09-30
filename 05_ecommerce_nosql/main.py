from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import products

app = FastAPI(
    title="NoSQL E-Ticaret API",
    description="MongoDB ve Repository Pattern kullanılarak geliştirilmiş esnek e-ticaret altyapısı.",
    version="1.0.0",
)

# CORS Ayarları (Örn: React veya Vue ile bağlandığında sorun yaşamamak için)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router'ları (Garsonları) ana uygulamaya (Restoran Müdürüne) tanıttık
app.include_router(products.router)

@app.get("/")
async def root():
    return {"message": "NoSQL E-Ticaret Kataloğuna Hoşgeldiniz! Test için lütfen /docs adresine gidin."}
