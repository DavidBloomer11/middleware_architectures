from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views


urlpatterns = [
    path('tours/<slug:id>/',views.get_tour),
    path('tours/',views.get_tours)
]
