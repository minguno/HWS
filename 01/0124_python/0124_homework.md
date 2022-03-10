# 0124_homework



## 1. 모음은 몇 개나 있을까?

```python
def count_vowels(word):
    L = ['a', 'e', 'i', 'o', 'u']
    cnt = 0
    for i in L:
        if i in word:
            cnt += word.count(i)
    
    return cnt
```

## 2. 문자열 조작

```typescript
(4) .strip([chars])은 특정 문자를 지정하면, 양쪽에서 해당 문자를 찾아 제거한다. 특정 문자를 지정하지 않으면 오류가 발생한다.
=> default 값은 공백이며, 특정 문자를 지정하지 않을 시 양 끝의 공백을 제거한다.
```

## 3. 정사각형만 만들기

```python
def only_square_area(L1, L2):
    result = []
    for j in L1:
        for i in L2:
            if i == j:
                result.append(i * i)
    return result
```

