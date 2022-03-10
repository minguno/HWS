# 0302_workshop: Django project



## 개발환경 설정

- 가상환경 생성 및 활성화

  ```bash
  $ python -m venv venv
  ```

  ```bash
  $ source venv/Scripts/activate
  ```

- Django 설치

  ```bash
  $ pip install django==3.2.12
  ```

- `intro/` 프로젝트 디렉토리 생성

  ```bash
  $ django-admin startproject intro .
  ```

- 서버 확인

  ```bash
  $ python manage.py runserver
  ```

- `pages` 앱 생성

  ```bash
  $ python manage.py startapp pages
  ```

- `intro/settings.py`에 생성한 앱 등록 (출생신고)

  ```python
  INSTALLED_APPS = [
      # Custom apps (python manage.pu startapp으로 직접 생성한 앱)
      'pages',
      #Third-party packages (pip install 명령어로 설치한 패키지들)
      .. 아직 없음 ..
      # Django core packages
      .. 생략 ..
  ]



## 기능 개발

### 유저 스토리

1. 사용자가 `/dinner/저녁메뉴/인원수/ ` 주소로 접속한다
2. 사용자가 저녁메뉴와 저녁 먹을 사람 정보가 담긴 페이지를 본다

### 기능 정의

1. 사용자가 `/dinner/저녁메뉴/인원수/` 주소로 접속한다
   - 사용자가 접속할 수 있는 주소를 작성한다 (urls.py)
   
     ```python
     from pages import views
     ```
   
     `urlpatterns`에 입력
   
     ```python
     path('dinner/<str:menu>/<int:number>/', views.dinner)
     ```
   
   - 위 주소로 접속했을 때 실행할 함수를 작성한다 (views.py)
   
     ```python
     def dinner(request, menu, number):
         context = {
             'menu': menu,
             'numner': number,
         }
         return render(request, 'dinner.html', context)
     ```
   
   - 위 함수에서 저녁메뉴와 인원수 정보를 URL에서 가져온다 (views.py)
   
     ```html
     127.0.0.1:8000/dinner/chicken/6
     ```
   
   - 위 함수에서 저녁메뉴와 인원수 정보를 template(html)에 넘긴다 (views.py)
   
     `pages/` 앱 내에 `templates/` 디렉토리 생성
   
     `templates/` 내에 `dinner.html` 생성
   
     ```django
     <h1>저녁 메뉴</h1>
     <h2>저녁 먹을 사람?! {{ number }}명</h2>
     <h2>어떤 메뉴?! {{ menu }}</h2>
     ```
   
2. 사용자가 저녁메뉴와 저녁 먹을 사람 정보가 담긴 페이지를 본다

   - view 함수에서 전달한 저녁메뉴와 인원수 정보를 template에서 보여준다 (template of dinner.html)

     



