-- SQLite

INSERT INTO classmates (name, id) VALUES ('홍길동', 23);

INSERT INTO classmates VALUES ('홍길동', 30, '서울');

SELECT * FROM classmates;

SELECT rowid, * FROM classmates;

-- 테이블 삭제
DROP TABLE classmates;

-- pk 포함한 테이블
CREATE TABLE classmates (
  id INTEGER PRIMARY KEY, -- pk 속성은 타입을 반드시 INTEGER
  name TEXT NOT NULL,
  age INT NOT NULL,
  address TEXT NOT NULL
);

-- pk 가 명시된 테이블에 데이터를 채워야 할 경우
INSERT INTO classmates (name, age, address) VALUES ('홍길동', 30, '서울');

CREATE TABLE classmates (
  name TEXT NOT NULL,
  age INT NOT NULL,
  address TEXT NOT NULL
);

INSERT INTO classmates VALUES
('홍길동', 30, '서울'),
('김철수', 30, '대전'),
('이영희', 26, '광주'),
('노진구', 29, '구미'),
('최번개', 28, '부산');
