# 0119_homework



## 1. Built-in 함수

1. `print()`
2. `map()`
3. `len()`
4. `sort()`
5. `round()`
6. `input()`

## 2. 정중앙 문자

```python
def get_middle_char(word):
    if len(word) % 2 == 0:
        return word[int(len(word) / 2 - 1): int(len(word) / 2 + 1)]
    else:
        return word[int(len(word) // 2)]

print(get_middle_char('ssafy'))
print(get_middle_char('coding'))
```

## 3. 위치 인자와 키워드 인자

```python
# (4) 키워드 인자 다음에 위치 인자(name=)이 올 수 없기 때문
ssafy(name='길동', '구미')
```

## 4. 나의 반환값은

```python
10
```

## 5. 가변 인자 리스트

```python
def my_avg(*args):
    total = 0
    for i in args:
        total += i
    mean = total / len(args)
    return mean

print(my_avg(77, 95, 83, 80, 70))
```

