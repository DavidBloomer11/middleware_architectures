from django.contrib import admin
from .models import Country, Location, Customer, Tour

# Register your models here.
admin.site.register(Tour)
admin.site.register(Country)
admin.site.register(Location)
admin.site.register(Customer)