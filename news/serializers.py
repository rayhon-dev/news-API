from rest_framework import serializers

from tags.serializers import TagSerializer
from .models import New
from categories.serializers import CategorySerializer


class NewsSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)


    class Meta:
        model = New
        fields = ['id', 'title', 'content', 'category','tags', 'image', 'is_published']


