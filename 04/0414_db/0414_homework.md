# 0414_homework



### 제시된 조건

1. 지점별 편의점들이 존재한다.
2. 각 상품들은 특정 조건별로 분류 할 수 있다.
3. 단, User는 고려하지 않는다.

## ERD (Entity-relationship Diagram)

![image-20220414221806313](C:\Users\meh\AppData\Roaming\Typora\typora-user-images\image-20220414221806313.png)

## models.py

```python
from django.db import models

# Create your models here.
class Branch(models.Model):
    branch_name = models.CharField(max_length=20)
    revenue = models.IntegerField()
    open_date = models.DateTimeField(auto_now_add=True)

    
class Product(models.Model):
    product_name = models.CharField(max_length=20)
    expiration_date = models.CharField(max_length=10)
    made_in = models.CharField(max_length=20)
    
    
class BranchProduct(models.Model):
    branch = models.ForeignKey(Brawnch, on_delete=models.CASCADE)
    product = models.FroeignKey(Product, on_delete=models.CASCADE)
```

## Rationale

User를 고려하지 않기 때문에 User 모델을 불러오진 않는다.

지점별 편의점을 나타내기 위한 Branch 모델과 편의점의 상품을 나타내기 위한 Product 모델을 작성해주고 이들의 관계를 나타내는 BranchProduct 모델을 생성한 후 ForeignKey로 엮어줬다.