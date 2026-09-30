from django.contrib import admin
from .models import Category, Tag, Post, Comment

# Kategori ve Etiket tablolarını basitçe Admin paneline kaydediyoruz
admin.site.register(Category)
admin.site.register(Tag)

# Post (Blog Yazısı) tablosunu daha detaylı kaydediyoruz
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Yazıları listelerken başlığını, kategorisini, yazarını ve tarihini görelim
    list_display = ('title', 'category', 'author', 'created_at')
    
    # Sağ tarafta Kategoriye ve Etikete göre filtreleme menüsü olsun
    list_filter = ('category', 'tags')
    
    # Başlıkta ve içerikte kelime araması yapabilelim
    search_fields = ('title', 'content')

# Yorum tablosunu kaydediyoruz
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Yorumları listelerken hangi yazıya, kimin tarafından ne zaman yapıldığını görelim
    list_display = ('post', 'author', 'created_at')
    search_fields = ('text',)
