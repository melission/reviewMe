from django import forms

choices = (('Book', 'Search a book'), ('Movie', 'Search a movie'), ('Contributor', 'Search an author'),
           ('Director', 'Search a director'))

class SearchForm(forms.Form):
    search_phrase = forms.CharField(min_length=3)
    search_in = forms.ChoiceField(choices=choices, widget=forms.RadioSelect, required=False)
