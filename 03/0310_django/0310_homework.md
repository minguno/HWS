# 0310_homework



```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
```

## 1. 마이그레이션 작업

`posts` 앱 안의 `models.py`에 위와 같이 코드를 작성한 후, 마이그레이션 작업을 진행해줘야 `No such table` 에러가 뜨지 않는다

```bash
$ python manage.py makemigrations posts
```

처음 위 명령어를 실행하면 `posts/migrations/`에 `0001_initial.py` 파일이 생성된다

```bash
$ python manage.py migrate
```

DB에 table이 옮겨진다

### 추가로 알아두면 좋은 명령어

지정 마이그레이션의 SQL 내역

```bash
$ python manage.py sqlmigrate <app_name> <migration_name>
```

마이그레이션 적용 현황을 보여주는 명령어

```bash
$ python manage.py showmigrations <app_name>
```

## 2. New

```python
# 1 (O)
post = Post()
post.title = 'a'
post.content = 'b'
post.save()
# 2 (O)
post = Post(title='가', content='나')
post.save()
# 3 (X)
post = Post('제목', '내용')
post.save()
# 4 (O)
Post.objects.create(title='1', content='2')
```

1. Post 클래스의 인스턴스 변수를 생성한 후 각 필드값을 지정해주고 저장한다
2. 필드값을 지정한 인스턴스 변수를 생성한 후 저장한다
3. Post 클래스는 지정되있지 않은 인자값을 받지 않기 때문에 틀렸다
4. 필드값을 지정한 인스턴스 변수를 생성하고 저장 기능이 내포되어 있는 create() 메서드를 사용한다

## 3. 불러오기

10개의 Post가 저장되어 있고 id값이 1-10일 때 가장 첫 번째 Post를 불러오는 코드

```python
# 1 (O)
post1 = Post.objects.all()[0]
# 2 (X)
post2 = Post.objects.all()[-10]
# 3 (O)
post3 = Post.objects.all().first()
# 4 (O)
post4 = Post.objects.all().get(id=1)
```

1. QuerySet은 유사리스트이기 때문에 인덱싱이 가능하다
2. '유사' 리스트인 만큼 음수 인덱싱은 지원하지 않아 에러가 발생한다
3. 0번째 인덱스를 가져오는 것과 동일하다
4. id 값이 꼭 순서대로는 아니지만, increment 성질이 있기 때문에 1-10까지의 id 값을 갖고있다면 1이 첫 번째 Post이다

## 4. Edit

```python
my_post.title = '안녕하세요'
my_post.content = '반갑습니다'
my_post.save()
```

## 5. QuerySet 가져오기

```python
posts = Post.objects.all()
```

유사 리스트 QuerySet 형태로 반환된다
