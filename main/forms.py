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
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'absolute p-1 bottom-8 ml-2 bg-white text-gray-400'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'absolute p-1 bottom-8 ml-2 bg-white text-gray-400'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'absolute p-1 bottom-8 ml-2 bg-white text-gray-400'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'absolute p-1 bottom-8 ml-2 bg-white text-gray-400'}))
    class Meta:
        model = User
        fields = ['username', 'email']


class PaymentForm(forms.ModelForm):
    card_number = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер карты'}))
    expiration_date = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Год'}))
    cvv = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'CVC'}))

    class Meta:
        model = Payment
        fields = ['card_number', 'expiration_date', 'cvv']


class BookTourForm(forms.ModelForm):
    data = forms.DateTimeField(
        widget=forms.DateTimeInput(format="%Y-%m-%d",
                                   attrs={"type": "data"}),
        input_formats=["%Y-%m-%d"])

    class Meta:
        model = Tour
        fields = ['data']
