from rest_framework import serializers
from .models import Meme, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'memes']


class MemeSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Meme
        fields = ['id', 'picture', 'published', 'tags']


