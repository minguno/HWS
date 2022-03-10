# 0308_homework



## 1. Model 반영하기

*"Django가 Model에 생긴 변화를 DB에 반영하는 방법"*을 뜻하는 용어는 `migrate`이다.

## 2. Model 변경사항 저장하기

```python
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
```

### 1. 위 Model의 변경사항을 저장하기 위한 명령어

```bash
python manage.py makemigrations
```

`models.py`에 생긴 변경사항들의 스냅샷을 만드는 작업

마이그레이션 파일을 생성한다

### 2. 마이그레이션 파일에 대응되는 SQL문 확인 명령어

```bash
python manage.py sqlmigrate articles 0001_initial

===
python manage.py sqlmigrate 앱이름 마이그레이션_파일명
```

 파일 토대로 DB에 실제 반영한다

## 3. Python Shell

프로젝트 디렉토리 내 `settings.py`에 아래와 같이 추가해주고

```python
INSTALLED_APPS = [
    ..
    'django_extensions',
    ..
]
```

prompt에서

```bash
$ python manage.py shell_plus
```

를 입력하면 Shell이 실행된다

## 4. Django Model Field

- CharField
- TextField
- BooleanField
- FloatField
- ImageField
- TimeField

등 [공식 문서](https://docs.djangoproject.com/en/4.0/ref/models/fields/)에서 확인 가능하다