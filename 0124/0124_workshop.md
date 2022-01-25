# 0124_workshop



## 1.  평균 점수 구하기

```python
def get_dict_avg(dic):
    sum = 0
    for value in dic.values():
        sum += value
    
    return sum / len(dic)
```

## 2. 혈액형 분류하기

```python
# 방법 1
def count_blood(L):
    dic = {}
    blood_type = ['A', 'B', 'P', 'AB']
    for key in blood_type:
        dic[key] = L.count(key)
    return dic

```

```python
# 방법 2
def count_blood(L):
    result = {}
    for blood in blood_list:
        if blood not in result:
            result[blood] = 1
        else:
            result[blood] += 1
    return result
```

