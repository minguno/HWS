# 0303_homework



## 1. 한국어로 번역하기

1) django 프로젝트를 한국어로 제공하기 위한 번역을 설정하려면 settings.py에서 `LANGUAGE_CODE` 변수에 `'ko-kr'` 값을 할당해야 한다.

   ```python
   LANGUAGE_CODE = 'ko-kr'
   ```

2) django의 번역 시스템을 활성화 할 것인지에 대한 on/off 결정을 하는 `USE_I18N`변수가 활성화되어 있어야 한다.

## 2. 경로 설정하기

```python
# urls.py
path('ssafy/', views.saffy)
```

## 3. Django Template Language

1. menus 리스트를 반복문으로 출력

   ```django
   {% for menu in menus %}
     <p>{{ menu }}</p>
   {% endfor %}
   ```

2. posts 리스트를 반복문을 활용하여 0번 글부터 출력하시오.

   ```django
   {% for post in posts %}
     <p>{{ forloop.counter0 }}번 글 : {{ post }}</p>
   {% endfor %}
   ```

3. users 리스트가 비어있다면 '현재 가입한 유저가 없습니다.' 텍스트를 출력하시오.

   ```django
   {% for user in uers %}
     <p>{{ user }}</p>
   {% empty %}
     <p>현재 가입한 유저가 없습니다.</p>
   {% endfor %}
   ```

4. 첫 번째 반복문일 때와 아닐 때를 조건문으로 분기처리 하시오.

   ```django
   {% if forloop.first %}
     <p>첫 번째 반복문 입니다.</p>
   {% else %}
     <p>첫 번째 반복문이 아닙니다.</p>
   {% endif %}
   ```

5. 출력된 결과가 주석과 같아지도록 하시오.

   ```django
   <!-- 5 -->
   <p>{{ 'hello'|length }}</p>
   <!-- My Name Is Tom -->
   <p>{{ 'my name is tom'|capfirst }}</p>
   ```

6. 변수 today에 datetime 객체가 들어있을 때 출력된 결과가 주석과 같아지도록 작성하시오.

   ```django
   <!-- 2020년 02월 02일 (Sun) PM 02:02 -->
   {{ today|date:"Y년 m월 d일 (D) A h:i" }}
   ```

## 4. Form tag with Django

1. form 태그의 속성인 action의 역할은 입력 데이터가 전송될 URL을 지정하는 것이다
2. form 태그에서 method는 입력 데이터 전달 방식을 지정, 다른 의미론 주어진 리소스가 수행할 작업을 나타내고 `GET`, `POST`, `PUT`, `DELETE` 등 종류가 다양하다. 요청에 의해 서버로부터 응답 받은 정보를 조회하는데 사용하는 요청의 방식으로 HTML 문서 한 장을 받는 것이 `GET`이다.
3. `/create/`