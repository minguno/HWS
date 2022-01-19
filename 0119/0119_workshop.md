# 0119_workshop



## 1. List의 합 구하기

```python
def list_sum(L):
    total = 0
    for i in L:
        total += i
    return total

print(list_sum([1, 2, 3, 4, 5]))
```

## 2. Dictionary로 이루어진 List의 합 구하기

```python
dic = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]

def dict_list_sum(lst):
    total = 0
    # 리스트 안에 딕셔너리 인자를 하나씩 꺼내와서
    for i in range(len(lst)):
        # 각 딕셔너리의 'age' key 값에 해당하는 value를 변환값을 담을 변수에 더해준다
        total += lst[i]['age']
    return total

print(dict_list_sum(dic))
```

## 3. 2차원 List의 전체 합 구하기

```python
L = [
    [1],
    [2, 3],
    [4, 5, 6],
    [7, 8, 9, 10]
]

def all_list_sum(lst, val = 0):
    for i in lst:
        # 리스트 인자가 리스트일 때, 정의한 함수를 다시 돌리는 조건문
        if type(i) == list:
            val += all_list_sum(i)
        # 2차원 리스트를 뚫고 정수 인자에 도달 했을 때 총합 변수에 더해주기
        else:
            val += i
    return val

print(all_list_sum(L))
```

