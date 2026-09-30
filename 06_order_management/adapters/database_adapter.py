from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from domain.models import Order, Base
from domain.schemas import OrderCreate
from ports.database_port import DatabasePort

# SQLite Bağlantı Ayarları
SQLALCHEMY_DATABASE_URL = "sqlite:///./orders.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ==========================================
# ADAPTERS - GERÇEK VERİTABANI BAĞLANTISI
# ==========================================
# SEBEP: Bu sınıf, Ports klasöründeki 'DatabasePort' sözleşmesini imzalar (miras alır).
# O sözleşmedeki içi boş kuralların içini, burada gerçek SQLite/SQLAlchemy kodlarıyla dolduruyoruz.

class SqliteDatabaseAdapter(DatabasePort):
    def __init__(self):
        self.db = SessionLocal()

    def create_order(self, order_data: OrderCreate) -> Order:
        db_order = Order(
            customer_name=order_data.customer_name,
            total_amount=order_data.total_amount
        )
        self.db.add(db_order)
        self.db.commit()
        self.db.refresh(db_order)
        return db_order

    def get_order_by_id(self, order_id: int) -> Order:
        return self.db.query(Order).filter(Order.id == order_id).first()
