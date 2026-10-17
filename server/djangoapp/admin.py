from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.


# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 2

# CarModelAdmin class


class CarModelAdmin(admin.ModelAdmin):
    fields = ['name', 'car_make', 'type', 'year']

# CarMakeAdmin class with CarModelInline


class CarMakeAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    inlines = [CarModelInline]

# Register models here


admin.site.register(CarMake)
admin.site.register(CarModel)
