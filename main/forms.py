from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField

from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class PaymentForm(forms.Form):
    card_number = forms.CharField(label='Номер карты', max_length=16)
    expiration_date = forms.CharField(label='Срок действия', max_length=4)
    cvv = forms.CharField(label='CVV', max_length=3)
