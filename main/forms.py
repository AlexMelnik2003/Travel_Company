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
    card_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер карты'}))
    expiration_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Месяц / Год'}))
    cvv = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'CVC'}))
    amount = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Сумма'}))

    class Meta:
        model = Payment
        fields = ['card_number', 'expiration_date', 'cvv', 'amount']
