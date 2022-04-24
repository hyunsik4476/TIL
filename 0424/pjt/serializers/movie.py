from rest_framework import serializers
from .review import ReviewListSerializer
from .shorten import ActorShortenSerializer
from ..models import Movie

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview',)


class MovieSerializer(serializers.ModelSerializer):
    review_set = ReviewListSerializer(many=True, read_only=True)
    actors = ActorShortenSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('__all__')
