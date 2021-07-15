from django import forms
from .models import *


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'
        # the same as fileds == '__all__
        # exclude = ()
