# 0406_workshop

## 0-1. 사전 준비

1. 가상환경 생성 & 활성화
2. django 3.2.12 설치
3. `runserver`

## 0-2. 기본 설정

1. 프로젝트 이름 `crud`, 앱 이름 `articles` 생성 & 출생신고
2. 상속시킬 `base.html` 작성
   - `manage.py`와 같은 레벨에 `templates/base.html/` 생성
   - `crud/settings.py`에 `BASE_DIR` `'templates'`로 지정
   - `crud/urls.py`에 `include` 불러와서 `articles.urls`로 경로 생성
   - `articles/urls.py` 생성
3. 제공된 이미지와 같아지도록 `settings.py` 지역, 언어 설정
   - `LANGUAGE_CODE = 'ko-kr'`
   - `TIME_ZONE = 'Asia/Seoul'`

## 1. Model

```python
# articles/models.py
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

```python
# articles/forms.py
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        # 유효성 검사를 진행할 필드
        fields = ('title', 'content')
```

DB에 올리기

```bash
$ python manage.py makemigrations
```

```bash
$ python manage.py migrate
```

## 2. Url

```python
# articles/urls.py
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # http://localhost:8000/articles/
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
]
```

## 3. View

```python
# articles/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)

    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)
```

## 4. Template

- index.html

```django
{% extends 'base.html' %}

{% block content %}

<header class="mb-4">
  <h1 class="mb-2">Articles</h1>
  
  <a href="{% url 'articles:create' %}">CREATE</a>
</header>

{% for article in articles %}
  <article>
    <p>글 번호: {{ article.pk }}</p>
    <p>글 제목: {{ article.title }}</p>
    <p>글 내용: {{ article.content }}</p>

    <a href="{% url 'articles:detail' article.pk %}">DETAIL</a>
  </article>
  <hr>

{% endfor %}

{% endblock content %}
```

- create.html

```django
{% extends 'base.html' %}

{% block content %}
  <h1>CREATE</h1>

  <form action="{% url 'articles:new' %}" method="POST">
    {% csrf_token %}
    <div class='mb-1'>
      <label for="title">제목: </label>
      <input type="text" id='title' name='title'>
    </div>
    <div>
      <label for="content">Content: </label>
      <textarea name="content" id="content" cols="30" rows="10"></textarea>
    </div>
    <button>CREATE</button>
  </form>

  <hr>
  <a href="{% url 'articles:index' %}">BACK</a>

{% endblock content %}
```

- detail.html

```django
{% extends 'base.html' %}

{% block content %}

<h1>Detail</h1>
<h2>{{ article.title }}</h2>
<p>{{ article.content }}</p>
<p>작성일: {{ article.created_at }}</p>
<p>수정일: {{ article.updated_at }}</p>

<a href="{% url 'articles:index' %}">BACK</a>
{% endblock content %}
```

