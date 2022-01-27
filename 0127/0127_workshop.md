# 0127_workshop



## 1. 도형 만들기

```python
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle(Point):

    # 강제성은 전혀 없는 type 표시이고 그렇기 때문에 '='은 ':'로 대체 가능하다
    def __init__(self, p1 = Point, p2 = Point):
        self.p1 = p1
        self.p2 = p2

    def get_area(self):
        return abs((self.p2.x - self.p1.x) * (self.p1.y - self.p2.y))

    def get_perimeter(self):
        return abs((self.p2.x - self.p1.x) + (self.p1.y - self.p2.y)) * 2

    def is_square(self):
        if abs((self.p2.x - self.p1.x)) == abs((self.p1.y - self.p2.y)):
            return True
        else:
            return False


p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area()) # => 4
print(r1.get_perimeter()) # => 8
print(r1.is_square()) # => True
p3452 = Point(3, 7)
p4652 = Point(6, 4)
r1678 = Rectangle(p3452, p4652)
print(r1678.get_area()) # => 9
print(r1678.get_perimeter()) # => 12
print(r1678.is_square()) # => True
```

```python
# Rectangle class의 다른 생성자 메서드 정의 및 호출 방법 (대신 변수명을 다 바꿔줘야 한다)

def __init__(self, p1, p2):
	self.x1 = p1.x
	self.y1 = p1.y
	self.x2 = p2.x
	self.y2 = p2.y

'''
부모클래스의 인스턴스 변수명으로 호출한다 e.g. p1.x
만약 변수명이 point1 이었다면 point1.x
자식클래스 매개변수로 부모클래스 매개변수를 호출할 수 있다
self(자식클래스).매개변수 = 부모클래스 인스턴스 변수.부모클래스 매개변수
'''
```



## 궁금한 점

- 상속에 있어 `Point` 클래스의 매개변수를 어떻게 `Rectangle` 클래스 매개변수에 강제하는지? i.e. `p3`, `p4`는 정답을 출력하지만 `point3`, `poin4`는 에러가 나는 이유, `p3452`랑 `p4652`로 `r1678` 인스턴스 변수를 생성하면 정답을 출력하는 이유?

  => 파이썬은 type에 대한 강제가 적은편이라 사실상 Point인지 아닌지 모름 (확답은 X)