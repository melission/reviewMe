from django.forms import ModelForm
from .models import Review
from django import forms

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']



choices = (('BOOK', 'Search a book'), ('Movie', 'Search a movie'), ('Contributor', 'Search an author'),
           ('Director', 'Search a director'))

class SearchForm(forms.Form):
    search = forms.CharField(min_length=3)
    search_in = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
