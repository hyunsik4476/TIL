# DB/ SQL

[참고](https://www.sqlitetutorial.net/)

## 데이터베이스

* 자료 파일을 조직적으로 통합



### 스키마

* 데이터베이스 구조에 대한 명세
* 어떤 column 값을 갖고 데이터 타입이 뭔지



### 구조

* 



### RDBMS

* 관계형 데이터베이스 관리 시스템
* 핵심 : 테이블
  * 행. 레코드 / 열. 컬럼. 필드 를 가짐
  * ************스키마 : 필드를 타입 지정

### SQLite

* 서버 형태가 아닌 파일 형식으로 응용 프로그램에 넣어서 사용하는 가벼운 데이터베이스
* 타입 선호도라는 동적 데이터타입을 가짐
* Null, Integer, Real, Text, BLOB 같은 데이터 타입을 가짐
  * Type Affinity
  * 프로젝트의 경우 처음 선언시부터 선호 타입에 맞게 시작할 예정



### 장고 모델과 뭐가 다른가?

* 마이그레이션 파일에 DB에 필요한 내용들이 들어있고 makemigrate로 반영됨
  * 즉, 클래스 변경을 통해 기존 테이블에 비해 어떻게 바꿀지 확인하고 만들어지는 파일임
* 모델을 만들었다 = 대응되는 테이블을 생성해야한다
  * SQLite 에서 CREATE TABLE



## SQL

* 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계됨
* 데이터베이스 스키마의 생성 및 수정이 가능
* 데이저 정의/ 조작/ 제어 언어
  * CREATE, DROP, ALTER
  * INSERT, SELECT, UPDATE, DELETE (=CRUD)



### CSV 파일 기반으로 DB, TABLE 만들기

* $ sqlite3 tutorial.sqlite3
  * $ .database (DB생성)
  * $ .mode csv
  * $ .import \<dbname>.csv \<tablename> (테이블 생성)
  * $ SELECT * FROM \<tablename>; (읽기 명령, tablename 전체 테이블의 모든 데이터 조회)
  * $ .headers on
  * $ .mode column
* DROP TABLE \<tablename> (테이블 삭제)
* INSERT INTO \<tablename> (col1, col2, ...) VALUES (val1, val2, ...)
  * 모든 컬럼을 채울땐 col1 ... 필요없음

* id(primary key)의 경우 별도로 명시하지 않으면 보이지 않음
  * rowid 라는 이름의 컬럼이 내부적으로 정의됨

* 꼭 필요한 정보는 NULL 값으로 두면 안된다 (NOT NULL) 설정이 필요
  * 스키마를 만들 때 타입 뒤에 NOT NULL 추가
* PRIMARY KEY 속성의 경우 스키마 설정 시 타입을 반드시 INTERGER로
  * affinity 에 의해 INT, INTERGER 모두 INTERGER로 통합되지만 이 경우에는 주의가 필요
  * 스키마에 id를 직접 작성한 경우 모든 column에 데이터를 채울 때에서 col을 명시해야함



### 테이블에서 데이터 조회하기

> SELECT

* 다양한 clause (절) 과 함께 사용됨
  * 원하는 조건에 맞게 조회해야하므로



### DISTINCT

* 반드시 SELECT 바로 뒤에



### csv 파일 임포트하기

* sqlite3 \<DBname>.sqlite3
* .mode csv
* .import <csvname.csv> \<tablename>



### 조건 걸기

> WHERE

* SELECT * FROM users WHERE age >= 30;



### 집계 함수(aggfunc)

> Aggregate funcion

* 여러 행으로부터 하나의 결괏값을 반환하는 함수
* SELECT 구문에서만 사용됨



### LIKE

* 패턴 일치를 기반으로 데이터를 조회
* % (percent sign)
  * 0개 이상의 문자
  * 이 자리에 문자열이 있을 수도, 없을 수도 있다
* _ (underscore)
  * 임의의 단일 문자
  * 자리에 반드시 한 개의 문자가 존재해야함
* SELECT * FROM users WHERE age LIKE '2_';
  * 20대 인 사람들 (2, 200, 2000 등이 검색되지 않도록)
* SELECT * FROM users WHERE phone LIKE '02-%';
  * 지번이 02- 인 사람들 (이후값은 중요치않음)



### ORDER BY

* 기준이 될 column을 정해 정렬 (기본값 오름차순)
  * ASC : 오름차순
  * DESC : 내림차순
* 여러 기준을 잡는 경우 먼저 선언한 것이 우선



### GROUP BY

* 행 집합에서 요약 행 집합을 만듬(???)
* 문장에 WHERE 절이 포함된 경우 반드시 WHERE 뒤에 작성

* SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
* SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name;



### ALTER TABLE

* table 이름 변경
  * ALTER TABLE articles RENAME TO news;
* 테이블에 새로운 column 추가
  * NOT NULL 설정을 가진 column 을 추가하려면 기본값 설정이 필요
  * ALTER TABLE news ADD COLUMN subtitle TEXT NOT NULL DEFAULT '소제목';
* column 이름 수정 (v3.25~)
  * ALTER TABLE news RENAME COLUMN contetnt TO content;
* Drop column (v3.35~)
  * ALTER TABLE news DROP COLUMN subtitle;



