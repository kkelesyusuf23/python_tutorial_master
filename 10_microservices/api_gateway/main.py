from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

app = FastAPI(
    title="API Gateway (Ağ Geçidi)", 
    description="Müşterinin tek muhatabı. Mikroservis orkestra şefi.",
    version="1.0.0"
)

# Mikroservislerimizin çalıştığı adresler (Gerçek hayatta farklı sunucu IP'leri olur)
AUTH_URL = "http://127.0.0.1:8001"
ORDER_URL = "http://127.0.0.1:8002"
NOTIFICATION_URL = "http://127.0.0.1:8003"

class CheckoutRequest(BaseModel):
    token: str
    product_id: int
    quantity: int

@app.post("/checkout")
async def checkout(data: CheckoutRequest):
    """
    ==========================================
    API GATEWAY (PORT 8000) - ORKESTRA ŞEFİ
    ==========================================
    Müşteri arkada 3 farklı sunucu olduğunu BİLMEZ. O sadece Gateway'e tek bir 
    "Satın Al" (Checkout) isteği atar. Kalan tüm iletişimi Gateway (httpx ile) yönetir.
    """
    
    # 1. ADIM: Kimlik Doğrulama Servisine Git (Port 8001)
    async with httpx.AsyncClient() as client:
        auth_response = await client.post(f"{AUTH_URL}/verify-token", json={"token": data.token})
        
        if auth_response.status_code != 200:
            raise HTTPException(status_code=401, detail="Gateway Uyarısı: Müşteri kimliği doğrulanamadı, işlem iptal edildi!")
        
        user_id = auth_response.json()["user_id"]

    # 2. ADIM: Kimlik doğruysa Sipariş Servisine Git (Port 8002)
    async with httpx.AsyncClient() as client:
        order_response = await client.post(
            f"{ORDER_URL}/create-order", 
            json={"user_id": user_id, "product_id": data.product_id, "quantity": data.quantity}
        )
        order_id = order_response.json()["order_id"]

    # 3. ADIM: Sipariş de kaydedildiyse Bildirim Servisine Git (Port 8003)
    async with httpx.AsyncClient() as client:
        await client.post(
            f"{NOTIFICATION_URL}/send-email", 
            json={
                "user_id": user_id, 
                "message": f"Tebrikler! {order_id} numaralı siparişiniz başarıyla alındı ve hazırlanıyor."
            }
        )

    # 4. ADIM: Her şey bittiğinde Müşteriye (Frontend'e) Tek Bir Cevap Dön!
    return {
        "status": "success", 
        "message": "Satın alma işlemi başarıyla tamamlandı!",
        "order_id": order_id
    }
