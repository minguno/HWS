from django.contrib.auth.forms import UserChangeForm, UserCreationForm
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


User = get_user_model() # == User 모델 (현재 프로젝트에서 활성화된 User 모델


class CustomUserChangeForm(UserChangeForm):
    password = None
    
    class Meta:
        model = User
        fields = ('username', 'email', 'last_name', 'first_name')


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')