# 0127_homework



## 1. Circle 인스턴스 만들기

```python
class Circle:
    # 클래스 변수
    pi = 3.14

    # 생성자 메서드
    def __init__(self, r, x, y):
        # 위치 인자로 매개변수 r, x, y를 전달 받을 수 있게 정의하는 구간
        self.r = r
        self.x = x
        self.y = y

    # 아래는 다 인스턴스 메서드
    def area(self):
        return self.pi * self.r * self.r

    def circumference(self):
        return 2 * self.pi * self.r

    # 매개변수를 튜플로 반환
    def center(self):
        return (self.x, self.y)

# 인스턴스 변수 생성
c1 = Circle(3, 2, 4) 
print(c1.area()) # => 28.259999999999998
print(c1.circumference()) # => 18.84
```

## 2. Dog과 Bird는 Animal이다

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')
    
    def eat(self):
        print(f'{self.name}! 먹는다!')


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        print(f'{self.name}! 달린다!')

    def bark(self):
        print(f'{self.name}! 짖는다!')


class Bird(Animal):

    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print(f'{self.name}! 푸드덕!')


# 자식클래스에서 인스턴스 메서드를 overriding 해준다
dog = Dog('멍멍이')
dog.walk()
dog.bark()

bird = Bird('구구')
# 부모클래스의 인스턴스 메서드를 상속받는다
bird.walk()
bird.eat()
bird.fly()
```

## 3. 오류의 종류

- `ZeroDivisionError`
  - 0으로 나누는 계산을 하려할 때 일어난다. 컴퓨터는 무한대를 담을 수 없기 때문.
- `NameError`
  - 정의되지 않는 변수를 호출할 때 일어난다
- `TypeError`
  - 자료형이 올바르지 못한 경우에 일어난다. e.g. int만 받을 수 있는 함수에 str 넣었을 때
- `IndexError`
  - 인덱스 범위를 넘어선 값이 들어갔을 때 호출이 불가능해서 일어난다
- `KeyError`
  - 딕셔너리에서 존재하지 않는 key로 접근한 경우에 일어난다
- `ModuleNotFoundError`
  - 불러오고자 하는 모듈이 존재하지 않을 때 일어난다. 따로 설치를 안했거나, 디렉토리에 없거나.
- `ImportError`
  - 불러오고자 하는 함수/클래스가 존재하지 않을 때 일어난다