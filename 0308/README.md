# django Model

## Form

### 작동 순서

* form 태그의 action의 url 로 input의 name 값을 이름으로 갖는 변수가 전달
* views의 함수에서 request.GET으로 url 의 정보를 딕셔너리 같은 형태로 받음
* request.GET.get(key) 로 원하는 정보를 찾아냄



## Database

* 데이터 구조화



## ORM

* object-relational-mapping
  * django에서 객체의 관계를 조작해 SQL(데이터베이스)을 조작함
  * SQL을 잘 알지 못해도 DB조작이 가능
  * 하지만, ORM만으로 완전한 서비스를 구현하기 어려운 경우도 있다
* 즉, DB를 객체로 조작하기 위해 ORM을 사용한다



## 데이터 구조화

### Django(서버)

* URL 요청이 들어오면 처리해서 응답

### 모델

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    # 처음 추가될 때만
    updated_at = models.DateTimeField(auto_now=True)        # 뭔가 바뀔 때 항상
```

* `models.Model` 을 상속받음
* 여러 가지 필드(타입) 을 클래스의 속성으로 가짐



* 모델을 통해서 데이터를 구조화하고 DB에 반영(migration)
  * 클래스로 구조화 할 예정
* 데이터를 조작
  * 클래스로 구조화했으므로 객체를 조작할 예정
* 결과를 DB에 반영?(쿼리문 작성???)



### migration

* models.py에 생긴 변화를 db에 반영하는 과정



* `python manage.py makemigrations`
  * migration(설계도) 파일 생성
* `python manage.py migrate`
  * 실제로 DB에 반영하는 작업



## Database API

### DB 조작하기

* Articles.objects.all()
  * classname/ manager/ queryset API
* QuerySet
  * 데이터베이스로부터 전달받은 객체 목록



### shell_plus

* pip install ipython django-extensions

* INSTALLED_APPS 에 'django_extensions' 등록 ( 언더바임! )

* python manage.py shell_plus 로 shell 실행

* Article.objects.all()

* ```bash
  In [1]: Article.objects.all()
  Out[1]: <QuerySet []>
  
  In [2]: article = Article()	# models 에 정의한 클래스
  
  In [3]: article.title = '제목'
  
  In [4]: article.content = '내용입니다.'	# 클래스의 속성
  
  In [5]: article
  Out[5]: <Article: Article object (None)>
  
  In [6]: article.save()	# 저장
  
  In [7]: article
  Out[7]: <Article: Article object (1)>
  
  In [8]: Article.objects.all()	# 전체 내용 조회
  Out[8]: <QuerySet [<Article: Article object (1)>]>
  
  #==========================#
  
  In [9]: a2 = Article(title='2번글', content='2번 내용')
  
  In [10]: a2.save()
  
  In [11]: Article.objects.all()
  Out[11]: <QuerySet [<Article: Article object (1)>, 
  <Article: Article object (2)>]>
  
  #=========================#
  
  In [12]: Article.objects.create(title='3번글', content='3번 내용')
  Out[12]: <Article: Article object (3)>
  
  In [13]: Article.objects.all()
  Out[13]: <QuerySet [<Article: Article object (1)>, 
  <Article: Article object (2)>, <Article: Article object (3)>]>
  ```



#### Read

```python
# 1. 전체 데이터
Article.objects.all()
# >>> queryset 출력

# 2. 단일 데이터
# DB에 저장 시 자동으로 저장되는 id, pk 를 이용해 .get으로 확인 가능
Article.objects.get(pk=1)
# >>> <Article: Article object (1)>

# 2-1. 없는 데이터
Article.objects.get(pk=999)
# >>> DoesNotExist: Article matching query does not exist.

# 2-2 여러 값을 가지는 키를 .get 에 넣은 경우 => 에러

# 3. 여러 데이터
Article.objects.filter(title='제목')
# >>> queryset 출력
```

* get()은 고유한 값을 조회할 때 사용한다
  * pk(primary key)는 DB에서 유일한 값이므로 pk를 기준으로 조회할 때 사용함

* filter()는 여러 데이터를 조회한다



#### Update

```python
In [14]: a2 = Article.objects.get(pk=2)

In [15]: a2.title = '제목'

