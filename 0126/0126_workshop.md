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



## Class와 instance에 대한 보충 설명

- `cls`와 `self`

  ```python
  @classmethod
  def 나는_클래스_전용_메서드(cls):
      # 클래스메서드니까 첫번째 인자에 자동으로 클래스 자신이 들어오는데,
     # 개발자들끼리 그냥 cls라고 줄여서 부르기로 약속 ㅎㅎ
  
     cls.num_of_dogs += 1 
  
  def 나는_인스턴스_메서드(self):
      # 인스턴스 메서드에서는 인자로 클래스가 안들어오니까
      # 만약 클래스에 접근하고 싶으면 cls가 아닌 "클래스명" 자체로 접근
      
      Doggy.num_of_dogs
  ```

- `인스턴스 메서드`와 `클래스 메서드`

  ```python
  from faker import Faker
  
  # 인스턴스는 어떤 이름의 변수를 찾을 때 인스턴스 -> 클래스 순으로 namespace를 탐색한다
  
  # Faker 클래스의 클래스변수 seed의 값을 1234로 지정
  Faker.seed(1234)
  
  # 인스턴스를 만들고 따로 인스턴스 변수를 설정하지 않는다
  fake1 = Faker('ko_KR') # 클래스 변수 seed값을 따라감
  fake2 = Faker('ko_KR') # 클래스 변수 seed값을 따라감
  fake3 = Faker('ko_KR') # 클래스 변수 seed값을 따라감
  
  print(fake1.name()) # seed = 1234의 첫 번째 이름 => 박경숙
  print(fake2.name()) # seed = 1234의 두 번째 이름 => 심은경
  print(fake3.name()) # seed = 1234의 세 번째 이름 => 김지연
  
  # fake1이 인스턴스 메서드인 seed_instance()를 이용해서 인스턴스 변수로 seed를 만든다
  fake1.seed_instance(4321)
  
  # 이제부터 fake1은 name()을 실행해서 이름을 만들 때 시드값으로 클래스 변수 cls.seed 말고 자기만의 변수 self.seed를 사용하게 된다
  print(fake1.name()) # seed = 4321의 첫 번째 이름 => 이도윤
  print(fake2.name()) # seed = 1234의 네 번째 이름 => 김주원
  print(fake3.name()) # seed = 1234의 다섯 번째 이름 => 강우진
  
  # fake2, fake3는 자기만의 seed가 없으므로 name()으로 이름을 만들 때 원래 존재하는 클래스의 seed 변수를 사용한다
  ```

- `클래스 변수`와 `인스턴스 변수`

  ```python
  class Doggy:
      # 클래스 변수
      num_of_dogs = 0
      birth_of_dogs = 0
      
      # __init__은 생성자 메서드 (인스턴스 생성시에 자동으로 호출되는 함수)
      # name, species는 인자다
      def __init__(self, name, species):
          # 속성 정의하기 -> d1.name만 해도 이름이 호출되게
          self.name = name
          self.species = species
          # 인스턴스 메서드에서 클래스 변수 호출할 때는 클래스 명(Doggy) 사용
          Doggy.num_of_dogs += 1
          Doggy.birth_of_dogs += 1
  
  # 인스턴스 변수        
  d1 = Doggy('쮸쮸', '푸들')
  ```

