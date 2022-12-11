from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet)
router.register(r'tours', views.TourViewSet2)
router.register(r'locations', views.LocationViewSet)
router.register(r'countries', views.CountryViewSet)
router.register(r'customers-on-tours', views.CustomerOnTourViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('status/<slug:id>/',views.view_status,name='api_view_status'),
    path('test',views.view_conditional)
]
