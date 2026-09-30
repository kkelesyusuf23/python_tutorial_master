from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# SEBEP: Views tarafında ModelViewSet kullandığımız için her bir işlemi (GET, POST vs.) tek tek yollara bağlamak zorunda değiliz.
# DRF'nin "DefaultRouter" yapısı, verdiğimiz "tasks" kelimesinden yola çıkarak;
# - GET /tasks/ (Listeleme)
# - POST /tasks/ (Ekleme)
# - GET /tasks/5/ (5 Numaralıyı Görme)
# - PUT /tasks/5/ (Güncelleme)
# - DELETE /tasks/5/ (Silme)
# Tüm bu URL yollarını bizim yerimize otomatik olarak arkada oluşturur.

router = DefaultRouter()
router.register(r'tasks', TaskViewSet) # "tasks" adında bir yol oluşturduk ve bunu TaskViewSet (Aşçı) sınıfına bağladık.

urlpatterns = [
    # SEBEP: Router'ın ürettiği bu otomatik yolların hepsini (URLs) uygulamamızın ana yol haritasına ekliyoruz.
    path('', include(router.urls)),
]
