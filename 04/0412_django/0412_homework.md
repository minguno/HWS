# 0412_homework



## 1. User  Model BooleanField

User 모델에서 사용할 수 있는 칼럼 중 BooleanField로 정의 된 컬럼을 모두 작성하시오.

```python
class PermissionsMixin(models.Model):
    """
    Add the fields and methods necessary to support the Group and Permission
    models using the ModelBackend.
    """
    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )
    
    
class AbstractUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
```

## 2. Username max length

Django에서 기본적으로 사용하는 User 모델의 username 컬럼이 저장할 수 있는 최대 길이는 `150`자이다.

## 3. Login validation

단순히 사용자가 '로그인 된 사용자인지'만을 확인하기 위하여 User 모델 내부에 정의된 속성의 이름은 `@login_required`이다.

## 4. Login 기능 구현

```python
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

def login(request):
    if request.methd == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context) 
```

## 5. Who are you?

로그인을 하지 않았을 경우 template에서 user 변수를 출력했을 때 나오는 클래스의 이름은 `AnonymousUser`이다.

## 6. 암호화 알고리즘

Django에서 기본적으로 User 객체의 password 저장에 사용하는 알고리즘은 `PBKDF2`, 그리고 함께 사용된 해시 함수는 `SHA256`이다.

## 7. Logout 기능 구현

로그아웃 기능을 구현하기 위하여 다음과 같이 코드를 작성하였다. 로그아웃 기능을 실행 시 문제가 발생한다고 할 때 그 이유와 해결 방법을 작성하시오.

```python
def logout(request):
    logout(request)
    return redirect('accounts:login')
```



개발자가 정의하는 `logout` 함수랑 django 내부적으로 불러온 `logout` 함수랑 이름이 같아 혼선이 생길 수 있다. 이럴 땐 불러올 때

```python
from django.contrib.auth import logout as auth_logout
```

으로 이름을 구분해준다.