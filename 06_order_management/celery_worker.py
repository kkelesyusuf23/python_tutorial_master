import time
from celery import Celery
from domain.models import OrderStatus
from adapters.database_adapter import SqliteDatabaseAdapter

# Docker üzerinde kurduğumuz RabbitMQ sunucusuna bağlanıyoruz (AMQP protokolü)
celery_app = Celery(
    "order_tasks",
    broker="amqp://guest:guest@localhost:5672//",
)

@celery_app.task
def process_order_task(order_id: int):
    """
    ==========================================
    ARKA PLAN İŞÇİSİ (BACKGROUND TASK)
    ==========================================
    SEBEP: Eğer bu fonksiyonu doğrudan API içine yazsaydık, müşteri siparişi verdikten 
    sonra ekranda 10 saniye boş boş "Yükleniyor..." ikonunu bekleyecekti.
    Ancak bu fonksiyon Celery ile arka planda API'den tamamen bağımsız çalışır.
    """
    db_adapter = SqliteDatabaseAdapter()
    
    order = db_adapter.get_order_by_id(order_id)
    if not order:
        return "Sipariş bulunamadı"

    print(f"[{order_id}] Numaralı Sipariş İşleniyor... (Fatura Kesiliyor)")
    order.status = OrderStatus.PROCESSING
    db_adapter.db.commit()
    
    # E-posta gönderme veya Kargo firmasıyla iletişime geçme SİMÜLASYONU (10 Saniye sürsün)
    time.sleep(10)
    
    print(f"[{order_id}] Numaralı Sipariş Kargoya Verildi!")
    order.status = OrderStatus.SHIPPED
    db_adapter.db.commit()
    
    return f"Sipariş {order_id} başarıyla kargolandı!"
