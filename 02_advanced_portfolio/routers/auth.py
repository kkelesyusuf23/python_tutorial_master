from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from database import get_db
from models import User
from schemas import UserCreate, UserResponse, Token
from services import auth_service
from core.security import SECRET_KEY, ALGORITHM, create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

# FastAPI'ye Token'ın nereden alınacağını söylüyoruz
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# ==========================================
# DEPENDENCY: YETKİLİ KULLANICI KONTROLÜ
# ==========================================
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """Gelen token'ı çözer, geçerliyse veritabanından kullanıcıyı bulup döndürür."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token geçersiz veya süresi dolmuş",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Token'ı çöz
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("username")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
        
    # Kullanıcıyı veritabanında bul
    user = auth_service.get_user_by_username(db, username=username)
    if user is None:
        raise credentials_exception
        
    return user


# ==========================================
# ENDPOINTS
# ==========================================
@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """Sisteme yeni bir kullanıcı kaydeder."""
    db_user = auth_service.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Bu kullanıcı adı zaten alınmış.")
    return auth_service.create_user(db=db, user=user)

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Kullanıcı adı ve şifre ile giriş yapıp JWT Token döndürür."""
    user = auth_service.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Kullanıcı adı veya şifre hatalı")
        
    # Başarılıysa Token üret
    access_token = create_access_token(data={"username": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
