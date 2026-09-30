import asyncio
from domain.models import OrderStatus
from adapters.database_adapter import SqliteDatabaseAdapter

async def process_order_task(order_id: int):
    """
    ==========================================
    ARKA PLAN İŞÇİSİ (FASTAPI ASYNC)
    ==========================================
    Celery yerine Python'un kendi asenkron yapısını (asyncio) kullanarak
    arka plan görevi oluşturduk. 
    """
    # Kendi bağımsız veritabanı bağlantımızı açıyoruz
    db_adapter = SqliteDatabaseAdapter()
    
    order = db_adapter.get_order_by_id(order_id)
    if not order:
        return

    print(f"[{order_id}] Numaralı Sipariş İşleniyor... (Fatura Kesiliyor)")
    order.status = OrderStatus.PROCESSING
    db_adapter.db.commit()
    
    # E-posta gönderme veya Kargo firmasıyla iletişime geçme SİMÜLASYONU (10 Saniye)
    # NOT: time.sleep yerine asenkron await asyncio.sleep kullanıyoruz ki sunucu donmasın.
    await asyncio.sleep(10)
    
    print(f"[{order_id}] Numaralı Sipariş Kargoya Verildi!")
    order.status = OrderStatus.SHIPPED
    db_adapter.db.commit()
