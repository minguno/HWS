# 0303_workshop



## 1. intro/urls.py에 lotto/ 형태의 요청 경로를 명시

```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lotto/', views.lotto),
]
```

## 2. pages/views.py에 랜덤 로또 번호 6자리를 생성하고 html 파일을 렌더링 해주는 함수 작성

```python
from django.shortcuts import render
import random

# Create your views here.
def lotto(request):
    lotto = random.sample(range(1, 46), 6)
    context = {
        'lotto': lotto,
    }
    return render(request, 'lotto.html', context)
```

## 3. 서버의 응답 결과로 정해진 서식의 출력 결과를 보여주는 templates/lotto.html 문서 생성

```django
<h1>제 OOO회 로또 번호 추천</h1>
<p>SSAFY님께서 선택하신 로또 번호는 {{ lotto }}입니다.</p>
```

