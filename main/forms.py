from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField

from .models import Profile, Payment, Tour


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email']


class PaymentForm(forms.ModelForm):
    card_number = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер карты'}))
    expiration_date = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Год'}))
    cvv = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'CVC'}))
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Сумма'}))

    class Meta:
        model = Payment
        fields = ['card_number', 'expiration_date', 'cvv', 'amount']


class BookTourForm(forms.ModelForm):
    data = forms.DateTimeField(
        widget=forms.DateTimeInput(format="%Y-%m-%d",
                                   attrs={"type": "data"}),
        input_formats=["%Y-%m-%d"])

    class Meta:
        model = Tour
        fields = ['data']
