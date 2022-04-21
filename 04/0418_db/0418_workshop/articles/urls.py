from django.urls import path 
from . import views 

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/like/', views.like, name='like'),
    # like 함수보다 아래에 있어야 좋아요가 반영된다
    path('<int:pk>/', views.detail, name='detail'),
]
