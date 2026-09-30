from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Klasik SQLite veritabanı ayarımız
SQLALCHEMY_DATABASE_URL = "sqlite:///./analytics.db"

# SEBEP: BackgroundTasks kullanarak logları asenkron (arkaplanda) yazdıracağımız için,
# SQLite'ın "aynı anda birden fazla yerden yazma yapamazsın" kısıtlamasını aşmak adına
# check_same_thread=False ayarını ekliyoruz.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# API uç noktalarında (CQRS dosyalarında) kullanacağımız bağımlılık (Dependency)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
