from rest_framework import serializers
from .shorten import MovieShortenSerializer
from ..models import Review


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content',)


class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieShortenSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('__all__')
        read_only_fields = ('movie',)
