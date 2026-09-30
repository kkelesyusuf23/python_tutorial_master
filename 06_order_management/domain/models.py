import enum
from sqlalchemy import Column, Integer, String, Float, Enum
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# SEBEP: Siparişin alabileceği sadece belirli durumlar vardır. 
# Kullanıcı veya sistem kafasına göre "Sipariş Yolda" yazamasın, 
# sadece bizim belirlediğimiz bu 4 durumu (Enum) kullanabilsin diye kısıtlıyoruz.
class OrderStatus(str, enum.Enum):
    PENDING = "Beklemede"
    PROCESSING = "İşleniyor"
    SHIPPED = "Kargolandı"
    DELIVERED = "Teslim Edildi"

# ==========================================
# DOMAIN (ÇEKİRDEK) KATMANI - MODELLER
# ==========================================
# SEBEP: Hexagonal mimaride Domain katmanı projenin kalbidir. 
# Sipariş nedir? Hangi alanları vardır? Burada tanımlanır.
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, index=True)
    total_amount = Column(Float)
    
    # Sipariş ilk oluşturulduğunda varsayılan olarak "Beklemede" statüsünde başlar.
    status = Column(Enum(OrderStatus), default=OrderStatus.PENDING)
