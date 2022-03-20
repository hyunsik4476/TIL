# 시험대비

## Admin 상속

```python
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'updated_at') # 보이고 싶은 속성
    # 원래는 admin 사이트에서 객체 자체를 보여주는 설정이지만 내가 고칠 수 있음
    
admin.site.register(Article, ArticleAdmin) # 이런 식으로 admin page 조정
```



### 오류 고치기

* OperationalError
  * no such table: articles_article
    * models 에서 선언한 클래스는 appname_classname 의 테이블을 생성
    * DB에 실제로 migrate를 하지 않아서 생기는 오류



### settings.py

* BASE_DIR
* INSTALLED_APPS
* TEMPLATES
* 'DIRS' : [BASE_DIR / 'templates']
* 등 변수명의 단/ 복수형을 잘 보는게 도움이 된다
* LANGUAGE_CODE 이하 설정이 무슨 뜻인지?
  * TIME_ZONE : 데이터베이스 연결 시간대를 나타냄
    * USE_TZ 가 True 일 때만 사용해야함, 아니면 에러 발생
  * USE_I18N : 장고 번역 시스템을 사용할지 여부 설정
    * 이게 True 여야 LANGUAGE_CODE가 작동
  * USE_L10N : 데이터의 localized formatting 을 기본적으로 활성화할지 설정
  * USE_TZ : datetimes가 시간대를 인식하는지 설정
    * True 일 때만 TIME_ZONE 에 사용 가능
* STATIC_DIR
* STATICFILES_DIRS



### template

* base.html 관련 상속 활용하는 방법들



### form

* GET / POST 코드의 차이