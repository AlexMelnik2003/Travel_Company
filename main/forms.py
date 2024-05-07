from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField

from .models import Profile, Payment


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class RegistrationForm(UserCreationForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['card_number', 'expiration_date', 'cvv', 'amount']
