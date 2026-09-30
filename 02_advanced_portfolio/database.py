from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite veritabanı bağlantı ayarlarımız (Infrastructure Katmanı)
SQLALCHEMY_DATABASE_URL = "sqlite:///./advanced_portfolio.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Modellerimizin miras alacağı temel (Base) sınıf
Base = declarative_base()

# API isteklerinde veritabanı bağlantısı açıp kapatacak olan bağımlılık (Dependency)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
