from django import forms
from . import models

class courseForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())  #for password field
    class Meta:
        model = models.course 
        fields ='__all__'
        labels = {
            'name': 'Full Name',
            'photo': 'Photo',
        }
        help_texts = {

            'email': 'Email Will be confidential',

        }

