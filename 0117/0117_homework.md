# 0117_homework



## 1. Python 예약어

```python
import keyword
print(keyword.kwlist)
```

```python
False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
```

## 2. 실수 비교

```python
num1 = 0.1 * 3
num2 = 0.3

#방법 1
abs(num1 - num2) <= 1e-10

# 방법 2
import sys
abs(num1 - num2) <= sys.float_info.epsilon

# 방법 3
import math
math.isclose(num1, num2)

```

## 3. Escape sequence

```python
# 줄 바꿈
\n
# 탭
\t
# 백슬래시
\\
```

## 4. String interpolation

```python
name = '철수'

# 방법 1
print('안녕, %s야' % name)

# 방법 2
print('안녕, {}야'.format(name))

# 방법 3
print(f'안녕, {name}야')
```

## 5. 형 변환

```python
int('3.5')	# (5)
```

## 6. 네모 출력

```python
print('*'*n)
print('*{}*'.format(' '*(n-2)))
print('*{}*'.format(' '*(n-2)))
print('*{}*'.format(' '*(n-2)))
print('*{}*'.format(' '*(n-2)))
print('*{}*'.format(' '*(n-2)))
print('*{}*'.format(' '*(n-2)))
print('*{}*'.format(' '*(n-2)))
print('*'*n)
```

```python
*****
*   *
*   *
*   *
*   *
*   *
*   *
*   *
*****
```

## 7. 이스케이프 시퀀스 응용

```python
print('\"파일은 c:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다.\"\n나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지.\'')
```

## 8. 근의 공식

```python
r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
print('{} 또는 {}'.format(r1, r2))
```

