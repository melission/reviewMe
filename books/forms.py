from django import forms
from .models import *
# from reviews.models import Review


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
    rating = forms.IntegerField(min_value=0, max_value=5)

    # capitalise if not
    def clean_name(self):
        cap_name = self.cleaned_data['name']
        cap_name = cap_name.title()
        return cap_name
