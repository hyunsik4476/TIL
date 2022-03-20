-- SQLite
-- 각 성씨가 몇 명씩 있는지?
SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
