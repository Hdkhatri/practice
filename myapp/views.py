from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def myfunctionCall(request):
    return HttpResponse('Hello world')

def myfunctionabout(request):
    return HttpResponse('About Response')


def add(request,a,b):
    return HttpResponse(a+b)

def intro(request,name,age):
    dict= {
        'name' : name,
        "age" : age
    }
    return JsonResponse(dict)