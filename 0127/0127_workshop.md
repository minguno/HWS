# 0127_workshop



## 1. 도형 만들기

```python
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle(Point):

    # 강제성은 전혀 없는 type 표시이고 그렇기 때문에 '='로 대체 가능하다
    def __init__(self, p1: Point, p2: Point):
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
그러나 자식 클래스 Rectangle의 생성자 메서드 매개 변수명과 달라지므로 정의가 길어졌을 때 코드가 쉽게 꼬이거나 가독성이 떨어질 가능성이 높다.
'''
```



## 궁금한 점

- 상속에 있어 `Point` 클래스의 매개변수를 어떻게 `Rectangle` 클래스 매개변수에 강제하는지? 

  => 사실상 Point 클래스의 인스턴스인지 아닌지 모른다 (강제성 X)
  
  => 개발자가 코드를 짤 때 저 자리에 Point 클래스의 인스턴스를 받을 거라고 가정하고 짜기 때문에 가능하다
  
  => 본인이 작성한게 아니고서야 전체 코드를 쭉 읽어봐야만 알 수 있는데,
  
  ```python
  def __init__(self, p1: Point, p2: Point)
  ```
  
  ​	이런 식으로 `p1은 Point 클래스의 인스턴스입니다`를 명시적으로 나타내주면 더 원활한 소통을 할 수 있다