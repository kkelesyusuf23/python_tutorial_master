from bson import ObjectId
from database import database
from schemas import ProductCreate

# MongoDB'deki "products" koleksiyonunu (SQL'deki tablonun karşılığı) seçiyoruz
product_collection = database.get_collection("products")

class ProductRepository:
    """
    ==========================================
    REPOSITORY PATTERN (DEPO KALIBI) MANTIĞI
    ==========================================
    SEBEP: Bu sınıfın hayattaki tek bir görevi vardır: Veritabanı ile konuşmak!
    Uygulamanın geri kalanı (Router'lar, Garsonlar) MongoDB kullanıldığını kesinlikle bilmez.
    Router sadece "Bana ürünleri getir" der, burası gider MongoDB'den getirir.
    
    Eğer yarın patron "MongoDB çok pahalı, PostgreSQL'e dönüyoruz" derse, 
    sistemdeki hiçbir yeri (Router'ları vs.) ellemeyiz! Sadece gelir buradaki 
    sorgu kodlarını SQL kodlarıyla değiştiririz. Sistemin çökmesini engelleriz.
    """
    
    @staticmethod
    async def get_all_products():
        # Asenkron (async/await) hızından faydalanıp 100 ürünü anında çekiyoruz.
        products = await product_collection.find().to_list(100)
        
        # MongoDB kendi içindeki ID'leri "_id" (ObjectId) olarak tutar.
        # Biz bunu Pydantic şemamıza uygun olsun diye "id" (str) şekline çeviriyoruz.
        for product in products:
            product["id"] = str(product["_id"])
        return products

    @staticmethod
    async def create_product(product_data: ProductCreate):
        # Router'dan gelen Pydantic verisini Dictionary (Sözlük) haline getirip veritabanına atıyoruz.
        product_dict = product_data.model_dump()
        result = await product_collection.insert_one(product_dict)
        
        # Kaydedilen veriyi, oluşan eşsiz ID'si ile birlikte geri çekiyoruz.
        created_product = await product_collection.find_one({"_id": result.inserted_id})
        created_product["id"] = str(created_product["_id"])
        return created_product
