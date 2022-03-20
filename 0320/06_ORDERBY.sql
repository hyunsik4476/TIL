-- SQLite

SELECT * FROM users ORDER BY age ASC LIMIT 10;
-- 정렬의 기준을 여러개를 줬을 때는 앞에 있는 column 기준으로 먼저 정렬
SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;

SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;

SELECT * FROM users ORDER BY age ASC, balance DESC LIMIT 10;