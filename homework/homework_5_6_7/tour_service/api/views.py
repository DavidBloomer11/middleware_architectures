from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

from asgiref.sync import sync_to_async
import asyncio


import time

from .models import Customer, Tour, Country, Location, CustomerOnTour

from rest_framework import viewsets
from rest_framework import views
from rest_framework import permissions, generics, status
from .serializers import CustomerSerializer, TourSerializer, LocationSerializer, CountrySerializer, CustomerOnTourSerializer

from .viewsets import HateoasModelViewSet
# Create your views here.

from .models import Tour

from django.views.decorators.http import condition

# Class based
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

    '''
    By overiding the function get_queryset() we are able to add filter against query parameters
    Example: /api/customers?first_name=David
    '''
    def get_queryset(self):
        queryset = Customer.objects.all()
        first_name = self.request.query_params.get('first_name')
        last_name = self.request.query_params.get('last_name')

        if first_name is not None:
            queryset = queryset.filter(first_name=first_name)

        if last_name is not None:
            queryset = queryset.filter(last_name=last_name)

        return queryset

class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [permissions.IsAuthenticated]

    '''
    We also want to be able to filter the tours by city and by country
    /api/tours?country=Belgium&City=Antwerp
    '''

    def get_queryset(self):
        queryset = Tour.objects.all()
        country = self.request.query_params.get('country')
        city = self.request.query_params.get('city')

        if city is not None:
            queryset = queryset.filter(location__city__in = [city])
        
        if country is not None:
            countryObj = Country.objects.filter(name = country)
            queryset = queryset.filter(location__country__in = countryObj)
        
        return queryset



    


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Location.objects.all()
        country = self.request.query_params.get('country')
        city = self.request.query_params.get('city')

        if city is not None:
            queryset = queryset.filter(city = city)
        
        if country is not None:
            countryObj = Country.objects.filter(name = country)
            queryset = queryset.filter(country__in=countryObj)
        
        return queryset

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]

class CustomerOnTourViewSet(viewsets.ModelViewSet):
    queryset = CustomerOnTour.objects.all()
    serializer_class = CustomerOnTourSerializer
    permission_classes = [permissions.IsAuthenticated]



class TourViewSet2(HateoasModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, pk=None, admin = False):
        admin = request.query_params.get('admin')
        try:
            tour = Tour.objects.get(pk=int(pk))
            if admin:
            # If admin request, the resource will be deleted
                tour = Tour.objects.get(pk=int(pk))
                tour.delete()
                return HttpResponse(status=200)
            else:
                response = f"http://127.0.0.1:8000/api/status/{pk}/"
                return HttpResponse(response,status=202)
        except:
            # Resource doesn't exists so return 404
            return HttpResponse(status=404)

    def get_retrieve_links(self, request, instance):
        qs = CustomerOnTour.objects.filter(tour=instance)
        customer_list = []
        for element in qs:
            x = {'href':f'http://127.0.0.1:8000/api/customers/{element.customer.customer_id}'}
            customer_list.append(x)

        return {
            'href': request.build_absolute_uri(request.path),
            'customers': customer_list,
        } 


def view_status(request,id):
    # Check if tour exists
    try:
        tour = Tour.objects.get(pk=int(id))
        return HttpResponse('pending')
    except:
        return HttpResponse('deleted')



def etag(request):
    '''This function takes the request and generates some sort of etag out of it
    example: hashing a object to an etag
    '''
    return 'xyz'

@condition(etag_func=etag)
def view_conditional(request):
    # Set Etag and Last-modifier response headers

    return HttpResponse('hello')


