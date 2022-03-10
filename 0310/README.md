# Model

> 20220310

## 모델

### 모델이란

* 데이터의 구조(DB)
  * 마이그레이션
  * 모델의 클래스 <=> DB의 테이블 연결
* 데이터 조작(ORM)



## GET, POST

* POST 의 경우, CSRF 토큰에 대한 설정이 필요
* 각각의 form 태그 안에 `{% csrf_token %}` 필요



## render() 와 redirect()

* recirect 가 필요한 순간에 render를 사용하면 views를 통과하지 않을 수 있음



## 관리자 페이지 만들기

* admin.py 안에서,
* from .models import Article
* admin.site.register(Article)



* bash 에서
* python manage.py createsuperuser