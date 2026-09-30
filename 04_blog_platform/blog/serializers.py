from rest_framework import serializers
from .models import Category, Tag, Post, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    # SEBEP: Yorumu çeken kişi, yazarın sadece ID'sini (Örn: 1) değil, adını da görsün diye.
    author_name = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Comment
        fields = ['id', 'author', 'author_name', 'text', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    # ==========================================
    # İÇ İÇE (NESTED) SERIALIZERS MANTIĞI
    # ==========================================
    # SEBEP: Normalde DRF, ilişkili (ForeignKey) alanları sadece ID olarak döndürür (Örn: category: 1, tags: [1,2]).
    # Ancak bir mobil uygulama geliştiricisi 1 numaralı kategorinin adının ne olduğunu bilmek ister.
    # "source='category'" diyerek yukarıdaki CategorySerializer'ı buraya GÖMÜYORUZ.
    # "read_only=True" çok önemlidir: Sadece veriyi okurken (GET) detayları getirir. 
    # Yeni bir blog yazısı eklerken (POST) yine sadece Kategori ID'si (category=1) göndermemiz yeterlidir.
    
    category_detail = CategorySerializer(source='category', read_only=True)
    tags_detail = TagSerializer(source='tags', many=True, read_only=True)
    author_name = serializers.ReadOnlyField(source='author.username')
    
    # Bir blog yazısına atılan yorumları (One-to-Many ilişkisinin tersi) getirmek için
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'content', 'created_at',
            'category', 'category_detail',   # Hem ID okumak/yazmak için, hem Detay görmek için
            'tags', 'tags_detail',           # Hem ID listesi, hem Detay listesi
            'author', 'author_name',
            'comments'                       # Bu yazıya ait yorumlar
        ]
