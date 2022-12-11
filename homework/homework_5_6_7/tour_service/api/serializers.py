from rest_framework import serializers
from .models import Customer, Tour, Location, Country, CustomerOnTour

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['url','customer_id','first_name','last_name','identification_number']


class TourSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tour
        fields = ['url','name','location']


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ['url','name','street','city','country']


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ['url','name','code']


class CustomerOnTourSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomerOnTour
        fields = ['url','tour', 'customer', 'date_start','date_end']