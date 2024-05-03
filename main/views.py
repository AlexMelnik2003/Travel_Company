from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import RegistrationForm, PaymentForm
from .models import Tour, Profile, Book_list, Payment
from django.contrib.auth.views import LogoutView
from django.contrib import messages


def tour_list(request):
    tours = Tour.objects.all()
    return render(request, 'main/tour_list.html', {'tours': tours})


@login_required
def tour_detail(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    is_booked = False
    if request.user.is_authenticated:
        is_booked = Book_list.objects.filter(user=request.user, tour=tour).exists()
    return render(request, 'main/tour_detail.html', {'tour': tour, 'is_booked': is_booked})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
    return render(request, 'registration/login.html')


@login_required
def profile(request):
    profile = request.user.profile
    booked_tours = Book_list.objects.filter(user=request.user)
    return render(request, 'profile/profile.html', {'profile': profile, 'booked_tours': booked_tours})


def user_logout(request):
    return render(request, 'main/tour_list.html')


@login_required
def book_tour(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    if request.method == 'POST':
        if not Book_list.objects.filter(user=request.user, tour=tour).exists():
            Book_list.objects.create(user=request.user, tour=tour)
    return redirect('/')


def make_payment(request, pk):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = Payment.objects.create(
                book_id=pk,
                card_number=form.cleaned_data['card_number'],
                expiration_date=form.cleaned_data['expiration_date'],
                cvv=form.cleaned_data['cvv']
            )
            return redirect('payment_success')
    else:
        form = PaymentForm()

    return render(request, 'pay/pay.html', {'form': form})


def payment_success(request):
    return render(request, 'pay/payment_success.html')
