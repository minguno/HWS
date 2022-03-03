# 0302_homework



## 1. MTV

|    MVC     |   MTV    |
| :--------: | :------: |
|   Model    |  Model   |
|    View    | Template |
| Controller |   View   |

MVC는 소프트웨어 공학에서 사용되는 design pattern 중 하나로 사용자 인터페이스로부터 프로그램 로직을 분리하여 애플리케이션의 시각적 요소나 이면에서 실행되는 부분을 서로 영향 없이 쉽게 고칠 수 있는 애플리케이션을 만들 수 있다.

이에 상응하는 MTV Pattern이 django에 존재한다.

- Model: 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리(추가, 수정, 삭제)
- Template: 파일의 구조나 레이아웃을 정의; 실제 내용을 보여주는 presentation에 사용
- View: HTTP 요청을 수신하고 HTTP 응답을 반환; Model을 통해 요청을 충족시키는데 필요한 데이터에 접근하고 template에게 응답의 서식 설정 (html) 을 맡긴다

## 2. URL

`Variable routing`은 django에서 URL 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것을 의미한다.

```python
# urls.py
path('lotto/<int:number>/', views.lotto, name='lotto')
```

```python
# views.py
def lotto(request, number):
    ..생략..
```

## 3. Django template path

Django 프로젝트는 render할 template 파일들을 찾을 때, 기본적으로 settings.py에 등록된 각 앱 폴더 안의 `templates` 폴더 내부를 탐색한다.