In [16]: a2.save()
```



#### Delete

```python
a3 = Article.objects.get(pk=3)
a3.delete()
```



# 게시판 만들어보기

## 내용 저장용 DB 만들기

* models.py

* ```python
  from django.db import models
  
  # Create your models here.
  class Article(models.Model):
      title = models.CharField(max_length=30)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)    # 처음 추가될 때만
      updated_at = models.DateTimeField(auto_now=True)        # 뭔가 바뀔 때 항상
  
  ```

  * models.Model 을 상속한 클래스
  * objects 등의 속성을 갖고있음



## 입력받은 내용을 DB에 저장하고, 화면에 출력하기

### Form

* ```python
  {% extends 'base.html' %}
  {% block section %}
  <form action="{% url 'articles:create' %}" method="GET">
    <label for="title">title</label>
    <input type="text" id="title" name="title">
    <br>
    <label for="content">content</label>
    <textarea name="content" id="content" cols="30" rows="10"></textarea>
    <hr>
    <input type="submit">
  </form>
  {% endblock section %}
  ```

* form 태그의 액션에서 DB에 저장하기 위한 url(`{% url 'articles:create' %}`)로 요청을 보냄



### DB에 저장하기

* ```python
  from django.shortcuts import render, redirect
  # ...
  def create(request):
      article = Article()
      article.title = request.GET.get('title')
      article.content = request.GET.get('content')
      article.save()
      context = {
          'article': article,
      }
      # return redirect('articles:index')
      return redirect('articles:detail', article.pk)
  ```

* 전에 하던 것과 비슷하지만 models.py 에서 만든 클래스 Article을 사용함

* `article.save()` 를 해야 DB에 저장됨

* 글 작성이 완료되면 redirect를 이용해 작성 내용을 보여주는 detail 로 보낼 예정

  * 이 때, detail 은 variable routing 을 쓸 것이므로 글의 번호, pk를 보내줌



### 글 보여주기

* 각 글마다 페이지를 정해줘야 하므로 변수를 받을 것

* 늘 그렇듯이, 유 -> 뷰 -> 템 순서로 만들자

* ```python
  urlpatterns = [
      path('<int:pk>/', views.detail, name='detail'),
  ]
  ```

  * 이게 조금 헷갈리는데 /articles/1/ 로 가면 1번 글의 내용이 보이는 형태

* ```python
  def detail(request, pk):
      article = Article.objects.get(pk=pk)
      context = {
          'article': article
      }
      return render(request, 'articles/detail.html', context)
  ```

  * `Article.objects` 을 사용해 위에서 저장한 pk 번 글의 제목과 내용을 불러올 수 있음
  * html 템플릿은 생략



### 글 삭제/ 수정

* 유뷰템

#### 유

* ```python
  urlpatterns = [
      path('<int:pk>/delete/', views.delete, name='delete'),
      path('<int:pk>/edit/', views.edit, name='edit'),
      path('<int:pk>/update/', views.update, name='update'),
  ]
  ```

  * 마찬가지, 글마다 다른 내용을 보여주거나 삭제해야 하므로 variable routing

#### 뷰

* ```python
  def delete(request, pk):
      article = Article.objects.get(pk=pk)
      article.delete()
      return redirect('articles:index')
  ```

  * 삭제 : 클래스의 .delete() 메서드 사용 가능

* ```python
  def edit(request, pk):
      article = Article.objects.get(pk=pk)
      context = {
          'article': article,
      }
      return render(request, 'articles/edit.html', context)
  ```

* ```python
  def update(request, pk):
      article = Article.objects.get(pk=pk)
      article.title = request.GET.get('title')
      article.content = request.GET.get('content')
      article.save()
  
      return redirect('articles:detail', article.pk)
  ```

  * 수정 : 내용을 입력할 url 과 입력받은 내용을 저장할 url 두개가 사용된다
  * `edit` 에서 article 을 가져온 이유는 이전에 썼던 글의 내용을 보여주기 위함
  * `update` 의 경우 위에서 저장하는 것과 거의 비슷하지만 article을 새로 class 로 지정하는것이 아닌 이미 저장된걸 가져오는게 차이점
  * 저장이 완료되면 `article/<pk>`로 리다이렉트해 수정된 내용을 보여줌

#### 템

* 이번엔 좀 헷갈려서 템플릿도 추가

* ```html
  {% extends 'base.html' %}
  {% block section %}
  <form action="{% url 'articles:update' article.pk%}" method="GET">
    <label for="title">title</label>
    <input type="text" id="title" name="title" value="{{article.title}}">
    <br>
    <label for="content">content</label>
    <textarea name="content" id="content" cols="30" rows="10">{{article.content}}</textarea>
    <hr>
    <input type="submit">
  </form>
  {% endblock section %}
  ```

  * `edit` 
  * 입력받은 내용을 action을 통해 DB에 저장하는 url `update` 로 보냄
  * `{% url 'articles:update' article.pk%}` django html 에서 variable routing 을 위한 값을 보내는 방법

