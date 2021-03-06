# 0421

## 정리

```python
# serializers.py
from rest_framework import serializers
from .models import Artist, Music


class MusicListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ('id', 'title',)

class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ('__all__')
        read_only_fields = ('artist',)

class ArtistListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('__all__')

class ArtistSerializer(serializers.ModelSerializer):
    music_set = MusicSerializer(many=True, read_only=True)
    music_count = serializers.IntegerField(source='music_set.count', read_only=True)

    class Meta:
        model = Artist
        fields = ('__all__')
```

```python
# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Artist, Music
from .serializers import ArtistListSerializer, ArtistSerializer, MusicListSerializer, MusicSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def artists_list(request):
    artists = get_list_or_404(Artist)
    if request.method == 'GET':
        serializer = ArtistListSerializer(artists, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistSerializer(artist)
    return Response(serializer.data)


@api_view(['POST'])
def music_create(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = MusicSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(artist=artist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def music_list(request):
    musicList = get_list_or_404(Music)
    serializer = MusicListSerializer(musicList, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        music.delete()
        data = {
            'delete': f'데이터 {music_pk}번 음악이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = MusicSerializer(music, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
```

## 1:N 2가지 방법

```python
class ArticleSerializer(serializers.ModelSerializer):
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = ('__all__')

```

