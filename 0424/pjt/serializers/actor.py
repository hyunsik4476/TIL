from rest_framework import serializers
from .shorten import MovieShortenSerializer
from ..models import Actor

class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('id', 'name',)


class ActorSerializer(serializers.ModelSerializer):
    movies = MovieShortenSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ('__all__')