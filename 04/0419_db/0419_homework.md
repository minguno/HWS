# 0419_homework




## 1. MTV

Django는 MTV로 이루어진 Web Framework다.

M : Model

- 데이터베이스를 관리하는 역할을 한다.

T : Template

- 사용자에게 보여지는 레이아웃을 관리한다.

V : View

- 중앙 컨트롤러 역할을 한다.

## 2. 404 Page not found

기본 `http://localhost:8000/` 페이지에 접속하게 되면 `Page not found (404)` 에러가 발생한다. 이때 index.html을 렌더링하고자 할 때 `crud` 프로젝트의 `articles`에서 index.html 파일을 렌더링 하는 `index` 이름의 view 함수를 작성학시오.

```python
from django.contrib import admin
from django.urls import path, include
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('', views.index, name='index'),
]
```

## 3. templates and static

Django 프로젝트는 기본적으로 render 할 html과 같은 template 파일과 css, js와 같은 static 파일을 앱 폴더 내부의 templates와 static 이름의 폴더에서 찾는다. 만약 해당 위치가 아닌 임의의 위치에 파일을 위치 시키고 싶으면 `settings.py` 파일의 `TEMPLATES`와 `STATICFILES_DIRS`라는 변수에 담긴 리스트의 요소를 정의하면 된다.

## 4. migration

```python
# articles/models.py

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

1. 마이그레이션 생성

   ```bash
   $ python manage.py makemigrations
   ```

2. 마이그레이션 DB 반영 여부 확인

   ```bash
   $ python manage.py showmigrations
   ```

3. 마이그레이션에 대응되는 SQL문 출력

   ```bash
   $ python manage.py sqlmigrate articles <파일이름>
   ```

4. 마이그레이션 파일의 내용을 DB에 최종 반영

   ```bash
   $ python manage.py migrate
   ```

## 5. ModelForm True of False

1. `POST`와 `GET` 방식은 의미론상의 차이이며 실제 동작 방식은 동일하다. **(F)**
   - 서버의 DB를 수정, 추가, 삭제 가능하게 해주는 건 POST 요청만 가능하다
2. `ModelForm`과 `Form Class`의 핵심 차이는 Model의 정보를 알고 있는지의 여부이다. **(T)**
3. `AuthenticationForm`은 `User` 모델과 관련된 정보를 이미 알고있는 `ModelForm`으로 구성되어 있다. **(T)**
4. `ModelForm`을 사용할 때 Meta 클래스에 fields 관련 옵션은 반드시 작성해야 한다. **(T)**

## 6. media 파일 경로

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'crud' / 'uploaded_files'
```

## 7. DB True or False

1. RDBMS를 조작하기 위해서 SQL문을 사용한다. **(T)**
2. SQL에서 명령어는 반드시 대문자로 작성해야 동작한다. **(F)**
   - 소문자여도 똑같이 작동하는데 가독성을 위한 약속이다.
3. 일반적인 SQL문에서는 세미콜론(;)까지를 하나의 명령어로 간주한다. **(T)**
4. SQLite에서 .tables, .headers on과 같은 dot으로 시작하는 명령어는 SQL문이 아니다. **(T)**
5. 하나의 데이터베이스 안에는 반드시 한 개의 테이블만 존재해야 한다. **(F)**

## 8. on_delete

`ProtectedError`를 발생시켜 참조 된 객체, 즉 게시글과 댓글의 관계에서 댓글이 존재하는 게시글은 삭제할 수 없도록 하는 코드를 작성하시오.

```python
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    
clss Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.PROTECT)
```

## 9. Like in models

Article 모델과 User 모델을 M:N 관계로 설정하여 '좋아요' 기능을 구현하려 한다.

```python
from django.db import models
from django.conf import settings

class Article(models.Model):
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManytoManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
```

## 10. Follow in models

'팔로우' 기능을 구현하기 위해 아래와 같은 모델을 작성하였다.

```python
# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```

Migration 작업 이후 DB에 만들어지는 중개 테이블의 이름은 `accounts_user_followings`이고 id를 제외한 해당 테이블의 컬럼은 `from_user_id`와 `to_user_id`이다.