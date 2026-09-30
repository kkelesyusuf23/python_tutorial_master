from motor.motor_asyncio import AsyncIOMotorClient

# SEBEP: Docker üzerinde ayağa kaldırdığımız MongoDB varsayılan olarak localhost'ta 27017 portunu dinler.
MONGO_URL = "mongodb://localhost:27017"

# Uygulama boyunca MongoDB'ye istek atacak olan ana istemcimiz (Client)
client = AsyncIOMotorClient(MONGO_URL)

# "ecommerce_db" adında bir veritabanına (Database) bağlanıyoruz.
# NOT: SQL dünyasının aksine NoSQL'de veritabanını önceden bir panelden oluşturmamıza gerek yoktur.
# Sisteme ilk ürünü (JSON) gönderdiğimiz an MongoDB bu veritabanını otomatik olarak kendisi açacaktır!
database = client.ecommerce_db
