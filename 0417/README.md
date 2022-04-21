# 시험준비

* filter 옵션
* order_by('-pk')
* model 정의할 때
  * FK 에서 on_delete 의 옵션들
  * migtration 이 무엇인지?
* djangoORM 이 무엇인지? / 장단점?
  * 교재 참고
* dmm , sql 문법
* INSERT 하는 방법
* LIKE 의  option
* RDBMS의 특징



## SQL

### CREATE

* ```sql
  CREATE TABLE tablenames (
  id INTERGER PRIMARY KEY,
  name TEXT NOT NULL,
  address TEXT,
  );
  ```



### DROP

* ```sql
  DROP TABLE tablenames;
  ```

* 테이블 삭제



### INSERT

* ```sql
  INSERT INTO tablenams (col1, col2) VALUES(val1, val2);
  ```

* ```sql
  INSERT INTO tablenames VALUES(val1, val2, val3);
  ```

* 특정 테이블에 단일 행 삽입

* 모든 컬럼에 값을 넣는 경우 아래와 같이 작성 가능



### SELECT

* ```sql
  SELECT rowid, * FROM tablenames;
  SELECT col1, col2 FROM tablenames LIMIT 10 OFFSET 5; # 갯수, 시작점
  SELECT col1 FROM tablenames WHERE address='서울'; # 특정 조건
  SELECT DISTINCT col1 FROM tablenames; # 중복 없이 조회
  ```

* 특정 테이블의 레코드 정보 반환



### DELETE

* ```sql
  DELETE FROM tablenames WHERE rowid=3;
  ```

* sqlite 는 삭제된 id값을 재사용한다

* 이를 막기위해 스키마에 AUTOINCREMENT 속성을 추가할 수 있으며, 이는 django 에서 기본값으로 설정되어있다



### UPDATE

* ```sql
  UPDATE tablenames SET col1=val1, col2=val2 WHERE rowid = 5;
  ```



### WHERE

* ```sql
  SELECT col1 FROM tablenames WHERE age>=30 AND last_name='김';
  ```



### Aggregate funtion

* SELECT 구문에서만 사용됨

* ```sql
  SELECT COUNT(*) FROM tbns;
  ```

* ```sql
  SELECT AVG(col1) FROM tbns;
  ```

* 이 외 SUM, MIN, MAX 등 존재



### LIKE

* ```sql
  SELECT * FROM tbns WHERE phone LIKE '02-%';
  ```

* 패턴 일치를 기반으로 데이터를 조회
* `_` : 해당 자리에 반드시 하나의 문자가 존재해야함
* `%` : 해당 자리에 0개 이상의 문자가 존재하면 됨



### ORDER BY

* ```sql
  SELECT age FROM tbns ORDER BY col1 ASC col2 DESC;
  ```



### GROUP BY

* ```sql
  SELECT col1, MIN(col2) FROM tbns GROUP BY col1, col2;
  ```

* 문장에 WHERE 절이 포함된 경우 반드시 WHERE 절 뒤에



## ORM

* ```python
  # 모두 조회
  User.objects.all()
  # 특정 행 조회
  User.objects.get(pk=pk)
  # 새로운 행 추가
  User.objects.create(col1 = val1, col2 = val2)
  # 내용 수정
  user = User()
  user.name = 'new_name'
  user.save()
  # DB크기
  User.objects.count()
  # 특정 조건
  User.objects.filter(age=30).values('name')
  # __gte, __lte, __gt, __lt
  User.objects.filter(age__gte=30).count()
  User.objects.filter(age=30, last_name='김')
  # Q object
  User.objects.filter(Q(age=30) | Q(last_name='김'))
  # 와일드카드
  User.objects.filter(name__startswith='김')
  # 정렬
  User.objects.order_by('-pk')
  # aggregate
  User.objects.aggregate(Avg('age'))
  User.objects.aggregate(avg_value=Avg('age'))
  # annotate
  User.objects.values('country').annotate(Count('country'))
  ```



## 1:N

* ```python
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  ```

* 1:N 관계에서 N DB는 ForeignKey 를 가짐

* 이 값은 반드시 PK일 필요는 없으나 유일한 값이어야 함

* on_delete 옵션은 데이터 무결성(Database integrity)와 관련된 옵션



* ```python
  comment.article
  >>> <Article obj>
  comment.article_id
  >>> 1(FK)
  comment.article.pk
  >>> 1(PK)
  article.comment_set.count()
  
  
  ```



* ```python
  comment.save(commit=False)
  comment.article = article
  comment.save()
  # or
  comment.article_id = article.pk
  comment.save()
  ```

* 