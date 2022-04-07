# 0407_homework

```python
# articles/views.py
from django.shortcuts import render, redirect
from .forms import ArticleForm

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArtcielForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```



## 1. 왜 변수 context는 if else 구문과 동일한 레벨에 작성 되어있는가?

POST 요청일 때 유효성 검사를 통과하지 못하는 경우, 에러 메세지를 화면에 보여주기 위해 context를 지문과 같이 구성해준다.

## 2. 왜 request의 http method는 POST 먼저 확인하도록 작성하는가?

GET 요청을 if문으로 올리면 유효성 검사를 통과하지 못한 POST의 form을 위해 context과 render 반환값을 중복으로 작성해줘야 하는 불편함이 있다.
