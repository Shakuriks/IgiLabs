from .models import Film, Hall, FilmCategory
from django import forms

class FilmSearchForm(forms.Form):
    search_query = forms.CharField(label='Поиск')
    

class FilmForm(forms.ModelForm):
    edit_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите название фильма'}))
    edit_category = forms.ModelChoiceField(queryset=FilmCategory.objects.all())
    class Meta:
        model = Film
        fields = ('name', 'category')
        
        
class SessionForm(forms.ModelForm):
    date = forms.CharField(widget=forms.DateInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите дату сеанса'}))
    time = forms.IntegerField(widget=forms.TimeInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите время'}))
    hall = forms.ModelChoiceField(queryset=Hall.objects.all())
    movie = forms.ModelChoiceField(queryset=Film.objects.all())
    price = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите цену'}))
    class Meta:
        model = Film
        fields = ('date', 'time', 'hall', 'movie', 'price')        