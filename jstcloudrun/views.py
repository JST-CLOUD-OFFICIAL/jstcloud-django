from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from .models import Counter

def hello_world(request):
    response_data = {
        "message": "Welcome to Jst ApoEngine, Hello World!"
    }
    return JsonResponse(response_data)

def get_counter_value(request):
    counter = Counter.objects.first()
    response_data = {
        'value': counter.count if counter else 0
    }
    return JsonResponse(response_data)


def increment_counter_value(request):
    counter = Counter.objects.first()
    if not counter:
        counter = Counter(count=1)
    else:
        counter.count += 1
    counter.save()
    response_data = {
        'value': counter.count
    }
    return JsonResponse(response_data)

def decrement_counter_value(request):
    counter = Counter.objects.first()
    if not counter:
        counter = Counter(count=-1)
    else:
        counter.count -= 1
    counter.save()
    response_data = {
        'value': counter.count
    }
    return JsonResponse(response_data)