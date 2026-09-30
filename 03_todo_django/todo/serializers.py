from rest_framework import serializers
from .models import Task

# SEBEP: FastAPI'deki "schemas.py" (Pydantic) dosyasının Django'daki tam karşılığı "Serializers" kavramıdır.
# Serializer'ın iki çok kritik görevi vardır:
# 1. (Doğrulama - Validation): İstemciden (kullanıcıdan) gelen JSON verisinin doğru formatta olup olmadığını test eder. (Örn: title boş mu? is_completed sadece True/False mu?)
# 2. (Dönüştürme - Serialization): Veritabanından (Models) okunan karmaşık verileri (Queryset) alıp API üzerinden gönderilebilecek temiz bir JSON metnine çevirir.

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task  # SEBEP: Bu serializer'ın bizim yazdığımız Task modeli (tablosu) ile bağlantılı olduğunu belirtiyoruz.
        
        # SEBEP: Modeldeki hangi alanların (sütunların) API'de gösterileceğini veya güncellenebileceğini belirtiyoruz.
        # Tek tek ('id', 'title', 'description'...) yazmak yerine pratiklik için '__all__' (hepsi) diyoruz.
        fields = '__all__'
