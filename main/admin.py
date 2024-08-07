from django.contrib import admin
from .models import Destination, Tour, Book_list, Payment, Profile, TourImage, Faq


class TourImageInline(admin.TabularInline):
    model = TourImage
    extra = 1


class TourAdmin(admin.ModelAdmin):
    inlines = [TourImageInline]


admin.site.register(Destination)
admin.site.register(Tour)
admin.site.register(Book_list)
admin.site.register(Payment)
admin.site.register(Profile)
admin.site.register(TourImage)
admin.site.register(Faq)
