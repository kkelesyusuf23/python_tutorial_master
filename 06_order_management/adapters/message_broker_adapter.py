import asyncio
from ports.message_broker_port import MessageBrokerPort
from adapters.background_worker import process_order_task

# ==========================================
# ADAPTERS - ASYNC (GÖMÜLÜ) ADAPTÖR
# ==========================================
# SEBEP: Mimarimizin (Ports & Adapters) gücüne bak! 
# RabbitMQ kuramadığımız için sistemin çekirdeğini hiç bozmadan
# sadece "Adaptörü" değiştirdik. Artık Celery yerine asyncio kullanıyoruz.

class AsyncBrokerAdapter(MessageBrokerPort):
    def send_order_processing_task(self, order_id: int) -> None:
        # create_task() komutu, fonksiyonu arka planda başlatır ve
        # bitmesini beklemeden (API'yi dondurmadan) hemen yola devam eder.
        asyncio.create_task(process_order_task(order_id))
