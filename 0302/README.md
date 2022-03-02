# Django

> 20220302

![Image Pasted at 2022-3-2 13-45](README.assets/Image%20Pasted%20at%202022-3-2%2013-45.jpg)

> 오늘의 MVP : django의 흐름



## 웹 프레임워크

### Static web page

* 서버가 정적 웹 페이지에 대한 요청을 받은 경우 추가 처리과정 없이 클라이언트에 응답
  * 클라이언트: =~ 웹브라우저/ 서버: django
* 모든 사용자에게 동일한 정보를 표시



### Dynamic web page

* 웹 페이지에 대한 요청을 받은 경우 추가적인 처리 이후 클라이언트에 응답
* 파이썬, 자바 등 서버 사이드 프로그래밍 언어 사용



### MTV 디자인 패턴

* MVC와 같은 패턴
* Model
  * 응용프로그램의 데이터 구조를 정의, 데이터베이스의 기록 관리(추가, 수정, 삭제)
* Template (MVC의 view)
  * 파일의 구조/ 레이아웃을 정의
  * 실제 내용을 보여주는 데 사용
* View (MVC의 controller)
  * 요청 수신, 응답 반환
  * Model을 통해 요청을 충족시키는데 필요한 데이터에 접근
  * template에게 응답의 서식을 맡김



## Django

### 가상환경 설정

``` bash
$ python -m venv venv
$ source venv/Scripts/activate
```

### 장고 설치

```bash
// 가상환경 활성하고
$ pip install django==3.2.12
```



### 프로젝트 만들기

```bash
$ django-admin startproject <projectname> .
```

### 프로젝트 폴더의 구조

* 프로젝트 폴더를 하나의 파이썬 패키지로 인식하게 됨
* asgi.py
  * 배포 단계에서 사용하는 파일
* settings.py
  * 애플리케이션의 모든 설정 표시
* urls.py *
  * 사이트의 url과 views의 연결을 지정
* wsgi.py
  * 배포 단계에서 사용하는 파일
* manage.py
  * command를 작동하게 하는 파일



### 어플리케이션 만들기

```bash
$ python manage.py startapp <appname>
```

### 어플리케이션 폴더의 구조

* admin.py *
* apps.py 
  * 앱의 정보가 작성된 곳
* models.py *
  * 앱에서 사용하는 Model을 정의하는 곳
* test.py
  * 프로젝트의 테스트 코드를 작성
* views.py *
  * view 함수들이 정의되는곳



### App?

* 실제 요청을 처리하고 페이지를 보여주는 등의 역할
* 하나의 프로젝트는 여러 앱을 가짐
* 일반적으로 앱은 하나의 역할 및 기능 단위로 작성
* 생성 후 project의 settings.py의 INSTALLED_APPS 에 추가해야함 ***
* 앱 등록 시, Local apps/ Third party apps/ Django apps 순서대로 하는 것을 권장



## 요청과 응답

### urls.py

```python
from django.contrib import admin
from django.urls import path
from articles import views # 직접 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.???), # 직접 추가/ 마지막 콤마 
]
```

* urlpatterns 에 path라는 함수 존재



### view 함수 만들기

``` python
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
```

* urls 에서 요청에 응답하기 위해 app 의 views에 함수 추가



### templates 만들기

* `apps/templates/index.html`



## Template

### Django Template Language(DTL)

* 조건 반복 변수치환 필터 등의 기능을 제공
* 일부 프로그래밍적 구조를 사용 가능
* 파이썬이 html에 포함된 것이 아님! 착각x



### 변수

* `{{ variable }}`

* 렌더의 세번째 인자로 딕셔너리 형태로 넘겨줌

* ```html
  <body>
    <p>I'm {{ name }}.</p>
  </body>
  ```

* ```python
  def greeting(request):
      return render(request, 'greeting.html', {'name': 'Alice',})
  ```

* ```python
  def greeting(request):
      context = {
          'name': 'Alice',
      }
      return render(request, 'greeting.html', context)
  ```



### 필터

* 변수 뒤에 파이프라인 `|` 기준으로 사용
* 표시할 변수를 수정할 수 있음



### 태그

```html
<body>
  <p>Today's dinner : {{ pick }} </p>
  <p>{{ pick }} : {{ pick|length }} alp</p>
  <p>{{ foods|join:', ' }}</p>
  <hr>
  <p>menu</p>
  <ul>
    {% for food in foods %}
      <li>{{ food }}</li>
    {% endfor %}
  </ul>
  <a href="/index/">뒤로</a>
</body>
```

* `{% tag %}`
* 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만듬
* 일부 태그는 시작과 종료 태그가 필요
* `{% if %}` `{% endif %}`



### 코멘트(주석)

* `{# 한 줄 주석 #}`



### Template inheritance(상속)

* 코드의 재사용성을 위해

* 구조화를 위해 settings.py 에 템플릿 경로를 추가

  * ```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'],
            ...
        }
    ]
    ```

  * [참고: 파이썬의 객체 지향 파일 시스템](https://docs.python.org/ko/3/library/pathlib.html)

* `{% extends '부모템플릿 이름' %}`

  * 자식 템플릿이 부모 템플릿을 확장받겠다
  * 반드시 템플릿 최상단에 작성

* `{% block %}` `{% endblock %}`

  * 자식 템플릿에서의 재정의를 위한 공간 설정

* 부모 / 자식

  * ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link rel="stylesheet" href="bootstrapcss">
      <title>Document</title>
    </head>
    <body>
      {% include '_nav.html' %}
      {% block content %}
      {% endblock content %}
      
    
      <script src="js"></script>
    </body>
    </html>
    ```

  * ```html
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>메인</h1>
      <a href="/dinner">dinner</a>
      <a href="/greeting">greeting</a>
      <a href="/dtl-practice">dtl_practice</a>
    {% endblock content %}
    ```

