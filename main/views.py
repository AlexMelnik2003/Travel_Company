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


def contact(request):
    return render(request, 'main/contact.html')


def about_us(request):
    return render(request, 'main/about_us.html')


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


# @login_required
# def book_tour(request, pk):
#     tour = get_object_or_404(Tour, pk=pk)
#     if request.method == 'POST':
#         if not Book_list.objects.filter(user=request.user, tour=tour).exists():
#             if tour.available_seats > 0:
#                 Book_list.objects.create(user=request.user, tour=tour)
#                 tour.available_seats -= 1
#                 tour.save()
#             else:
#                 messages.error(request, "Извините, все места на этот тур уже забронированы.")
#     return redirect('/')

@login_required
def book_tour(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    if request.method == 'POST':
        form = BookTourForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            book = Book_list.objects.create(user=request.user, tour=tour, start_date=start_date, end_date=end_date)
            tour.available_seats -= 1
            tour.save()
            return redirect('/')
    else:
        form = BookTourForm()
    return render(request, 'book_tour.html', {'form': form})

@login_required
def make_payment(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user

            book = Book_list.objects.filter(user=request.user, tour=tour).first()
            if not book:
                # Обработка случая, когда бронирование не найдено
                messages.error(request, "Для этого тура и пользователя бронирование не найдено.")
                return render(request, 'pay/pay.html', {'form': form, 'tour': tour})
            payment.book = book
            payment.amount = form.cleaned_data['amount']
            payment.save()
            return redirect('payment_success')
    else:
        form = PaymentForm()

    return render(request, 'pay/pay.html', {'tour': tour, 'form': form})


def payment_success(request):
    return render(request, 'pay/payment_success.html')