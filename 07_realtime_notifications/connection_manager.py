from fastapi import WebSocket
from typing import List

class ConnectionManager:
    """
    ==========================================
    YAYIN (BROADCAST) VE ABONELİK (PUB/SUB) YÖNETİCİSİ
    ==========================================
    SEBEP: WebSocket bağlantıları HTTP gibi cevap verip kapanmaz, sürekli açık kalır. 
    Eğer sisteme 5 müşteri bağlanırsa, bu 5 müşterinin bağlantı adreslerini (WebSocket objelerini) 
    bir listede (hafızada) tutmalıyız ki, sistemden bir duyuru geçtiğinde hepsine tek tek ulaşabilelim.
    """
    def __init__(self):
        # Aktif bağlantıları (müşterileri) tutacağımız havuz (Memory)
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        # Müşteri bağlandığında önce bağlantıyı (Handshake) kabul et, sonra havuza ekle
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        # Müşteri tarayıcıyı kapattığında veya interneti koptuğunda onu havuzdan sil (Hata vermemesi için)
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        # Sistemde bir olay olduğunda (Örn: Yönetici indirim başlattığında), 
        # havuzdaki tüm müşterilere aynı anda (Real-time) mesajı gönder!
        for connection in self.active_connections:
            await connection.send_text(message)

# Uygulama genelinde kullanılacak tek bir yönetici nesnesi oluşturuyoruz
manager = ConnectionManager()
