from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    ad = Column(String)
    soyad = Column(String)
    unvan = Column(String)
    
    # Sisteme giriş (Login/JWT) yapabilmek için gereken kritik alanlar:
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    # Bir kullanıcının birden fazla projesi olabilir (One-to-Many İlişkisi)
    projects = relationship("Project", back_populates="owner")


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    project_adi = Column(String, index=True)
    durum = Column(String)
    
    # Hangi kullanıcıya ait olduğunu belirten Dış Anahtar (Foreign Key)
    user_id = Column(Integer, ForeignKey("users.id"))

    # İlişki (Bu projenin sahibi)
    owner = relationship("User", back_populates="projects")
