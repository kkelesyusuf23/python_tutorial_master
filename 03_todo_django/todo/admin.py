from django.contrib import admin
from .models import Task # Kendi yazdığımız modeli (tabloyu) içeri aktarıyoruz

# SEBEP: Django'nun bedava verdiği Admin Panelinde kendi oluşturduğumuz Task tablosunu yönetmek istiyoruz.
# Normalde sadece admin.site.register(Task) demek yeterlidir ancak biz daha profesyonel bir görünüm (sütunlar, filtreler) istiyoruz.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # SEBEP: Admin panelinde sadece isimleri değil, görevin durumunu ve oluşturulma tarihini de sütunlar halinde görelim diye.
    list_display = ('title', 'is_completed', 'created_at')
    
    # SEBEP: Sağ tarafa bir filtreleme menüsü ekler. Böylece tek tıkla "Sadece tamamlananları göster" diyebiliriz.
    list_filter = ('is_completed',)
    
    # SEBEP: Üst tarafa bir arama çubuğu ekler. Görev başlığında (title) ve açıklamasında (description) kelime araması yapar.
    search_fields = ('title', 'description')
