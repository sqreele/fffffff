from rest_framework import serializers
from .models import Article



class ArticleSerializers(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only = True)
    author = serializers.StringRelatedField()
    class Meta:
        model =Article
        fields = '__all__'