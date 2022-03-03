# Django

> 20220303

##  큰 흐름

* 가상환경 만들기
* django-admin startproject \<pjtname>
* python manage.py startapp \<appname>
* settings.py 에 앱 등록
* urls -> views -> templates



## django의 built-in template tag & filter

[문서](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/)



## url 관리

* 여러 개의 앱을 관리할 때, url 을 앱의 하위에서 관리하게 됨
* 프로젝트의 url에는 `import ... path, include` 추가 후
* `path('articles/', include(articles.urls)),` 추가
* 앱의 url 에는
* `app_name = 'articles'`
* `path('throw/', views.throw, name='throw')` url 설정 할때 이름 붙이기 가능
* 이후, 호출해야 할 때는
* `{% url 'articles:throw' %}` 로 이름 붙인 url 호출 가능



## 상속

```html
{% extends 'base.html' %}

<div class="container">
  {% block content %}
    <h1>메인</h1>
    <a href="/dinner">dinner</a>
    <a href="/greeting">greeting</a>
    <a href="/dtl-practice">dtl_practice</a>
  {% endblock content %}
</div>
```



## 실습 : 로또 시뮬

```python
from django.shortcuts import render
import random
import requests
import json

# Create your views here.

def lotto(request):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1'
    res = requests.get(url)
    data = res.json()
    lotto = []
    cnt = [0]*6
    bonus = data['bnusNo']
    for i in range(1, 7):
        ltkey = 'drwtNo'+str(i)
        lotto.append(data[ltkey])

    for j in range(1000):
        i = 0
        b = 0
        tmp = random.sample(range(1, 46), 6)
        for num in tmp:
            if num in lotto:
                i += 1
            if num == bonus:
                b = 1
        if i == 6:
            cnt[0] += 1
        elif i == 5 and b == 1:
            cnt[1] += 1
        elif i >= 3:
            cnt[7-i] += 1
        else:
            cnt[5] += 1

    context = {
        'lotto' : lotto,
        'bonus': bonus,
        'cnt': cnt,
    }

    return render(request, 'lotto.html', context)

```

```html
<h1>로또 당첨 횟수를 알아보자</h1>
<hr>
<h3>당첨 번호 : {{ lotto }} + {{ bonus }}</h3>
<ul>
  {% for num in cnt %}
    <li>{{ forloop.counter }}등 : {{num}}번</li>
  {% endfor %}
</ul>

```

