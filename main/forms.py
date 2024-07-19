from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField


from .models import Profile, Payment, Tour, Faq


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class RegistrationForm(UserCreationForm):
    # captcha = ReCaptchaField()
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Username'}
    ))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'First name'}
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Last name'}
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'placeholder': 'Password 1'}
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'placeholder': 'Password 2'}
    ))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', ]


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


class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ['questions']
        widgets = {
            'questions': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Напишите сюда вопрос или предложение'}),
        }
