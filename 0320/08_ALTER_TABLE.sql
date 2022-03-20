-- SQLite
CREATE TABLE articles (
  title TEXT NOT NULL,
  contetnt TEXT NOT NULL
);

INSERT INTO articles (title, contetnt) VALUES ('1번제목', '1번내용');

-- 테이블 이름 변경
ALTER TABLE articles RENAME TO news;

-- column 추가하기
ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL;
-- 새로 추가할 필드에 대한 정보가 없어 NOT NULL 추가가 불가능
-- 오류 발생
-- NOT NULL 설정을 빼던지, 기본값을 추가해야함

-- NOT NULL 빼고 추가, datetime 함수 써보기
ALTER TABLE news ADD COLUMN created_at TEXT;
INSERT INTO news VALUES ('2번제목', '2번내용', datetime('now'));

-- DEFAULT 옵션을 추가해서 NOT NULL 유지하기
ALTER TABLE news ADD COLUMN subtitle TEXT NOT NULL DEFAULT '소제목';

-- column 에 있는 오타 RENAME COLUMN 으로 고치기
ALTER TABLE news RENAME COLUMN contetnt TO content;
