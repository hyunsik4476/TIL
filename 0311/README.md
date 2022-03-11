# 깃

## 브랜치

### 목록 확인

* `git branch`



### 생성

* `git branch branchname`



### 브랜치 이동

* `git switch branchname`
* `git switch -c branchname`



### 로그 보기

* `git log --oneline` : 현재 헤드 위치의 로그

* `git log --oneline -- all` : 전체 로그

* `git log --oneline --all --graph` : 브랜치가 갈라진 거 확인 가능



### 삭제

* `git branch -d branchname`
* `git branch -D branchname` : 병합 여부에 관계없이 삭제



## 주의!!!

* 브랜치가 독립적인 공간이다?
  * -> 깃이 관리하는 파일공간 안에서만 성립
* 즉, staging area에 올라간 적 있는 파일만!



## 병합(merge)

* 병합 전, 메인브랜치로 switch 해야함
  * master는 항상 메인브랜치

### fast-forward

* 병합된 새 버전이 탄생하는게 아니라 과거에 있던게 앞으로 옴



### 3-way merge (merge commit)

* 두 가지의 공통 조상을 이용해 병합 후 새 버전 생성



### merge conflict

* 병합하는 두 브랜치에서 같은 파일의 같은 부분을 동시에 수정하는 경우



## Merge request

* 프로젝트 클론
* 내 브랜치 생성
* 작업 후 git push origin 내 브랜치 이름



# 프로젝트

## 웹 DB만들기

### 모델

```python
from django.db import models
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    release_date = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=30)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()
```

* movie = Movie(title='', audience='' ...) 같이 사용도 가능
  * movie.save() 필요
* movie = Movie.objects.create(title=''...)
  * 생성과 저장 동시에 가능
* 생성 후, python manage.py makemigrations/ python manage.py migrate 잊지말기



### Django html

```django
<a href="{% url 'movies:detail' movie.pk %}">
  <h3>{{ movie.title }}           
    <span class="badge {% if movie.score >= 3 %}bg-primary
                 {% else %}bg-secondary{% endif %} fs-5 px-1 py-0 fw-normal">
        {{ movie.score }}
    </span>
  </h3>
</a>
<p>{{ movie.description|truncatechars:50 }}</p>
```

```django
<footer>
  <div>
    <form action="{% url 'movies:edit' movie.pk %}" method="POST" style="display: inline;">
      {% csrf_token %}
      <button type="submit">수정</button>
    </form>
    <form action="{% url 'movies:delete' movie.pk %}" method="POST" style="display: inline;">
      {% csrf_token %}
      <button type="submit">삭제</button>
    </form>
  </div>
</footer>
```

* POST 메소드가 필요한 경우 a태그대신 form 으로 감싸서 링크를 전달해야함

```python
<select class="form-control" name="genre" id="genre">
  {% for genre in genres %}
    <option value="{{ genre }}" {% if genre == movie.genre %}selected{% endif %}>{{ genre }}</option>
  {% endfor %}
</select>
```

