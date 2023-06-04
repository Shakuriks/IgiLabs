
from django import forms

class FilmSearchForm(forms.Form):
    search_query = forms.CharField(label='Поиск')