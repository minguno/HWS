# 0125_workshop



## 1. 무엇이 중복일까

```python
def duplicated_letters(word):
    result = []
    for i in word:
        if word.count(i) > 1:
            if i not in result:
                result.append(i)
    
    return result

print(duplicated_letters('apple'))
print(duplicated_letters('banana'))
```

## 2. 소대소대

```python
def low_and_up(word):
    result = ''
    for i in range(len(word)):
        if i == 0 or i % 2 == 0:
            result += word[i].lower()
        else:
            result += word[i].upper()
    return result
```

## 3. 솔로 천국 만들기

```python
def lonely(iterable):
    result = []
    result.append(iterable[0])
    for i in range(1, len(iterable)):
        if iterable[i] != iterable[i - 1]:
            result.append(iterable[i])

    return result
```

