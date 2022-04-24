from rest_framework import serializers
from ..models import Actor, Movie

class ActorShortenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name',)


class MovieShortenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title',)