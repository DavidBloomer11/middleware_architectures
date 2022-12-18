from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .processor import Queue, order_processor
import datetime

from threading import Thread
# Create your views here.

def view_add_order(request):
    if request.method == 'POST':
        # Get parameters
        type = request.POST['type']
        name = request.POST['name']

        order = {
            'type':type,
            'name':name,
            'date_added':datetime.datetime.now()
        }

        q = Queue('order_queue.pkl')
        q.enqueue(order)
        q.save()



        return redirect('/orders/queue/')
    return render(request, 'add_order.html')

def view_order_queue(request):
    q = Queue('order_queue.pkl')
    items = q.items

    return render(request,'order_queue.html',context={'queue':items})

def view_booking_queue(request):
    q = Queue('booking_queue.pkl')
    items = q.items

    return render(request,'booking_queue.html',context={'queue':items})

def view_trip_queue(request):
    q = Queue('trip_queue.pkl')
    items = q.items

    return render(request,'trip_queue.html',context={'queue':items})

def get_booking(request):

    try:
        q = Queue('booking_queue.pkl')
        booking = q.dequeue()
        q.save()
        return JsonResponse(booking)
    except:
        return HttpResponse('no bookings in queue')

def get_trip(request):

    try:
        q = Queue('trip_queue.pkl')
        trip = q.dequeue()
        q.save()
        return JsonResponse(trip)
    except:
        return HttpResponse('no trips in queue')

def activate(request):
    try:
        new_thread = Thread(target=order_processor)
        new_thread.start()
        return HttpResponse('activated')
    except:
        return HttpResponse()