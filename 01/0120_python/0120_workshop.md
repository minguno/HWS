# 0120_workshop



## 1. 숫자의 의미

```python
def get_secret_word(numbers):
    ASCII = ''
    for number in numbers:
        ASCII += chr(number)
    return f'\'{ASCII}\''
```

## 2. 내 이름은 몇일까?

```python
def get_secret_number(word):
    numbers = []
    for char in word:
        numbers.append(ord(char))
    return numbers
```

## 3. 강한 이름

```python
def get_strong_word(a, b):
    A, B = 0, 0
    for i in a:
        A += ord(i)
    for j in b:
        B += ord(j)
    if bool(A > B):
        return f'\'{a}\''
    return f'\'{b}\''
```

