# Python Backend Geliştirme Yol Haritası (10 Adım)

Bu yol haritası, Python ile backend geliştirme becerilerini sıfırdan ileri seviyeye taşımak için tasarlanmıştır. Projeler basitten zora doğru ilerlerken, farklı mimari yaklaşımları (Monolitik, N-Katmanlı, Clean Architecture) ve farklı veritabanlarını (SQLite, PostgreSQL, MongoDB, Redis) kapsayacaktır. Frontend (UI) tarafı basitçe entegre edilecek veya tamamen API tabanlı ilerlenip test edilecektir. Görsel/dosya yükleme işlemleri hariç tutulmuş, tamamen metin tabanlı veri yönetimi odaklanmıştır.

---

## 1. Proje: Basit Portfolio API (Temel CRUD)
* **Amaç:** Temel yönlendirme (routing) ve CRUD işlemlerini kavramak.
* **Teknoloji:** FastAPI (veya Flask), SQLite.
* **Mimari:** 1 Katmanlı (Single-file / Monolitik) - Tüm kodlar tek/birkaç dosyada.
* **İçerik:** Kendi yeteneklerimizi, deneyimlerimizi ve projelerimizi (sadece metin tabanlı: proje adı, açıklaması, linki) ekleyip silebileceğimiz, güncelleyebileceğimiz basit bir API.

## 2. Proje: Gelişmiş Portfolio API (N-Katmanlı Mimari & Yetkilendirme)
* **Amaç:** Proje 1'i alıp profesyonel bir yapıya dönüştürmek, yetkilendirme eklemek.
* **Teknoloji:** FastAPI, PostgreSQL.
* **Mimari:** N-Katmanlı (Router -> Service -> Repository).
* **İçerik:** Portfolyo verilerini sadece yetkili kullanıcıların (Admin) değiştirebilmesi için JWT (JSON Web Token) tabanlı giriş sistemi. Veri doğrulama (Validation) işlemleri. Veritabanının PostgreSQL'e taşınması.

## 3. Proje: Görev Yönetim Sistemi (Django'ya Giriş)
* **Amaç:** Django framework'ü ve ORM (Object-Relational Mapping) yapısıyla tanışmak.
* **Teknoloji:** Django, Django REST Framework (DRF), SQLite.
* **Mimari:** Django MTV (Model-Template-View) / MVT.
* **İçerik:** Kullanıcıların kendi "To-Do" listelerini oluşturabildiği, görevleri tamamlandı olarak işaretleyebildiği bir API. Django'nun hazır Admin paneli ile tanışma.

## 4. Proje: Blog Platformu (İlişkisel Veritabanı Uzmanlığı)
* **Amaç:** Karmaşık veritabanı ilişkileri (One-to-Many, Many-to-Many) kurmak.
* **Teknoloji:** Django, DRF, PostgreSQL.
* **Mimari:** N-Katmanlı (App tabanlı modüler yapı).
* **İçerik:** Yazarlar, kategoriler, etiketler (tags) ve metin tabanlı blog yazıları. Yorum yapma sistemi. Sayfalama (Pagination) ve arama/filtreleme özellikleri.

## 5. Proje: E-Ticaret Ürün Kataloğu (NoSQL'e Giriş)
* **Amaç:** İlişkisel olmayan (NoSQL) veritabanı mantığını anlamak.
* **Teknoloji:** FastAPI, MongoDB.
* **Mimari:** Repository Pattern.
* **İçerik:** Kategoriler ve dinamik özelliklere (farklı ürünlerin farklı metin tabanlı özellikleri olabilir) sahip ürünlerin tutulduğu bir katalog API'si.

## 6. Proje: Sipariş Yönetim Sistemi (Arka Plan Görevleri)
* **Amaç:** Asenkron işlemler ve Message Broker (Mesaj Kuyruğu) kullanımı.
* **Teknoloji:** FastAPI, PostgreSQL, Celery, RabbitMQ.
* **Mimari:** Hexagonal Architecture (Ports & Adapters) temelleri.
* **İçerik:** Kullanıcının metin tabanlı sipariş oluşturması. Siparişin "İşleniyor", "Kargoya Verildi" gibi durumlarının asenkron arka plan görevleriyle (Celery) güncellenmesi ve e-posta (simülasyon) gönderimi.

## 7. Proje: Gerçek Zamanlı Bildirim Servisi
* **Amaç:** WebSockets ve gerçek zamanlı (Real-time) veri akışı.
* **Teknoloji:** FastAPI, Redis (Pub/Sub).
* **Mimari:** Event-Driven (Olay Güdümlü) Mimari.
* **İçerik:** Sistemde bir olay olduğunda (örneğin yeni bir duyuru yayınlandığında) bağlı olan tüm istemcilere (kullanıcılara) anında metin tabanlı bildirim gönderen servis.

## 8. Proje: Analitik ve Loglama API'si (Performans)
* **Amaç:** Yüksek veri yazma/okuma senaryolarını yönetmek.
* **Teknoloji:** Flask (veya FastAPI), TimescaleDB (veya gelişmiş PostgreSQL).
* **Mimari:** CQRS (Command Query Responsibility Segregation) - Okuma ve yazma işlemlerinin ayrılması.
* **İçerik:** Diğer sistemlerden gelen log kayıtlarını (hangi API uç noktasına ne zaman erişildi vb.) toplayan ve belirli tarih aralıklarında istatistik veren bir servis.

## 9. Proje: Rezervasyon ve Randevu Sistemi (Clean Architecture)
* **Amaç:** Karmaşık iş mantığını ve veritabanı transaction (işlem) yönetimini kurumsal standartlarda çözmek.
* **Teknoloji:** Django (veya FastAPI), PostgreSQL.
* **Mimari:** Clean Architecture (Domain, Use Cases, Interfaces, Infrastructure).
* **İçerik:** Çakışan saatlerde randevu alınmasını engelleyen, Race Condition (yarış durumu) senaryolarına karşı kilit (lock) mekanizmaları barındıran gelişmiş bir rezervasyon API'si.

## 10. Proje: Mikroservis Ekosistemi
* **Amaç:** Farklı servisleri birbirine bağlamak ve konteyner orkestrasyonu (temel).
* **Teknoloji:** Önceki projelerin birleşimi (Örn: Proje 2, Proje 6 ve Proje 7), Docker, API Gateway.
* **Mimari:** Microservices Architecture.
* **İçerik:** Yetkilendirme servisi (Proje 2), sipariş servisi (Proje 6) ve bildirim servisini (Proje 7) bir araya getirip tek bir ağ üzerinden konuşturan, API Gateway üzerinden yönlendirmelerin yapıldığı final projesi.

---

## Çalışma Prensibimiz
1. **Adım Adım Geliştirme:** Her proje için önce plan yapacağız, sonra kodlayacağız.
2. **Frontend:** İhtiyaç duyulan noktalarda senin için basit HTML/JS arayüzlerini ben (AI) yazacağım veya doğrudan Postman/Swagger (API dökümantasyonu) üzerinden ilerleyeceğiz.
3. **Odak Noktası:** Dosya yükleme gibi işler yok; tamamen iş mantığı (business logic), mimari tasarım, veri güvenliği ve algoritma üzerine yoğunlaşacağız.
4. **Çalışma Alanı:** Tüm projeler `python_tutorial_master` klasörü içerisinde ayrı alt klasörlerde profesyonel bir düzende tutulacak.

İlk projemiz olan **Portfolio Projesi (Basit CRUD)** ile başlamak için hazır olduğunda bana bildirmen yeterli!
