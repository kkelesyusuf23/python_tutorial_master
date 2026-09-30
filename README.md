# Python Backend Masterclass 🚀

Bu repo, Python ile backend geliştirme becerilerini sıfırdan ileri seviyeye taşımak amacıyla geliştirilmiş **10 farklı projeyi** içermektedir. Projeler basitten karmaşığa doğru ilerlerken, sektörde dev şirketlerin kullandığı modern mimarileri (Clean Architecture, Microservices, CQRS) ve teknolojileri kapsayacak şekilde tasarlanmıştır.

## 🛠️ Kullanılan Teknolojiler ve Kavramlar
- **Frameworks:** FastAPI, Django, Django REST Framework (DRF)
- **Veritabanları:** SQLite, PostgreSQL, MongoDB (NoSQL)
- **Mimariler:** Monolithic, N-Tier (Çok Katmanlı), Hexagonal (Ports & Adapters), Clean Architecture, CQRS, Microservices, Event-Driven
- **Kavramlar:** JWT Authentication, Background Tasks, WebSockets (Real-time Pub/Sub), API Gateway, Race Conditions, ORM & ODM.

---

## 📁 Projeler ve Klasör Yapısı

### [01] Portfolio API (Temel CRUD)
- **Mimari:** Monolitik (Tek Dosya)
- **Özet:** FastAPI ve SQLite kullanılarak geliştirilmiş, temel yönlendirme (routing) ve CRUD işlemlerini öğreten başlangıç seviyesi API.

### [02] Gelişmiş Portfolio API (N-Katmanlı Mimari)
- **Mimari:** N-Katmanlı (Router -> Service -> Repository)
- **Özet:** İlk projenin profesyonel bir klasör yapısına taşınmış hali. JWT (JSON Web Token) ile yetkilendirme ve PostgreSQL entegrasyonu barındırır.

### [03] Görev Yönetim Sistemi (Django'ya Giriş)
- **Mimari:** MTV (Model-Template-View)
- **Özet:** Django ve DRF dünyasına giriş. Kullanıcıların görev listelerini yönettiği ve otomatik Django Admin panelinin kullanıldığı REST API.

### [04] Blog Platformu (İlişkisel Veritabanı)
- **Mimari:** Modüler Django (App tabanlı)
- **Özet:** One-to-Many ve Many-to-Many gibi karmaşık veritabanı ilişkilerini içeren; yazarlar, etiketler ve yorum sistemlerini barındıran gelişmiş blog API'si.

### [05] E-Ticaret Ürün Kataloğu (NoSQL)
- **Mimari:** Repository Pattern
- **Özet:** İlişkisel olmayan (NoSQL) veri tabanı mantığına geçiş. FastAPI ve MongoDB kullanılarak esnek ürün özelliklerinin yönetildiği şemasız (schema-less) katalog servisi.

### [06] Sipariş Yönetim Sistemi (Arka Plan Görevleri)
- **Mimari:** Hexagonal Architecture (Ports & Adapters)
- **Özet:** Sistemin çekirdek iş kurallarının dış dünyadan izole edildiği, fatura ve kargo gibi ağır işlemlerin API'yi dondurmadan asenkron arka plan görevleriyle işlendiği sistem.

### [07] Gerçek Zamanlı Bildirim Servisi (WebSockets)
- **Mimari:** Event-Driven (Olay Güdümlü)
- **Özet:** HTTP'nin sınırlarını aşarak WebSockets üzerinden sürekli açık kalan bağlantılar (Pub/Sub) ile müşterilere anlık (Real-time) duyuruların itildiği (Push) bildirim servisi.

### [08] Analitik ve Loglama API'si (CQRS)
- **Mimari:** CQRS (Command Query Responsibility Segregation)
- **Özet:** Yüksek performans gerektiren sistemler için okuma (Query) ve yazma (Command) işlemlerinin, kod ve mantık seviyesinde ikiye bölündüğü analitik altyapısı.

### [09] Rezervasyon ve Randevu Sistemi (Clean Architecture)
- **Mimari:** Clean Architecture
- **Özet:** Yazılım mühendisliğinin zirvesi kabul edilen bu mimariyle, "Race Condition" (Yarış Durumu - Aynı saate randevu alma çakışması) problemlerinin çözüldüğü ve tüm kodun bağımsız halkalara ayrıldığı randevu sistemi.

### [10] Mikroservis Ekosistemi & API Gateway (Final)
- **Mimari:** Microservices Architecture
- **Özet:** Monolitik yapıların tamamen parçalanarak; Kimlik Doğrulama, Sipariş ve Bildirim işlemlerinin ayrı portlarda çalışan bağımsız sunuculara (servislere) dönüştürüldüğü büyük final projesi. Tüm mikroservisler, dışarıya tek bir kapıdan (API Gateway) `httpx` aracılığıyla orkestre edilerek sunulur.

---
*Bu repo, sıfırdan profesyonel backend mimarisine uzanan yoğun bir eğitim serüveninin ürünüdür.*
