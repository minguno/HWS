# 0118_homework



## 1. Mutable & immutable

```python
# mutable
List, Set, Dictionary (value)
# immutable
String, Tuple, Range, Dictionary (key only)
```

## 2. 홀수만 담기

```python
L = []

for num in range(1, 51):
    if num % 2 == 1:
        L.append(num)
```

## 3. Dictionary 만들기

```python
names = ['강경은', '김민성', '김수연', '김수환', '김연준', '김영준', '김우석',
     '김한솔', '남은열', '노수지', '노용래', '노희진', '명은호', '문희철',
     '박소은', '박종선', '배성진', '원재호', '원찬호', '이동근', '이상현',
     '이재상', '이종민', '정호제', '이진영']

names.sort()

dictionary = {}
for i in range(len(names)):
    dictionary[names[i]] = 27

# 나이를 몰라서 하나로 통일했어요 ㅎ^ㅎ
```

## 4. 반복문으로 네모 출력

```python
n = 5
m = 9

for i in range(1, m + 1):
    if i == 1:
        print('*' * n)
    elif 1 < i <= (m - 1):
        print('*{}*'.format(' ' * (n - 2)))
    else:
        print('*' * n)
```

## 5. 조건 표현식

```python
temp = 36.5
if temp >= 37.5: print('입실 불가')
else: print('입실 가능')
```

## 6. 평균 구하기

```python
scores = [90, 89, 99, 83]

# 방법 1
# import numpy
# average1 = numpy.mean(scores)
# print(average1)

# 방법 2
print('{}'.format(sum(scores) / len(scores)))
```

