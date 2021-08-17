from django import forms
from .models import *


class AddActorForm(forms.ModelForm):
    class Meta:
        model = Actors
        fields = '__all__'

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        last_name = last_name.title()
        return last_name

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        first_name = first_name.title()
        return first_name


class AddDirectorForm(forms.ModelForm):
    class Meta:
        model = Directors
        fields = '__all__'

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        last_name = last_name.title()
        return last_name

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        first_name = first_name.title()
        return first_name
