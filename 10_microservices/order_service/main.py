from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI(title="Order Microservice", version="1.0.0", docs_url=None, redoc_url=None)

class OrderRequest(BaseModel):
    user_id: int
    product_id: int
    quantity: int

@app.post("/create-order")
def create_order(order: OrderRequest):
    """
    ==========================================
    ORDER MİKROSERVİSİ (PORT 8002)
    ==========================================
    Bu servisin dünyadaki TEK görevi gelen siparişi veritabanına kaydetmektir.
    "Bu kullanıcının yetkisi var mı?" diye sormaz, o iş Auth servisinin (8001) sorunudur.
    """
    order_id = random.randint(1000, 9999)
    print(f"[ORDER DB] Sipariş Veritabanına Kaydedildi! Sipariş ID: {order_id} | Ürün ID: {order.product_id}")
    
    return {"status": "success", "order_id": order_id}
