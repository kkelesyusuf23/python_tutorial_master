from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

# Önceki projede olduğu gibi, DRF'nin otomatik yönlendiricisini (Router) kullanıyoruz.
router = DefaultRouter()

# "posts" adında bir yol oluşturduk ve bunu PostViewSet aşçısına bağladık.
# Bu sayede GET /posts, POST /posts, GET /posts/5 vb. tüm yollar otomatik oluştu.
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
