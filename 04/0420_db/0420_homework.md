# 0420_homework

## 1. T/F

1. URI는 정보의 자원을 표현하고, 자원에 대한 행위는 HTTP Method로 표현한다. **(T)**
  - URI는 리소스를 식별하는 역할을 하고, HTTP Method는 리소스에 대한 행위를 규정한다.
2. HTTP Method는 GET과 POST 두 종류가 있다. **(F)**
  - `PUT`, `DELETE` 등 리소스에 대한 행위를 나타내는 여러가지의 종류가 있다.
3. ‘https://www.fifa.worldcup/teams/team/43822/create' 는 계층 관계를 잘 표현한 RESTful한 URI라고 할 수 있다. **(F)**
  - RESTful 하다는 것은 URI를 통해서가 아니라 HTTP Method을 통해서 리소스에 대한 행위를 규정한다는 의미이다. 따라서 URI에서 CRUD등의 행위를 표현한 것은 RESTful한 것이 아니라고 할 수 있다.



## 2. 다음의 HTTP status code의 의미를 간략하게 작성하시오

- 200
  - OK. 정상작동
- 400
  - BAD REQUEST. 잘못된 요청
- 401
  - UNAUTHORIZED. 권한이 없는 접근.
- 403
  - FORBIDDEN. 금지된 요청
- 404
  - NOT FOUND. 찾을 수 없는 요청
- 500
  - INTERNAL SERVER ERROR. 내부 서버에서의 에러



## 3. SutdentSerializer

```python
# serializers.py

from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'
```





## 4.Serializers의 의미

Serializers는 API REST를 정의한다.

Serializers는 쿼리셋이나 모델 인스턴스와 같은 파이썬 고유 객체를 `JSON`, `XML` 같은 content 타입으로 쉽게 파싱하여 API를 표현하는 역할을 한다.

