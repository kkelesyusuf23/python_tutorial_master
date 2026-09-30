from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Notification Microservice", version="1.0.0", docs_url=None, redoc_url=None)

class NotificationRequest(BaseModel):
    user_id: int
    message: str

@app.post("/send-email")
def send_email(notification: NotificationRequest):
    """
    ==========================================
    NOTIFICATION MİKROSERVİSİ (PORT 8003)
    ==========================================
    Bu servisin dünyadaki TEK görevi kendisine verilen mesajı müşteriye mail atmaktır.
    Sipariş kaydedildi mi, kullanıcı giriş yaptı mı asla umursamaz.
    """
    print(f"\n[EMAIL SUNUCUSU] Müşteri #{notification.user_id} numaralı kişiye E-Posta gönderiliyor...")
    print(f"[EMAIL İÇERİĞİ] {notification.message}\n")
    
    return {"status": "success", "message": "E-Posta başarıyla gönderildi!"}
