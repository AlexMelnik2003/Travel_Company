from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', views.tour_list, name='tour_list'),
                  path('tour_detail/<int:pk>/', views.tour_detail, name='tour_detail'),
                  path('register/', views.register, name='register'),
                  path('login/', views.user_login, name='login'),
                  path('profile/', views.profile, name='profile'),
                  path('logout/', views.user_logout, name='logout'),
                  path('tour/<int:pk>/book/', views.book_tour, name='book_tour'),
                  path('make_payment/<int:pk>/', views.make_payment, name='make_payment'),
                  path('payment_success/', views.payment_success, name='payment_success'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
