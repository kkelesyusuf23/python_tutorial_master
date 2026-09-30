from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from schemas import ProjectCreate, ProjectResponse
from services import project_service
from models import User
from routers.auth import get_current_user

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.get("/", response_model=List[ProjectResponse])
def read_projects(db: Session = Depends(get_db)):
    """Tüm projeleri listeler. (Token gerektirmez - Herkese açık)"""
    return project_service.get_projects(db)

@router.post("/", response_model=ProjectResponse, status_code=201)
def create_project(project: ProjectCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Sisteme yeni proje ekler. (Sadece Token'ı olan - Giriş yapmış kullanıcılar ekleyebilir)"""
    # current_user: Depends(get_current_user) satırı sayesinde bu uç noktaya şifresiz girilemez!
    return project_service.create_project(db, project=project, user_id=current_user.id)

@router.delete("/{id}", status_code=204)
def delete_project(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Mevcut bir projeyi siler. (Sadece projeyi oluşturan kişi silebilir)"""
    db_project = project_service.get_project(db, project_id=id)
    
    if not db_project:
        raise HTTPException(status_code=404, detail="Proje bulunamadı")
        
    # Güvenlik Kontrolü: Bu projeyi silmeye çalışan kişi (current_user.id), projeyi oluşturan kişiyle (db_project.user_id) aynı mı?
    if db_project.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu projeyi silme yetkiniz yok!")
        
    project_service.delete_project(db, db_project)
    return
