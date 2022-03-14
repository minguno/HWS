# 0314_homework



## 1. SQL 용어 및 개념

### 스키마 Schema

: 관계형 데이터베이스 (RDBMS) 에서 구조와 제약조건에 관련한 전반적인 명세를 기술 한 것

### 테이블 Table

: 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합

### 컬럼 Column

: 고유한 데이터 형식이 지정되는 열

### 레코드 Record

: 단일 구조 데이터 항목을 가리키는 행

### 기본 키 Primary key

: 각 행의 고유 값

## 2. SQL 문법

DML은 Data Manipulation Language로, DB에서 데이터를 저장, 조회, 수정, 삭제 등을 하기 위한 명령어를 뜻한다

UPDATE, DELETE, SELECT 모두 DML의 한 종류이나 CREATE은 RDBMS를 정의하는 명령어이기 때문에 DDL로 분류된다

## 3. RDBMS

관계형 데이터베이스 관리 시스템 Relational Databse Management System 은 관계형 모델을 기반으로 하는 데이터베이스 관리시스템을 의미한다

모든 데이터를 2차원의 테이블 형태 (row와 columns의 관계) 로 표현한다

### Oracle

* 가장 널리 사용되는 RDBMS
* 관계형 모델을 객체 관계형 모델로 확장하여 복잡한 비즈니스 모델을 관계형 데이터베이스에 저장 가능하다

### MySQL

* 무료 오픈소스로 인기있는 DB 중 하나
* 매우 빠른 서버로 안정적이고 확장 가능하며 사용이 용이하다

### PostgreSQL

* 복잡한 데이터 워크로드를 안전하게 저장하며 SQL 언어를 사용하고 확장하는 오픈 소스 객체 관계형 데이터베이스 시스템 (ORDBMS)
* 아키텍처, 안정성의 데이터 무결성, 확장성 등 혁신적인 솔루션과 성능을 지속적으로 제공한다

## 4. INSERR INTO

아래와 같은 스키마를 가지는 테이블이 있을 때 틀린 문장을 고르시오

```sql
CREATE TABLE classmates (
	name TEXT,
	age INT,
	address TEXT
);
```

```sql
-- (1)
INSERT INTO classmates (name, age, address)
VALUES('홍길동', 20, 'seoul');
-- (2)
INSERT INTO classmates VALUES('홍길동', 20, 'seoul');
-- (3) (X)
insert into classmates
values(address='seoul', age=20, name='홍길동');
-- (4)
insert into classmates (address, age, name)
values('seoul', 20, '홍길동');
```

대문자 소문자는 명령어 자체에 영향이 없고 가독성을 위한 것이다

모든 필드에 값을 갖는 데이터의 경우 column 값 나열을 생략할 수 있다

Django와 같이 직접 필드값에 지정하는 형식은 지원하지 않기 때문에 정답은

(3)

## 5. 와일드카드 문자

|                % percent sign                |                 _ underscore                  |
| :------------------------------------------: | :-------------------------------------------: |
| 이 자리에 문자열이 있을 수도, 없을 수도 있다 | 반드시 이 자리에 한 개의 문자가 존재해야 한다 |

|   와일드카드 패턴    |                     의미                      |
| :------------------: | :-------------------------------------------: |
|         2 %          |                2로 시작하는 값                |
|         % 2          |                 2로 끝나는 값                 |
|        % 2 %         |                2가 들어가는 값                |
|        _ 2 %         | 아무 값이 하나 있고 두 번째가 2로 시작하는 값 |
|       1 _ _ _        |          1로 시작하고 총 4자리인 값           |
| 2 _ % _ % OR 2 _ _ % |        2로 시작하고 적어도 3자리인 값         |