# 0419_homework



## 1. M:N True or False

1. Django에서 1:N 관계는 ForeignKeyField를 사용하고, M:N 관계는 ManyToManyField를 사용한다 **(T)**
2. ManyToManyField를 설정하고 만들어지는 테이블 이름은 *"앱이름`_`클래스이름`_`지정한 필드이름"*의 형태로 만들어진다. **(T)**
3. ManyToManyField의 첫번째 인자는 참조할 모델, 두번째 인자는 related_name이 작성되는데 두 가지 모두 필수적으로 들어가야 한다. **(F)**
   - 참조할 모델을 제외하고는 `related_name`, `through`, `summetrical` 모두 옵션이다

## 2. Like in templates

```python
class Artciel(models.Model):
    ...
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delelete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
```

```django
{% for article in articles %}
  <p>{{ article.title }}</p>
  <form action="{% url 'articles:likes' article.pk %}" method="POST">
    {% csrf_token %}
    {% if request.user in article.like_articles.all %}
      <button>좋아요 취소</button>
    {% else %}
      <button>좋아요</button>
    {% endif %}
  </form>
  <span>{{ article.like_articles.all|length }}명이 이 글을 좋아합니다.</span>
{% endfor %}
```

## 3. Follow in views

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```

```python
app_name = 'accounts'
urlpatterns = [
    ...,
    path('<int:pk>/follow/', views.follow, name='follow'),
]
```

```python
from django.contrib.auth import get_user_model

User = get_user_model()

@require_POST
def follow(request, user_pk):
    person = get_object_or_404(User, pk=user_pk)
    user = request.user
    
    if user != person:
        if person.followers.filter(pk=user.pk).exists():
            person.followers.remove(user)
        else:
            person.followers.add(user)
    return redirect('accounts:profile', person.username)
```

## 4. User AttributeError

![image-20220419023606236](0419_homework.assets/image-20220419023606236.png)

`UserCreationForm`이나 `UserChangeForm`과 같이 django 내부적으로 있는 User Form을 커스텀하지 않고 사용했을 때 이러한 에러가 발생할 수 있다. 해결을 위해선 `CustomUserCreationForm`과 `CustomUserChangeForm`을 사용해서 커스텀해줘야 한다. 

혹은 models.py에서 User 모델을 사용할 때 settings의 AUTH_USER_MODEL 대신 get_iser_model()을 사용했기 때문일 수 있다. 해결을 위해선 전자로 바꿔주어야 한다.

## 5. related_name

```python
# articles/models.py

from django.db import models
from django.conf import settings

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
```

Article과 User의 관계를 설정하는데 위의 경우 user로 1:N, like_users로 M:N 관계 두 개가 존재하기 때문에 Manager의 이름이 같아져 `User.article_set.all()` 명령어가 두 관계 중 참조해야 할 관계를 구분할 수 없어 충돌하게된다. 

둘 중 하나의 모델에 꼭 `related_name`을 필수적으로 작성해줌으로써 역참조시 Manager 이름을 구분지어준다. 

## 6. Follow templates

3번과 같은 `urls.py`와 `models.py` 정보가 담겨져 있다.

```django
<!-- accounts/profile.html -->
<h1>{{ person.username }}'s profile</h1>

<div>
  <div>
    팔로잉: {{ person.followings.all|length }}
    팔로워: {{ person.followers.all|length }}
  </div>
  {% if request.user != person %}
    <div>
      <form action="{% url 'accounts:follow' person.pk %}" method="POST">
        {% csrf_token %}
        {% if request.user in person.followers.all %}
          <button>Unfollow</button>
        {% else %}
          <button>Follow</button>
        {% endif %}
      </form>
    </div>
  {% endif %}
</div>
```

