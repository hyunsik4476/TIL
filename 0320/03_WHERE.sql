-- SQLite
CREATE TABLE users (
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTERGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTERGER NOT NULL
);
-- where 를 사용해 조건에 맞는 r 조회
SELECT * FROM users WHERE age >= 30;
-- 조건에 맞는 특정 column 만 조회
SELECT first_name FROM users WHERE age >= 30;

-- 여러개의 조건 걸기
SELECT age, first_name, last_name FROM users
WHERE age >= 30 AND last_name = '김';