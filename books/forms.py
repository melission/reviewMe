from django import forms
from .models import *


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'
        # exclude = ()

    # capitalise if not
    def clean_name(self):
        cap_name = self.cleaned_data['name']
        cap_name = cap_name.title()
        return cap_name


# class CoverForm(forms.ModelForm):
#     class Meta:
#         model = Cover
#         exclude = ()
