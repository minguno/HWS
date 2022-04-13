# 0413_homework



## 1. 1:N True or False

1. `ForeignKey`는 부모 테이블의 테이더를 참조하기 위한 키이다. **(T)**
   - `ForeignKey`는 1:N 관계에서 N에 해당하는 테이블이 부모테이블의 데이터를 참조하기 위한 키이다
2. 1:N 관계에서 1은 N의 데이터를 직접 참조할 수 있다. **(F)**
   - 1:N에서 1은 N의 데이터를 직접 참조할 수 있는 필드를 가지고 있지 않다. 따라서 `_set` manager를 통해 역참조 해줘야한다 e.g. 하나의 게시글 입장에서 모든 댓글 조회
3. `on_delete` 속성은 `ForeignKey` 필드의 필수 인자이다. **(T)**
   - 참조 무결성을 유지하기 위해 필수로 지정한다
4. 1:N 관계에서 외래 키는 반드시 부모 테이블의 `PrimaryKey`여야 한다. **(F)**
   - 고유한 값이면 가능하다

## 2. ForeignKey column name

```python
# models.py

from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=50)
    
class Comment(models.Model):
    answer = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
```

위의 코드를 바탕으로 테이블이 만들어 졌을 때, DB에 저장되는 ForeignKey 컬럼의 이름은 `answer_id`이고 테이블의 이름은 `articles_comment`이다.

## 3. 1:N model manager

2번 문제 모델 관계를 바탕으로 어느 template 페이지가 다음과 같이 작성되어 있을 때, 질문에 작성된 모든 댓글을 출력하고자 한다.

```django
{% for comment in question.comment_set.all %}
  <p>{{ comment.content }}</p>
{% endfor %}
```

## 4. next parameter

