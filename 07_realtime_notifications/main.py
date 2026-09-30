from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from pydantic import BaseModel
from connection_manager import manager

app = FastAPI(
    title="Gerçek Zamanlı Bildirimler",
    description="WebSockets ve Pub/Sub mantığı ile anlık iletişim sağlayan servis.",
    version="1.0.0",
)

# HTML arayüzlerimizin (Frontend) bulunduğu klasör
templates = Jinja2Templates(directory="templates")

class Announcement(BaseModel):
    message: str

# ==========================================
# 1. UÇ NOKTA: MÜŞTERİ GİRİŞİ (FRONTEND)
# ==========================================
@app.get("/")
async def get_frontend(request: Request):
    """Müşterinin siteye ilk girdiği an (Sadece HTML arayüzünü verir)"""
    return templates.TemplateResponse("index.html", {"request": request})

# ==========================================
# 2. UÇ NOKTA: GERÇEK ZAMANLI KANAL (WEBSOCKET)
# ==========================================
@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    """Müşterinin arka kapıdan bağlandığı ve sürekli açık kalan canlı kanal"""
    # Müşteriyi aktif bağlantılar havuzuna (Pub/Sub) alıyoruz
    await manager.connect(websocket)
    try:
        # Bağlantı açık kaldığı sürece sonsuz bir döngüde dinleme yapılır
        while True:
            # WebSocket Çift Yönlüdür (Müşteri de bize mesaj atabilir, ancak biz sadece yayın mantığı kuruyoruz)
            data = await websocket.receive_text()
    except WebSocketDisconnect:
        # Müşteri sekmeyi kapattığında veya interneti gittiğinde onu havuzdan çıkartıyoruz
        manager.disconnect(websocket)

# ==========================================
# 3. UÇ NOKTA: PATRON/SİSTEM TUŞU (BROADCAST)
# ==========================================
@app.post("/announce")
async def announce_message(announcement: Announcement):
    """
    Şirket yöneticisinin (veya sistemin) dışarıdan sisteme olay gönderdiği uç nokta.
    Buraya gelen her bildirim (JSON), saniyesinde aktif olan TÜM müşterilere fırlatılır!
    """
    # Tek bir satır kodla, sistemdeki binlerce müşteriye aynı anda (Real-time) ulaşıyoruz
    await manager.broadcast(announcement.message)
    return {"status": "success", "message": f"'{announcement.message}' duyurusu tüm kullanıcılara gönderildi!"}
