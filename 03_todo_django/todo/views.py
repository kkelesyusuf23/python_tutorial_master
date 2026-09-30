from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

# SEBEP: FastAPI'da her uç noktayı (@app.get, @app.post, @app.put vb.) tek tek uzun uzun elimizle yazıyorduk.
# Django REST Framework'ün (DRF) yazılımcılara sunduğu en büyük sihirlerden biri "ModelViewSet" sınıfıdır.
# Sadece hangi tablonun kullanılacağını (queryset) ve hangi doğrulayıcının (serializer_class) çalışacağını söylersin,
# DRF arka planda listeleme, detay görme, ekleme, güncelleme ve silme işlemlerinin (tüm CRUD yapısının) kodlarını bizim yerimize otomatik yazar!

class TaskViewSet(viewsets.ModelViewSet):
    # SEBEP: Veritabanından verilerin nasıl çekileceğini belirtiyoruz (Task tablosundaki tüm verileri getir).
    queryset = Task.objects.all()
    
    # SEBEP: Kullanıcıdan gelen verilerin (POST/PUT) veya dışarı gönderilecek verilerin (GET) hangi kurallara göre JSON'a çevrileceğini belirtiyoruz.
    serializer_class = TaskSerializer
