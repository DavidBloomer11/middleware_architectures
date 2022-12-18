from django.urls import path, include
from . import views

urlpatterns = [
    path("orders/add/",views.view_add_order),
    path("orders/queue/",views.view_order_queue),
    path('activate/',views.activate),
    path('bookings/queue/',views.view_booking_queue),
    path('bookings/dequeue/',views.get_booking),
    path('trips/queue/',views.view_trip_queue),
    path('trips/dequeue/',views.get_trip)
]
