# 0126_workshop



## 1. pip

(1) 가짜 데이터를 가져올 수 있는 `faker` 라는 라이브러리를 설치한다

(2) Git bash

## 2. Basic Usages

(1) `faker라는 모듈에서 Faker class를 가져오기` 위한 코드이다.

(2) Faker는 `class`, fake는 `instance`이다.

(3) name()은 fake의 `instance method`이다.

## 3. Localization

```python
class Faker():
    
    def __init__(self, name):
        pass
```

## 4. Seeding the Generator

```python
# .seed() method

from faker import Faker

fake = Faker('ko_KR')
Faker.seed(4321)

print(fake.name()) # => 이도윤

fake2 = Faker('ko_KR')
print(fake2.name()) # => 이지후
```

`.seed()`는 `class method`이다. 

- 만약 인스턴스 메서드였다면, `class`인 `Faker`에서 메서드를 실행했을 때 `TypeError`가 났을 것이다.
- `class.seed(4321)`로 시작값을 고정해 놨기 때문에 두 인스턴스 `fake`와 `fake2` 둘 다 일정한 값만 반환한다.
- 용도는 해당 `class`의 모든 ` instance`에 적용하고 싶을 때 사용할 수 있다.

```python
# .seed_instance() method
from faker import Faker

fake = Faker('ko_KR')
fake.seed_instance(4321)

print(fake.name()) # => 이도윤

fake2 = Faker('ko_KR') # => 반환값이 계속 바뀐다.
print(fake2.name())
```

`.seed_instance()`는 `instance method`이다.

- 인스턴스인 `fake`로 호출했다. 
- 또한, 인스턴스 메서드는 해당 인스턴스 변수에만 영향력을 행사하기 때문에 시드값을 `4321`로 고정하여 `이도윤`만 반환되는 `fake` 인스턴스와 달리 고정 시드값이 없는 `fake2` 인스턴스는 매번 반환값이 달라진다.
- 용도는 특정 `instance`에만 고정값을 줄 때 사용할 수 있다.
