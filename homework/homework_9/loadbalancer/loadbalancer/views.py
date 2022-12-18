from django.shortcuts import render, redirect
from .health_checker import get_instance, run
from threading import Thread
from django.http import HttpResponse

# Create your views here.


def get_request(request):
    # We need to check which URL
    url = get_instance()

    return redirect(url)


def activate_loadbalancer(request):
    try:
        new_thread = Thread(target=run)
        new_thread.start()
        return HttpResponse('activated')
    except:
        return HttpResponse()