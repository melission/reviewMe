from django import forms
from .models import *


class ReviewBookForm(forms.ModelForm):
    # email_on_save = forms.BooleanField(required=False, help_text="Send a notification if the review is published")

    class Meta:
        model = ReviewBook
        exclude = ['edited_at']
        # fields = ['content', 'rating']
        widgets = {'content': forms.Textarea(attrs={'placeholder': 'Write your review here'})}
    rating = forms.IntegerField(min_value=0, max_value=5)
