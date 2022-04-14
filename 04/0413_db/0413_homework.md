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

```python
# views.py

from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

@login_required
@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')


def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)
```

위와 같은 함수가 작성되어 있다. 만약 비로그인 사용자가 삭제를 시도한다면, django는 해당 사용자를 url에 next 파라미터가 붙은 login 페이지로 redirect한다 -> `/accounts/login/?next=/articles/1/delete/`

### 1. redirect된 로그인 페이지에서 로그인에 성공했을 때 발생하는 HTTP response status code를 작성하고 이 오류가 발생한 원인을 작성하시오

`405 Method Not Allowed` 에러가 발생한다. 

next 파라미터에 delete와 article.pk가 포함된 login 페이지에서 로그인 시에는 해당 url로 GET 요청을 보내게 되지만 delete 함수에는 `@require_POST` 속성이 있어 POST 요청에만 동작하기 때문이다.

### 2. 위에서 발생한 오류를 해결하기 위해 다음과 같이 동작하는 코드로 수정하시오.

- 게시글 삭제는 HTTP Post method로만 가능하다
- 인증되지 않은 사용자가 게시글 삭제를 시도하는 경우, 해당 게시글 상세페이지로 redirect 되도록 한다.

```python
@login_required
def delete(request, article_pk):
    if request.method == 'POST':
	    article = get_object_or_404(Article, pk=article_pk)
	    article.delete()
    return redirect('articles:index')
```
