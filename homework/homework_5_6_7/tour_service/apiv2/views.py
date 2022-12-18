from django.shortcuts import render
from django.http import HttpResponse

from api.models import Tour
from django.views.decorators.http import condition

from rest_framework.response import Response
from api.serializers import TourSerializer
from rest_framework.decorators import api_view
# Create your views here.

def strong_etag(request,id):
    tour = Tour.objects.get(pk=int(id))
    return tour.get_hash()


def weak_etag(request):
    etag = Tour.get_weak_etag() 

    return etag

def last_modified(request):
    tour_list = Tour.objects.get(pk=8)
    context = {'request':request}
    serializer = TourSerializer(tour_list, many=True,context=context)
    return Response(serializer.data)

@api_view(('GET',))
@condition(etag_func=strong_etag,last_modified_func=last_modified)
def get_tour(request,id):
    tour = Tour.objects.get(pk=int(id))

    if 'If-None-Match' in request.headers:
        if request.headers['If-None-Match'] == tour.get_hash():
            # insert what to do when nothing changed
            return HttpResponse(status=304)
        else:
        #insert what to do if new version
            context = {'request':request}
            serializer = TourSerializer(tour,context=context)
            return Response(serializer.data)
    
    # If no header is given, just return the object
    context = {'request':request}
    serializer = TourSerializer(tour,context=context)
    return Response(serializer.data)


@api_view(('GET',))
@condition(etag_func=weak_etag)
def get_tours(request):

    if 'If-None-Match' in request.headers:
        if request.headers['If-None-Match'] == Tour.get_weak_etag():
            # insert what to do when nothing changed
            return HttpResponse(status=304)
        else:
        #insert what to do if new version
            tour_list = Tour.objects.all()
            context = {'request':request}
            serializer = TourSerializer(tour_list, many=True,context=context)
            return Response(serializer.data)

    tour_list = Tour.objects.all()
    context = {'request':request}
    serializer = TourSerializer(tour_list, many=True,context=context)
    return Response(serializer.data)





