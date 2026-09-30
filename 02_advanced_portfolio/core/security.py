from datetime import datetime, timedelta
from typing import Optional
from jose import jwt
from passlib.context import CryptContext

# ==========================================
# GÜVENLİK AYARLARI
# ==========================================
# Gerçek dünyada SECRET_KEY asla kodun içinde yazılmaz, .env gibi ortam değişkenlerinde saklanır.
SECRET_KEY = "super-gizli-portfolio-anahtari-bunu-kimseyle-paylasma"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # Token'ın geçerlilik süresi (30 dakika)

# Şifre hash'leme aracı olarak bcrypt kullanıyoruz
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ------------------------------------------
# 1. ŞİFRE İŞLEMLERİ
# ------------------------------------------

def get_password_hash(password: str) -> str:
    """Kullanıcının düz şifresini alıp, veritabanına kaydedilecek karmaşık (hash) hale getirir."""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Kullanıcının girdiği şifre ile veritabanındaki hash'lenmiş şifrenin eşleşip eşleşmediğini kontrol eder."""
    return pwd_context.verify(plain_password, hashed_password)

# ------------------------------------------
# 2. JWT TOKEN ÜRETİMİ
# ------------------------------------------

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Kullanıcı başarıyla giriş yaptığında ona verilecek olan yetki biletini (Token) üretir."""
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        
    to_encode.update({"exp": expire})
    
    # Bilgileri, gizli anahtarımızla (SECRET_KEY) mühürleyip token'ı oluşturuyoruz
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
