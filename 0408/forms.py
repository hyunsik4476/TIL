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