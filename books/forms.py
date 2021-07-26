from django import forms
from .models import *


class ReviewForm(forms.ModelForm):
    # email_on_save = forms.BooleanField(required=False, help_text="Send a notification if the review is published")

    class Meta:
        model = Review
        fields = ['content', 'rating']
        widgets = {'content': forms.Textarea(attrs={'placeholder': 'Write your review here'})}


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'
        # exclude = ()
