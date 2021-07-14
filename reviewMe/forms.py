from django import forms
from django.core.exceptions import ValidationError
import re

choices = (('Book', 'Search a book'), ('Movie', 'Search a movie'), ('Contributor', 'Search an author'),
           ('Director', 'Search a director'))


class SearchForm(forms.Form):
    search_phrase = forms.CharField(min_length=3)
    search_in = forms.ChoiceField(choices=choices, widget=forms.RadioSelect, required=False)

    # clean search phrase from special symbols
    def clean_search_phrase(self):
        # print('cleaning')
        req = self.cleaned_data['search_phrase']
        clean_req = re.sub(r'[?|$|.|!|*|/|&|=|+]', r'', req)
        # print('before if', clean_req)
        if len(clean_req) != len(req):
            # print('!=')
            return clean_req
        #     raise ValidationError(f'No special symbols allowed')
        # print('==')
        return req
