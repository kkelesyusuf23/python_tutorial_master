from django.db import models
from django.contrib.auth.models import User # Django'nun kendi içinde hazır gelen Kullanıcı tablosu

# 1. KATEGORİ TABLOSU
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 2. ETİKET TABLOSU
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# 3. BLOG YAZISI TABLOSU (Ana Tablo)
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    # İLİŞKİ 1 (One-to-Many): Bir yazının sadece 1 kategorisi olabilir. 
    # Kategori silinirse (CASCADE) ona bağlı yazılar da silinir.
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    
    # İLİŞKİ 2 (Many-to-Many): Bir yazıda birden fazla etiket olabilir. 
    # Bir etiket de birden fazla yazıda kullanılabilir.
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    
    # İLİŞKİ 3 (One-to-Many): Bir yazının sadece 1 yazarı (kullanıcısı) olabilir.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# 4. YORUM TABLOSU
class Comment(models.Model):
    # İLİŞKİ 4: Bu yorum hangi blog yazısına yapıldı?
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    
    # İLİŞKİ 5: Bu yorumu hangi kullanıcı yaptı?
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.post.title}"
