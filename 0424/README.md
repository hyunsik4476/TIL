# PJT08

## Models

### ERD

* ERD에 나온 대로 Movie - Actor M:N , Movie, Review 1:N 관계 모델링

* ```python
  from django.db import models
  
  # Create your models here.
  class Actor(models.Model):
      name = models.CharField(max_length=100)
  
  class Movie(models.Model):
      actors = models.ManyToManyField(Actor, related_name='movies')
      title = models.CharField(max_length=100)
      overview = models.TextField()
      release_date = models.DateTimeField(auto_now_add=True)
      poster_path = models.TextField()
  
  class Review(models.Model):
      movie = models.ForeignKey(Movie, on_delete=models.CASCADE)    
      title = models.CharField(max_length=100)
      content = models.TextField()
  
  ```



## Fixtures

### 만들기

* `python manage.py dumpdata --indent 4 appname.modelname > modelname.json`
  * 이번에는 미리 제공됨

### 적용하기

* 적용하기에 앞서 JSON내에 어떤 필드가 있는지 확인해봄
* migrate 이후 `python manage.py loaddata movies/<modelname>.json`으로 DB 적용



## rest_framework

* settings.py 에 설치 잊지말자



## urls

* ```python
  # pjt/urls.py
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('api/v1/', include('movies.urls')),
  ]
  ```

* ```python
  # app/urls.py
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path('actors/', views.actors_list),
      path('actors/<int:actor_pk>/', views.actor_detail),
      path('movies/', views.movies_list),
      path('movies/<int:movie_pk>/', views.movie_detail),
      path('movies/<int:movie_pk>/reviews/', views.review_create),
      path('reviews/', views.reviews_list),
      path('reviews/<int:review_pk>/', views.review_detail),
  ]
  ```

* 아직 RESTful 한 URL 구조라는게 뭔지 잘 감이 오지 않는다

* 명세대로 구현



## Serializers

### 모듈화

* class 관리를 위해 모델에 따라 나누었음

* 상세 페이지 정보에서 movie - actor 가 서로의 class 를 참조해야 할 일이 있었는데 이 상황을 해결하기 위해 shorten.py 추가

* ```python
  from rest_framework import serializers
  from .shorten import MovieShortenSerializer
  from ..models import Actor, Movie, Review
  
  class ActorListSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Actor
          fields = ('id', 'name',)
  
  
  class ActorSerializer(serializers.ModelSerializer):
      movies = MovieShortenSerializer(many=True, read_only=True)
  
      class Meta:
          model = Actor
          fields = ('__all__')
  ```

* ```python
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
  ```

* ```python
  from rest_framework import serializers
  from ..models import Review
  
  
  class ReviewListSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Review
          fields = ('title', 'content',)
  
  
  class ReviewSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Review
          fields = ('__all__')
          read_only_fields = ('movie',)
  ```

* ```python
  from rest_framework import serializers
  from ..models import Actor, Movie, Review
  
  class ActorShortenSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Actor
          fields = ('name',)
  
  
  class MovieShortenSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Movie
          fields = ('title',)
  ```





## views
### 목록 / 상세 받아오기


* ```python
  @api_view(['GET'])
  def actors_list(request):
      actors = get_list_or_404(Actor)
      serializer = ActorListSerializer(actors, many=True)
      return Response(serializer.data)
  
  
  @api_view(['GET'])
  def actor_detail(request, actor_pk):
      actor = get_object_or_404(Actor, pk=actor_pk)
      serializer = ActorSerializer(actor)
      return Response(serializer.data)
  ```

* 다른 점은 list / object, many=True 뿐



### 리뷰 RUD

* ```python
  @api_view(['GET', 'DELETE', 'PUT'])
  def review_detail(request, review_pk):
      review = get_object_or_404(Review, pk=review_pk)
      if request.method == 'GET':
          serializer = ReviewSerializer(review)
          return Response(serializer.data)
  
      elif request.method == 'DELETE':
          review.delete()
          data = {
              'delete': f'{review_pk}번 리뷰가 삭제되었습니다.'
          }
          return Response(data, status=status.HTTP_204_NO_CONTENT)
  
      elif request.method == 'PUT':
          serializer = ReviewSerializer(review, request.data)
          if serializer.is_valid(raise_exception=True):
              serializer.save()
              return Response(serializer.data)
  ```

* delete 에서 data 사용 확인

### 리뷰 Create

* ```python
  @api_view(['POST'])
  def review_create(request, movie_pk):
      movie = get_object_or_404(Movie, pk=movie_pk)
      serializer = ReviewSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save(movie=movie)
          return Response(serializer.data, status=status.HTTP_201_CREATED)
  ```

* Create 의 경우 review가 어느 movie에 작성되었는지를 알려줘야함

  * movie 를 read_only_fields 로 설정하고 `.save(movie=movie)` 를 통해 해결