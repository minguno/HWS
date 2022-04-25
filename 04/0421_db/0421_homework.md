# 0421_homework

## 1. T/F

- JSON 포맷의 데이터로 응답하기 위해서는 반드시 DRF를 사용해야한다. **(F)**
  - django.core의 JsonResponse를 사용하거나, 직접 Json 형태로 응답도 가능하다.
- DRF가 제공하는 기본 Form을 통해서만 여러 HTTP Method를 테스트 해볼 수 있다. **(F)**
  - postman, swagger를 통해서 HTTP Method를 테스트 해볼 수 있다.
- api_view 데코레이터를 사용하지 않아도 HTTP Method 요청에 응답할 수 있다. **(F)**
  - DRF를 통한 요청에서는 api_view를 사용해야한다. 다른 방식의 요청에서는 응답 가능하다.
- Serializers는 쿼리 객체를 JSON 포맷으로 변환할 수 있는 python 데이터 타입으로 만들어준다. **(F)**
  - Serializers는 쿼리 객체를 JSON 포맷으로 변환할 수 있다.

## ST API 디자인 가이드

REST API 디자인 설계 시 가장 중요한 항목을 2가지로 요약한다면, "정보의 자원을 표현해야 하는 `URI`와 자원에 대한 행위를 표현하는 `HTTP Method`라고 할 수 있다."

## 3. 코드 작성

```python
# views.py

from rest_framework import status


@api_view(['POST'])
def create_article(request):
    serializer = ArticleSerializer(request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```