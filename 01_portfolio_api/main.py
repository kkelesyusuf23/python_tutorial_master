from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from pydantic import BaseModel
from scalar_fastapi import add_scalar_reference
from typing import List

# ==========================================
# 1. VERİTABANI BAĞLANTISI (SQLAlchemy)
# ==========================================
SQLALCHEMY_DATABASE_URL = "sqlite:///./portfolio.db"

# SQLite, tek iş parçacığı kısıtlamasına sahip olduğu için check_same_thread=False yapıyoruz
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# ==========================================
# 2. VERİTABANI MODELLERİ
# ==========================================
class ProjectDB(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    technologies = Column(String)  # Örn: "Python, FastAPI"

# Tabloları veritabanında (portfolio.db dosyasında) oluştur
Base.metadata.create_all(bind=engine)


# ==========================================
# 3. PYDANTIC ŞEMALARI (Veri Doğrulama)
# ==========================================
class ProjectCreate(BaseModel):
    title: str
    description: str
    technologies: str

class ProjectResponse(BaseModel):
    id: int
    title: str
    description: str
    technologies: str

    class Config:
        from_attributes = True  # SQLAlchemy objesini Pydantic modeline dönüştürmeye yarar (Pydantic v2 için)


from fastapi.middleware.cors import CORSMiddleware

# ==========================================
# 4. FASTAPI UYGULAMASI VE ENDPOINTLER
# ==========================================
app = FastAPI(
    title="Portfolio API",
    description="Temel CRUD işlemleri içeren 1 Katmanlı Portfolio API",
    version="1.0.0",
    docs_url=None, # Varsayılan Swagger UI'ı (docs) kapattık, artık sadece Scalar kullanacağız
    redoc_url=None
)

# Frontend'in (HTML/JS) API ile konuşabilmesi için CORS ayarları
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Scalar arayüzünü /scalar adresine tanımlıyoruz
add_scalar_reference(app, route="/scalar")

# Her istekte veritabanı bağlantısı açıp kapatmak için Dependency (Bağımlılık)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "Portfolio API'ye Hoşgeldiniz! Gelişmiş dokümantasyon (Scalar) için /scalar adresine gidebilirsiniz."}

# ==========================================
# 5. CRUD İŞLEMLERİ
# ==========================================

# C - CREATE (Yeni Proje Ekleme)
@app.post("/projects", response_model=ProjectResponse, status_code=201)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    # 1. Pydantic şemasından gelen veriyi veritabanı objesine (SQLAlchemy Modeli) dönüştür
    db_project = ProjectDB(
        title=project.title,
        description=project.description,
        technologies=project.technologies
    )
    # 2. Veriyi veritabanı oturumuna ekle
    db.add(db_project)
    # 3. Değişiklikleri kalıcı olarak kaydet (Commit)
    db.commit()
    # 4. Veritabanının otomatik atadığı 'id' değerini almak için objeyi yenile (Refresh)
    db.refresh(db_project)
    
    # Oluşturulan objeyi geri döndür (FastAPI otomatik olarak ProjectResponse şemasına çevirir)
    return db_project




@app.get("/projects", response_model=List[ProjectResponse])
def get_projects(db: Session = Depends(get_db)):
    veriler = db.query(ProjectDB).all()
    return veriler



@app.get("/projects/{id}", response_model=ProjectResponse)
def get_project(id: int, db: Session = Depends(get_db)):
    veri = db.query(ProjectDB).filter(ProjectDB.id == id).first()
    
    if not veri:
        # Eğer veri veritabanında yoksa 404 (Not Found) hatası fırlat
        raise HTTPException(status_code=404, detail="Proje bulunamadı")
        
    return veri


@app.put("/projects/{id}", response_model=ProjectResponse)
def update_project(id: int, project: ProjectCreate, db: Session = Depends(get_db)):
    # 1. Önce güncellenecek kaydı bul (Senin yazdığın kısım - Harika!)
    veri = db.query(ProjectDB).filter(ProjectDB.id == id).first()
    
    if not veri:
        raise HTTPException(status_code=404, detail="Proje bulunamadı")
        
    # 2. Bulunan kaydın değerlerini kullanıcının gönderdiği yeni (project) verilerle değiştir
    veri.title = project.title
    veri.description = project.description
    veri.technologies = project.technologies
    
    # 3. Değişiklikleri veritabanına kaydet
    db.commit()
    db.refresh(veri)
    
    return veri

# D - DELETE (Mevcut Projeyi Silme)
@app.delete("/projects/{id}", status_code=204)
def delete_project(id: int, db: Session = Depends(get_db)):
    # 1. Önce silinecek kaydı bul
    veri = db.query(ProjectDB).filter(ProjectDB.id == id).first()
    
    if not veri:
        raise HTTPException(status_code=404, detail="Proje bulunamadı")
        
    # 2. Veriyi sil
    db.delete(veri)
    
    # 3. Değişiklikleri kaydet
    db.commit()
    
    # status_code=204 (No Content) olduğu için bir şey döndürmemize gerek yok
    return


