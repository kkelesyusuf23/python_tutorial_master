from fastapi import APIRouter
from typing import List
from schemas import ProductCreate, ProductResponse
from repositories.product_repository import ProductRepository

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=List[ProductResponse])
async def read_products():
    """Sistemdeki (veritabanındaki) tüm ürünleri listeler."""
    # ==========================================
    # KUSURSUZ İZOLASYON (SOYUTLAMA)
    # ==========================================
    # SEBEP: Router'ın koduna bak! İçinde hiçbir yerde "mongo", "find()", "db" gibi 
    # veritabanına ait kelimeler göremezsin. Garson sadece Depo Görevlisini (Repository) çağırır.
    return await ProductRepository.get_all_products()

@router.post("/", response_model=ProductResponse, status_code=201)
async def create_product(product: ProductCreate):
    """Yeni bir ürünü, o ürüne has dinamik özelliklerle (attributes) birlikte kaydeder."""
    return await ProductRepository.create_product(product)
