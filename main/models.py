from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from django.contrib.auth.models import User


# пункт назначения
class Destination(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='destination/')

    def __str__(self):
        return self.name


# поездка
class Tour(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='tour_detail_imаge/')
    available_seats = models.IntegerField(default=50)
    book_data = models.DateField(auto_now_add=True)

# Книга для туров
class Book_list(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    book_data = models.DateField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.tour.destination.name}"


# Оплата
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.OneToOneField(Book_list, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    card_number = models.CharField(max_length=16, validators=[MinLengthValidator(16)])
    expiration_date = models.IntegerField(max_length=5,validators=[MinValueValidator(2024)])
    cvv = models.CharField(max_length=3)
    payment_date = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

