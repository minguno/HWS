# 0411_homework



## 1. Django User Model

```python
# from django.contrib.auth.models import User

class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.
    Username and password are required. Other fields are optional.
    """

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
```

## 2. Create user by ModelForm

새 유저를 생성하는 Django 내부에 정의된 ModelForm을 사용하기 위한 import 구문은

```python
from django.contrib.auth.forms import UserCreationForm
```

## 3. Django sessions

Django는 사용자가 로그인에 성공할 경우 **(a) Django DB의 django_session** 테이블에 세션 데이터를 저장한다. 그리고 브라우저의 쿠키에 세션 값이 발급되는데 이 세션 값의 key 이름은 **(b) session_id** 이다. 