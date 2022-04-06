# 0406_homework

## 1. True or False

1. ModelForm을 사용할 때 Meta 클래스 내부에 model과 fields 변수는 반드시 작성해야 한다. **(F)**
   - `fields` 대신 `exclude`로 제외할 필드값을 설정 할 수도 있는데 둘을 동시에 사용하는 건 불가능하다
2. ModelForm을 사용할 때는 렌더링 되는 input element 속성은 Django에서 제공 해주는 대로만 사용해야 한다. **(T)**
3. 화면에 나타나는 각 element 위치는 html에서 form.as_p()를 사용하지 않아도 직접 위치시킬 수 있다. **(T)**

## 2. (a) ~ (d) 채우기

```python
# articles/forms.py
from django import forms
from .models import Article

class ArticleForm(forms.ModelsForm):
    class Meta:
        model = Article
        # 유효성 검사를 진행할 필드
        fields = '__all__'
```