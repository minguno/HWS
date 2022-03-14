-- (1) 테이블 생성
CREATE TABLE countries (
  id INTEGER PRIMARY KEY,
  room_num TEXT,
  check_in TEXT,
  check_out TEXT,
  grade TEXT,
  price INT
); 

-- (2) 데이터 추가
INSERT INTO countries (room_num, check_in, check_out, grade, price)
VALUES 
('B203', '2019-12-31', '2020-01-03', 'suite', 900),
('1102', '2020-01-04', '2020-01-08', 'suite', 850),
('303', '2020-01-01', '2020-01-03', 'deluxe', 500),
('807', '2020-01-04', '2020-01-07', 'superior', 300);

-- (3) 테이블의 이름 변경
ALTER TABLE countries RENAME TO hotels;

-- (4) 객실 가격을 내림차순 정렬하여 상위 2개의 room_num과 price 조회
SELECT room_num, price FROM hotels 
ORDER BY price DESC
LIMIT 2;

-- (5) grade 별 분류 & grade 개수를 내림차순 조회
SELECT grade, COUNT(grade) FROM hotels
GROUP BY grade
ORDER BY COUNT(grade) DESC;

-- (6) 객실의 위치가 지하 or 등급이 deluxe인 객실 모든 정보 조회
SELECT * FROM hotels
WHERE room_num LIKE 'B%' OR grade='deluxe';

-- (7) 지상층 객실 & 2020-01-04 체크인 목록을 price 오름차순 조회
SELECT * FROM hotels
WHERE room_num NOT LIKE 'B%' AND check_in='2020-01-04'
ORDER BY price;