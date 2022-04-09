# pjt06

## ModelForm

```python
from django import forms
from .models import Movie
GENRE_A = 'Comedy'
GENRE_B = 'Horror'
GENRE_C = 'Romance'
GENRE_CHOICE = [
    (GENRE_A, '코미디'),
    (GENRE_B, '공포'),
    (GENRE_C, '로맨스'),
]

class MovieForm(forms.ModelForm):
    release_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date'}
        )
    )
    genre = forms.CharField(
        widget = forms.Select(choices = GENRE_CHOICE,
            attrs = {
                
            }
        )
    )
    score = forms.FloatField(min_value = 0, max_value = 5,
        widget = forms.NumberInput(
            attrs = {
                'min': '0', 'max': '5', 'step' :'0.1',
            }
        )
    )
    class Meta:
        model = Movie
        fields = '__all__'
```

* form 의 각 요소의 속성을 설정할 수 있음
* arrts : html 태그의 요소를 딕셔너리 형태로 받음
* score의 경우 arrts 를 통해 html 단에서 점수 입력을 제한하고 min_value... 로 서버에서 valid 판단 가능
* [model 에 따른 form 의 필드](https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/#field-types)
  * 하나씩 눌러 내려가다보면 원하는게 나옴



## Image

```python
# settings.py
...
MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

# models.py
class Movie(models.Model):
    ...
    uploaded = models.ImageField(blank=True, upload_to='images/')

# django 에서 url 조회하는 법
<img class="w-100" src="{{ movie.uploaded.url }}" alt="{{ movie.title }}.img">
```

* 이미지 업로드 기능을 사용하기 위해 Pillow 설치가 필요함
* `root/upload_to/img.jpg` 로 저장됨