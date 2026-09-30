from abc import ABC, abstractmethod
from domain.schemas import OrderCreate
from domain.models import Order

# ==========================================
# PORTS (LİMANLAR) - VERİTABANI SÖZLEŞMESİ
# ==========================================
# SEBEP: Hexagonal Mimaride 'Port' bir sözleşmedir (Interface / Abstract Class).
# Uygulamanın kalbi (Domain) der ki: "Benim çalışabilmem için bana 
# 'create_order' ve 'get_order_by_id' yetenekleri olan bir sistem verin."
# Bu sınıfın içi boştur (pass), sadece kuralları belirler. Gerçek kaydetme işini 'Adapters' (Adaptörler) yapacak.

class DatabasePort(ABC):
    @abstractmethod
    def create_order(self, order_data: OrderCreate) -> Order:
        pass

    @abstractmethod
    def get_order_by_id(self, order_id: int) -> Order:
        pass
