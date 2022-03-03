from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/pages/
    path('', views.index, name='index'),
    
    path('dinner/<str:menu>/<int:number>/', views.dinner),
]