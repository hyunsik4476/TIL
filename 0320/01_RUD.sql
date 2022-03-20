-- SQLite
-- pk 를 포함한 테이블 읽어오기
SELECT rowid, * FROM classmates;

SELECT rowid, name FROM classmates;

SELECT rowid, name FROM classmates LIMIT 1;
-- 위에서 3번째 순서에 있는 1개 행 불러오기
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
-- 조건에 맞는 행의 pk와 name 불러오기
SELECT rowid, name FROM classmates WHERE address = '서울';
-- 중복을 제외하고 읽기
SELECT DISTINCT age FROM classmates;

DELETE FROM classmates where rowid=5;

INSERT INTO classmates VALUES ('최번개', 28, '부산');
-- 지워진 pk 5 를 재활용함
-- .. PRIMARY KEY AUTOINCREMENT 옵션으로 재사용 안하게 가능

-- address 값이 없으므로 안됨 (NOT NULL 설정시)
INSERT INTO classmates VALUES ('장거한', 99);

UPDATE classmates SET name='홍길동', address='제주도' where rowid=5;

