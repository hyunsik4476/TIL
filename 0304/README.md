# Django

> 20220304

## url 심화

* 여러 개의 앱을 관리할 때, include 함수를 임포트해서 사용 가능
* 서로 다른 앱의 같은 이름을 가진 url name은 이름공간을 설정해 구분함
* django는 정해진 경로의 파일을 하나로 모아서 보기 때문에 
  이름공간 설정을 위해 중간에 임의로 폴더를 만들어 줌



### 장고의 url 읽기

* `(ariticles/template/)dinner.html` 처럼 앞의 경로를 생략할 수 있는 이유
* 이 때, 여러개의 앱을 쓰는 경우 `app1/temps/` , `app2/temps/`, 
  `/basedir/temps/` 등이 약속된 경로로 볼 수 있음
* 각 경로의 html들을 모아서 관리하므로, 이름이 겹치는 경우 
  INSTALLED_APPS에 먼저 등록한 공간의 html을 우선 소환함
* 해서, 각 앱의 urls 에 app_name = 'app1' 과 같이 이름을 설정
* 이후 호출 시 `{% url 'app1:index' %}` 처럼 사용



### 이름 공간 폴더 만들기

* app1 어플리케이션의 templates 폴더 안에 app1 폴더 다시 추가
* 즉 경로가 `/articles/templates/articles/index.html` 처럼 변경
* 장고와 약속한 경로는 `/articles/templates` 까지 이므로
  이후 `render(request, 'articles/index.html', context)` 로 사용



## 웹 서버와 정적 파일(static file)

* 웹 서버는 요청받은 url로 서버에 존재하는 정적 자원을 제공함
* 서비스가 진행되면서 변화하거나 바뀌지 않음(???)



### 스태틱 태그

* `{% load static %}`
  * 스태틱은 빌트-인 태그가 아니기 때문에 로드가 필요
* 로드 태그는 extends로 상속 받아도 따라오지 않기 때문에
  extends 밑에 다시 써줘야함

* `{% static 'app1/example.jpg' %}`
* 파일의 실제 위치 : app1/static/app1/example.jpg
  * templates 와 비슷한 경로 약속



* `{% static 'style.css' %}` <<<



### 스태틱의 추가 경로를 설정

* settings.py 에 내용 추가
* `STATICFILES_DIRS = [BASE_DIR / 'static']`
  * s 오타 주의
* `STATIC_URL = '/static/'`
  * STATIC_ROOT에 있는 정적 파일을 참조 할 때 사용할 URL
  * 실제 파일이나 디렉토리가 아니며, URL로만 존재
  * 비어있지 않은 값으로 설정한다면 반드시 / 로 끝나야 함
  * 이미지를 위한 url을 만들어주는 역할(???)



### 스태틱 루트

* 개발단계에서는 동작하지 않음 
  = settings.py의 DEBUG 값이 True면 작용되지 않음

* 정적 파일을 수집하는 디렉토리의 절대 경로
* django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아 넣는 경로
* 배포 환경에서 django의 모든 정적 파일을 다른 웹 서버가 제공하기 위함



## 추가설명

* path : views.~ 로 호출된 함수에 request 단에 HttpRequest를 넘겨줌
* 이 HttpRequest 는 render 에 의해 리턴됨
