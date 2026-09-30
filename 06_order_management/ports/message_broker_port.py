from abc import ABC, abstractmethod

# ==========================================
# PORTS (LİMANLAR) - MESAJ KUYRUĞU SÖZLEŞMESİ
# ==========================================
# SEBEP: Sipariş alındığında arka plan görevini (Celery) tetikleyecek sözleşmemiz.
# Eğer yarın patron gelip "RabbitMQ çok eskidi, artık Kafka (veya AWS SQS) kullanacağız" derse,
# sistemin kalbi sadece bu sözleşmeyi ("send_order_processing_task") tanıdığı için 
# çekirdek kodlarımızda hiçbir değişiklik yapmamıza gerek kalmayacak!

class MessageBrokerPort(ABC):
    @abstractmethod
    def send_order_processing_task(self, order_id: int) -> None:
        pass
