# 정리

## URL

* `path('articles/', include('articles.urls'))`
  * 이 경우 path, include 만 임포트 하면 됨
* 앱/urls.py 에서 app_name 설정
  * from . import views 설정
  * path 에서도 name 설정해주기




## 뷰

* `redirect('articles:index')`
  * 만약 변수가 필요한 URL 이면 `redirect('articles:index', article.pk)`



## 모델

### 읽기

* Article.objects.all() : 모두 읽기
* Article.objects.get(pk=???) : 조건에 맞는 1개 객체 읽기
  * 맞는 조건이 없으면 DoesNotExist 에러
  * 조건이 맞는게 여러개 있으면 MultipleObj.. 에러
* Article.objects.filter() : 조건에 맞는 여러 데이터 조회
  * 맞는 데이터가 없어도 에러가 나지 않음
  * 빈 쿼리셋 



### 쓰기

* a = Article()
* a = Article(title = 'title', content = 'content')
* a = Article.objects.create(title = 'title', content = 'content')
  * 이 경우 a.save() 필요없음



## 어드민

* ``` python
  from .models import Article
  admin.site.register(Article)

* ```python
  class ArticleAdmin(admin.ModelAdmin):
      list_display = ['id', 'title', 'content']
  admin.site.register(Article, ArticleAdmin)
  ```

* 



## 그 외

* POST 옵션의 경우 `{% csrf_token %}` 필요

* static 사용시 `{% load static %}`

  * ```python
    STATICFILES_DIRS = [
        BASE_DIR / 'static',
    ]
    ```

* form 태그에서 action 활용하는 방법

  * `{% url 'articles:detail' article.pk %}`