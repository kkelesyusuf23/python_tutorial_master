from pydantic import BaseModel
from .models import OrderStatus

# ==========================================
# DOMAIN (ÇEKİRDEK) KATMANI - ŞEMALAR
# ==========================================
# SEBEP: API'ye dışarıdan gelecek olan JSON verisinin doğrulanması (Pydantic).
# Müşteri sipariş verirken sadece kendi adını ve tutarı gönderir, 
# durumunu (status) gönderemez.

class OrderCreate(BaseModel):
    customer_name: str
    total_amount: float

class OrderResponse(BaseModel):
    id: int
    customer_name: str
    total_amount: float
    status: OrderStatus # Durum bilgisini de cevap olarak döneriz

    class Config:
        from_attributes = True
