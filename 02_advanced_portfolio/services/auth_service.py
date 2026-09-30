from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate
from core.security import get_password_hash, verify_password

def get_user_by_username(db: Session, username: str):
    """Veritabanından username'e göre kullanıcı arar."""
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserCreate):
    """Yeni bir kullanıcı kaydeder (Şifreyi Hashleyerek)."""
    # core/security.py içerisindeki fonksiyonu kullanarak şifreyi karmaşıklaştırıyoruz
    hashed_pw = get_password_hash(user.password)
    
    db_user = User(
        username=user.username,
        ad=user.ad,
        soyad=user.soyad,
        unvan=user.unvan,
        hashed_password=hashed_pw
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username: str, password: str):
    """Kullanıcı adı ve şifre ile giriş (Login) denemesini kontrol eder."""
    user = get_user_by_username(db, username)
    if not user:
        return False
        
    # Girilen şifrenin doğruluğunu kontrol ediyoruz
    if not verify_password(password, user.hashed_password):
        return False
        
    return user
