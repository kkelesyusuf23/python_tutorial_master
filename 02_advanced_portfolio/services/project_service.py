from sqlalchemy.orm import Session
from models import Project
from schemas import ProjectCreate

def get_projects(db: Session):
    return db.query(Project).all()

def get_project(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()

def create_project(db: Session, project: ProjectCreate, user_id: int):
    """Yeni projeyi, onu oluşturan kullanıcının ID'si ile (user_id) kaydeder."""
    db_project = Project(
        project_adi=project.project_adi,
        durum=project.durum,
        user_id=user_id  # ForeignKey bağlantısı
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def update_project(db: Session, db_project: Project, project: ProjectCreate):
    db_project.project_adi = project.project_adi
    db_project.durum = project.durum
    db.commit()
    db.refresh(db_project)
    return db_project

def delete_project(db: Session, db_project: Project):
    db.delete(db_project)
    db.commit()
    return db_project
