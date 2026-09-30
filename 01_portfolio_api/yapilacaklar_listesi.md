# Proje 1: Portfolio API (Temel CRUD)

Bu projede amacımız en temel haliyle bir API ayağa kaldırmak ve yönlendirme (routing) ile veritabanı (SQLite) işlemlerini tek bir yapıda halletmektir. Bu sayede "1 Katmanlı Mimari" mantığını kavrayacağız.

## 📌 Yapılacaklar Listesi

- [ ] Gerekli kütüphanelerin sanal ortama (virtual environment) kurulması (FastAPI, Uvicorn, SQLAlchemy).
- [ ] `main.py` dosyasının oluşturulması ve FastAPI uygulamasının basit bir "Hello World" ile başlatılması.
- [ ] SQLite veritabanı bağlantısının kurulması ve modelin (ör. `Project` modeli) oluşturulması.
- [ ] Gelen verilerin doğrulanması için Pydantic şemalarının yazılması.
- [ ] **C**REATE: Yeni bir portfolyo öğesi ekleme API ucu (`POST /projects`)
- [ ] **R**EAD: Tüm portfolyo öğelerini listeleme (`GET /projects`) ve tek bir öğeyi getirme (`GET /projects/{id}`)
- [ ] **U**PDATE: Mevcut bir öğeyi güncelleme (`PUT /projects/{id}`)
- [ ] **D**ELETE: Bir öğeyi silme (`DELETE /projects/{id}`)
- [ ] Swagger üzerinden tüm uç noktaların test edilmesi.

## 💡 İpuçları (Tricks)
* **FastAPI Swagger:** FastAPI bizim için otomatik arayüz oluşturur. Uygulama çalıştıktan sonra tarayıcıda `http://127.0.0.1:8000/docs` adresine giderek API'mizi frontend yazmaya gerek kalmadan görsel bir arayüzden test edebileceğiz.
* **Neden her şey tek dosyada?** Tüm routing ve veritabanı işlemlerini başlangıçta `main.py` içine yazacağız. Bu bize başlangıçta kolaylık sağlasa da kod büyüdükçe yönetilmesi zorlaşacaktır. 2. Projede bu sorunu çözmek için katmanlı yapıya geçeceğiz; bu projede acıyı yaşayıp, diğerinde ilacını göreceğiz.
* **Sanal Ortam (Venv):** Projelerimizin bağımlılıklarının çakışmaması için her projede bir sanal ortam oluşturmak best-practice'dir (en iyi pratik).
