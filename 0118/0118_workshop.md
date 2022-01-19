# 0118_workshop



## 1. 간단한 N의 약수

```python
N = int(input())

if 1 <= N <= 1000:
    divisor = []
    for i in range(1, N + 1):
        if N % i == 0:
            divisor.append(i)

    # 출력 방법 1
    print(*divisor)
    # 출력 방법 2
    divisor_new = [str(a) for a in divisor]
    print(' '.join(divisor_new))
```

## 2. 중간값 찾기

```python
numbers = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
    51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
    52, 90,60, 49, 31, 12, 99, 94, 11, 25, 24
]

numbers.sort()
median = len(numbers) // 2
print(numbers[median])
```

## 3. 계단 만들기

```python
number = int(input())

if number > 0:
    stairs = []
    for i in range(1, number + 1):
        if i <= number:
            stairs.append(i)
            print(*stairs)
else:
    print('자연수를 입력하세요.')
```