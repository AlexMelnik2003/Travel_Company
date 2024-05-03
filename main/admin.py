from django.contrib import admin
from .models import Destination, Tour, Book_list, Payment, Profile

admin.site.register(Destination)
admin.site.register(Tour)
admin.site.register(Book_list)
admin.site.register(Payment)
admin.site.register(Profile)
