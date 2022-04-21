from django.urls import path
from . import views 

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'), # 회원 정보 수정
    path('change_password/', views.change_password, name='change_password'),
]