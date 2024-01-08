from django import forms
from django.core.validators import EmailValidator

class registrationForm(forms.Form):
    email = forms.CharField(label = 'Enter Email', validators = [EmailValidator()])
    