from django import forms

class SearchForm(forms.Form):
    search_term = forms.CharField(label='Parola da Tradurre', max_length=100)