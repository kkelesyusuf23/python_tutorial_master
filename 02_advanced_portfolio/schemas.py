from pydantic import BaseModel
from typing import List, Optional

# ==========================================
# PROJECT ŞEMALARI
# ==========================================
class ProjectBase(BaseModel):
    project_adi: str
    durum: str

# Yeni proje oluştururken kullanılacak şema
class ProjectCreate(ProjectBase):
    pass

# Veritabanından projeyi okuyup kullanıcıya gösterirken kullanılacak şema
class ProjectResponse(ProjectBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True


# ==========================================
# USER ŞEMALARI
# ==========================================
class UserBase(BaseModel):
    username: str
    ad: str
    soyad: str
    unvan: str

# Yeni kullanıcı kayıt (Register) olurken gönderilecek veri (Düz şifre içerir)
class UserCreate(UserBase):
    password: str 

# Kullanıcı bilgilerini geri dönerken şifreyi asla dönmeyiz (Response Şeması)
class UserResponse(UserBase):
    id: int
    projects: List[ProjectResponse] = [] # Kullanıcının sahip olduğu projeleri de listeleriz

    class Config:
        from_attributes = True


# ==========================================
# TOKEN ŞEMALARI
# ==========================================
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
