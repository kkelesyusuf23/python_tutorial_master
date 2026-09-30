# Proje 2: Gelişmiş Portfolio API (N-Katmanlı Mimari & JWT)

Bu projede amacımız, ilk projedeki tek katmanlı (Monolitik) yapıyı parçalayarak kodumuzu kurumsal standartlara (N-Tier Architecture) uygun hale getirmek ve **JWT (JSON Web Token)** ile güvenliği sağlamaktır.

## 📌 Yapılacaklar Listesi

- [ ] Yeni klasör (`02_advanced_portfolio`) ve sanal ortamın (`venv`) oluşturulması.
- [ ] Gerekli kütüphanelerin sanal ortama kurulması (FastAPI, SQLAlchemy, Uvicorn, passlib, python-jose, python-multipart).
- [ ] `database.py` dosyasının yazılması (Veritabanı bağlantı ayarları - Infrastructure).
- [ ] `models.py` dosyasının oluşturulması (`User` ve `Project` tabloları - Domain).
- [ ] `schemas.py` dosyasının oluşturulması (Gelen/Giden veriyi doğrulayacak Pydantic yapıları).
- [ ] `core/security.py` dosyasının oluşturulması (Şifre hash'leme, JWT Token üretme ve doğrulama ayarları).
- [ ] `services/` klasörünün oluşturulması ve içine veritabanı sorgularının yazılacağı dosyaların (`auth_service.py`, `project_service.py`) eklenmesi.
- [ ] `routers/` klasörünün oluşturulması ve API uç noktalarının (`auth.py`, `projects.py`) eklenmesi.
- [ ] `main.py` dosyasının oluşturulması ve tüm router'ların ana uygulamaya bağlanması.
- [ ] Token alarak sisteme giriş (Login) işleminin test edilmesi.
- [ ] Token ile yetkilendirme gerektiren uç noktaların (CREATE, UPDATE, DELETE) test edilmesi.

## 💡 İpuçları (Tricks)
* **N-Katmanlı Mimari:** Bu yapıda `main.py` dosyası hiçbir iş mantığı (business logic) içermez. Sadece ayarları yapar ve trafiği `routers/` klasörüne yönlendirir. `routers/` sadece isteği karşılar ve veriyi işlemek için `services/` klasörüne gönderir.
* **JWT (JSON Web Token):** Kullanıcı giriş yaptığında (kullanıcı adı ve şifre ile) ona bir "Token" (bilet) veririz. Kullanıcı, veri eklemek veya silmek istediğinde bu bileti bize göstermek zorundadır. Aksi takdirde API onu içeri almaz (401 Unauthorized).
* **Güvenlik:** Veritabanında şifreleri asla düz metin (plain text) olarak saklamayız. `passlib` kütüphanesi ile şifreleri "hash"leyerek (karmaşıklaştırarak) saklayacağız.
