from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from .models import Post
from .serializers import PostSerializer

# SEBEP: İleride sistemimizde yüzlerce blog yazısı olduğunda, API'nin tümünü tek seferde gönderip 
# hem sunucuyu hem de müşterinin internetini yormaması için "Sayfalama" (Pagination) sınıfı oluşturuyoruz.
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10 # Her API çağrısında varsayılan olarak sadece 10 yazı gönder
    page_size_query_param = 'size' # Müşteri URL'nin sonuna "?size=20" yazarak limiti esnetebilsin
    max_page_size = 50 # Müşteri sistemi yormak için "?size=10000" yazarsa, maksimum 50'ye kadar izin ver

class PostViewSet(viewsets.ModelViewSet):
    # En yeni yazılar en üstte gelsin diye created_at başına "-" (eksi) koyuyoruz
    queryset = Post.objects.all().order_by('-created_at') 
    serializer_class = PostSerializer
    
    # 1. SAYFALAMA ÖZELLİĞİ: Yukarıda yazdığımız ayarı bu görünüme ekliyoruz.
    pagination_class = StandardResultsSetPagination
    
    # 2. ARAMA (SEARCH) VE SIRALAMA (ORDERING) ÖZELLİKLERİ
    # SEBEP: DRF'nin bize bedavaya sunduğu arama motorunu ve sıralama butonlarını aktif ediyoruz.
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    
    # Kullanıcı tarayıcıda "?search=python" diye arattığında, bu kelimeyi nerelerde arayalım?
    # Not: 'author__username' yazımı Django'ya hastır. "author tablosuna git, oradaki username'in içinde ara" demektir (İlişkisel arama).
    search_fields = ['title', 'content', 'author__username', 'category__name', 'tags__name']
    
    # Müşteri "Tarihe göre" veya "Başlığa göre" sıralama yapabilsin
    ordering_fields = ['title', 'created_at']
