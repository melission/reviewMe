from django import forms
from .models import *
import attr


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']
        widgets = {'content': forms.Textarea(attrs={'placeholder': 'Write your review here'})}


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'
        # the same as fileds == '__all__
        # exclude = ()
