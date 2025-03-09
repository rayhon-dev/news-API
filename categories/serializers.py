from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', ]


    def create(self, validated_data):
        validated_data['slug'] = validated_data['name'].lower().replace(' ', '-')
        return super().create(validated_data)
