from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import username_validator, email_validator, letter_validator

class SignUpForm(UserCreationForm):
    username = forms.CharField(label="Username", max_length=30, required=True,validators=[username_validator,], error_messages={'required': "Це поле обов'язкове!"})
    first_name = forms.CharField(label="First Name", max_length=30, required=True,validators=[letter_validator,], error_messages={'required': "Це поле обов'язкове!"})
    last_name = forms.CharField(label="Last Name", max_length=30, required=True,validators=[letter_validator,], error_messages={'required': "Це поле обов'язкове!"})
    email = forms.EmailField(label="Email", max_length=320,required=True,validators=[email_validator,], error_messages={'required': "Це поле обов'язкове!"})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )