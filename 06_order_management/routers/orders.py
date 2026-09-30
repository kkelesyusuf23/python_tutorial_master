from fastapi import APIRouter, HTTPException
from domain.schemas import OrderCreate, OrderResponse
from adapters.database_adapter import SqliteDatabaseAdapter
from adapters.message_broker_adapter import AsyncBrokerAdapter # DEĞİŞTİ

router = APIRouter(prefix="/orders", tags=["Orders"])

# Adaptörlerimizi (iş yapıcılarımızı) başlatıyoruz
db_adapter = SqliteDatabaseAdapter()
broker_adapter = AsyncBrokerAdapter() # DEĞİŞTİ

@router.post("/", response_model=OrderResponse, status_code=201)
async def create_order(order: OrderCreate):
    """
    ==========================================
    ASENKRON BÜYÜSÜNÜN OLDUĞU YER
    ==========================================
    Kullanıcı sipariş verdiğinde çalışır. Siparişi veritabanına kaydeder ve 
    asıl uzun süren işi (fatura/kargo işlemi) RabbitMQ aracılığıyla Celery'ye fırlatır.
    Bu sayede müşteri 10 saniye beklemeden ANINDA (saliseler içinde) "Siparişiniz alındı" cevabını görür!
    """
    # 1. Siparişi Veritabanına kaydet (Durumu otomatik olarak PENDING/Beklemede olur)
    new_order = db_adapter.create_order(order)
    
    # 2. Sipariş ID'sini arka plan işçisine (Celery) fırlat ve unut.
    broker_adapter.send_order_processing_task(new_order.id)
    
    # 3. Müşteriye hemen siparişin alındığı bilgisini dön
    return new_order

@router.get("/{order_id}", response_model=OrderResponse)
async def get_order_status(order_id: int):
    """Siparişin o anki güncel durumunu sorgular."""
    order = db_adapter.get_order_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Sipariş bulunamadı.")
    return order
