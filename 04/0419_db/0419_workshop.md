# 0419_workshop



## accounts/views.py

```python
def profile(request, username):
    user_info = get_object_or_404(get_user_model(), username=username)
    context = {
        'user_info': user_info,
    }
    return render(request, 'accounts/profile.html', context)


@require_POST
def follow(request, user_pk):
    you = get_object_or_404(get_user_model(), pk=user_pk)
    me = request.user
    # 로그인 된 유저와 팔로우 하려는 유저가 같지 않다면
    if me.is_authenticated:
        if me.pk != you.pk:
            # 로그인 된 유저(me)가 이미 이 사람(you)의 팔로워로 등록되어 있다면
            if you.followings.filter(pk=me.pk).exists():
                you.followings.remove(me)
            else:
                you.followings.add(me)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')
```

## accounts/models.py

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```

## profile.html

```django
{% extends 'base.html' %}

{% block content %}
  <h1>{{ user_info.username }} 프로필</h1>
  <hr>

  {% with followers=user_info.followers.all followings=user_info.followings.all %}
    <div>
      팔로워 : {{ followings|length }}
    </div>
    <div>
      팔로우 : {{ followers|length }}
    </div>

    <div>
      {% if user != user_info %}
        <form action="{% url 'accounts:follow' user_info.pk %}" method="POST">
          {% csrf_token %}
          {% if user in followers %}
            <button>Unfollow</button>
          {% else %}
            <button>Follow</button>
          {% endif %}
        </form>
      {% endif %}
    </div>
  {% endwith %}

  <h2>작성한 글 모음</h2>
  {% for article in user.article_set.all %}
    <p>{{ article.title }}</p>
  {% endfor %}
  <h2>작성한 댓글 모음</h2>
  {% for comment in user.comment_set.all %}
    <p>{{ comment.content }}</p>
  {% endfor %}

  <a href="{% url 'articles:index' %}">[back]</a>

{% endblock content %}
```

## 결과 화면

![image-20220421233647041](C:\Users\meh\AppData\Roaming\Typora\typora-user-images\image-20220421233647041.png)

![image-20220421233513925](C:\Users\meh\AppData\Roaming\Typora\typora-user-images\image-20220421233513925.png)