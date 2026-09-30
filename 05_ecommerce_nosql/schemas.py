from pydantic import BaseModel, Field
from typing import Dict, Any, Optional

# ==========================================
# DİNAMİK ŞEMA MANTIĞI (NoSQL GÜCÜ)
# ==========================================
# SEBEP: Bir bilgisayar satarken "RAM" ve "İşlemci" bilgisine, 
# tişört satarken "Beden" ve "Renk" bilgisine ihtiyacımız vardır.
# SQL'de bunu çözmek için onlarca boş sütun açmak zorundayken, NoSQL'de 
# Dict[str, Any] diyerek kullanıcının istediği JSON verisini (attributes) 
# esnekçe kaydetmesine izin veriyoruz!

class ProductBase(BaseModel):
    name: str
    price: float
    # Ürüne göre değişebilen dinamik özellikler. Boş bırakılırsa "{}" olarak ayarlanır.
    attributes: Dict[str, Any] = Field(default_factory=dict)

# Yeni ürün eklerken kullanılacak şema
class ProductCreate(ProductBase):
    pass

# MongoDB'den veri çekip dışarı yollarken kullanılacak şema
class ProductResponse(ProductBase):
    # SEBEP: SQL veritabanlarında ID'ler sayıdır (1, 2, 3).
    # Ancak MongoDB, verilerine eşsiz bir metin olan "ObjectId" (Örn: 5f4e6v...) atar.
    # Bu yüzden ID tipini int değil, str (metin) olarak kurguluyoruz.
    id: str 

    class Config:
        from_attributes = True
