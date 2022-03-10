# 0126_homework



## 1. Type Class

1. `int`
2. `float`
3. `obj`
4. `str`
5. `complex`
6. `dictionary`

## 2. Magic Method

1. `__init__` : constructor method (생성자)

   ```python
   class Menu():
   
       def __init__(self, food, price):
           self.food = food
           self.price = price
           print('음식 정보가 메뉴에 생성되었습니다.')
   
           
   dinner = Menu('pizza', 20000)
   # => 음식 정보가 메뉴에 생성되었습니다.
   ```

   인스턴스 객체가 생성될 때 자동으로 호출되는 함수이다. `food`와 `price` 인자를 정의해준 것과 같이 인스턴스를 생성할 때 인스턴스의 속성을 정의할 수 있다.

   

2. `__del__` : destructor method (소멸자)

   ```python
   class Menu():
   
       def __init__(self, food, price):
           self.food = food
           self.price = price
           print('음식 정보가 메뉴에 생성되었습니다.')
   
       def __del__(self):
           print('음식 정보가 메뉴에서 지워졌습니다.')
   
           
   dinner = Menu('pizza', 20000)
   del dinner
   # => 음식 정보가 메뉴에 생성되었습니다.
   # => 음식 정보가 메뉴에서 지워졌습니다.
   ```

   인스턴스 객체가 소멸되기 직전에 자동으로 호출되는 함수이다. `del <인스턴스>` 식으로 활용된다.

   

3. `__str__` 

   ```python
   class Menu():
   
       def __init__(self, food, price):
           self.food = food
           self.price = price
   
       def __str__(self):
           return f'오늘 메뉴는 {self.food}이다.\n{self.price}원을 현금으로 준비해!'
   
       
   dinner = Menu('마라샹궈', 20000)
   print(dinner)
   # => 오늘 메뉴는 마라샹궈이다.
   # => 20000원을 현금으로 준비해!
   ```

   특정 객체를 출력할 때 보여줄 내용의 format을 정의할 수 있다. 

   

4. `__repr__`

   ```python
   # repr() 함수에 대한 고찰
   import random
   
   print(repr('ABC')) # => 'ABC'
   print(repr(56), type(repr(56))) # => 56 <class 'str'>
   print(repr([1, 2, 3]), type(repr([1, 2, 3]))) # => [1, 2, 3] <class 'str'>
   print(repr(random), type(repr(random))) # => <module 'random' from 'C:\\Users... <ckass 'str'>
   ```

   `repr` 함수는 어떤 객체의 printable representation을 문자열의 형태로 반환한다. 마찬가지로 어떤 객체를 인자로 해서 `repr` 함수를 실행하면 해당 객체의 클래스에 정의된 `__repr__`를 실행한다.

   ```python
   class Menu():
   
       def __init__(self, food, price):
           self.food = food
           self.price = price
   
       def __repr__(self):
           return f'오늘의 추천 메뉴는 {self.food}입니다.\n{self.price}원을 지불하십시오.'
       
       def __str__(self):
           return f'오늘 메뉴는 {self.food}이다.\n{self.price}원을 현금으로 준비해!'
       
   
   dinner = Menu('마라샹궈', 20000)
   
   print(repr(dinner))
   # => 오늘의 추천 메뉴는 마라샹궈입니다.
   # => 20000원을 지불하십시오.
   print(str(dinner)) 
   # => 오늘 메뉴는 마라샹궈이다.
   # => 20000원을 현금으로 준비해!
   print(dinner)
   # => 오늘 메뉴는 마라샹궈이다.
   # => 20000원을 현금으로 준비해!
   ```

   - `__str__`과의 차이점?
     - 의도가 다르다
       - `str`은 목적 자체가 문자열화해서 반환하는 것이다. 객체를 추가적인 가공이다 다른 자료형이 호환될 수 있도록 문자열화하는 데 목적이 있다. `print()` 함수를 쓰면 `[5] + 5`가 `TypeError`가 반환되는 것과 달리 `int`, `str`, `list` 자료형이 문자열로 반환되는데, 이는 `__str__` 메소드를 내부적으로 구현하고 있기 때문에 가능하다.
       - `repr`은 객체를 인간이 이해할 수 있는 plain text(평문)으로 represent, 표현하는 것이 목적이다. Overriding 한다면, 단순 객체를 문자열화가 아닌 주소값을 반환하게 할 수도 있다.
   - 왜 두 함수의 반환값이 똑같/비슷한 건지?
     - 기본 내장 클래스에서 객체를 표현하는 것과 다른 데이터 타입과의 상호작용을 위한 이터페이스가 되는 것이 동일했기 때문이다.

## 3. Instance Method

1. `.index(x[, start[, end]])`: 문자열, 튜플이나 리스트에서 x 값이 첫 번째로 등장하는 index 값을 `int` 형태로 반환한다. 생략가능하지만 검색을 시작하는 범위도 지정할 수 있다. Default는 처음부터 끝까지이다.

2. `.count(x)`: 문자열, 튜플이나 리스트에서 x 값의 개수를 `int` 형태로 반환한다.

   => 순서에 의존하거나 반환하는 method는 unordered data type에는 적용이 불가능하다.

3. `.reverse()`: 리스트의 원소들 순서가 반대로 뒤집힌다. `sorted()`와 같이 단순 정렬이 아닌 원본 순서가 수정된다.

4. `.pop(key)`: 딕셔너리에서 해당 key를 제거한 뒤 삭제한 key를 반환한다. 입력된 key가 존재하지 않는 경우 `KeyError`를 일으킨다.

5. `.discard(x)`: 셋에서 x 값을 지운다. 없을 경우 `None`으로 반환된다.

## 4. Module Import

```python
from fibo import fibo_recursion as recursion
```

