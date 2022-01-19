# 0117_workshop



## 1. 세로로 출력하기

```python
for i in range(1, 11):
    print(i)
```

## 2. 거꾸로 세로로 출력하기

```python
for i in range(5, -1, -1):
    print(i)
```

## 3. N줄 덧셈

```python
number = int(input())

if number <= 10000:
    total_num = 0
    for num in range(1, number + 1):
        total_num += num
    print(total_num)
elif number > 10000:
    print('10000 이하의 정수를 입력하세요.')
```

