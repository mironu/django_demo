from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_view(request):
    "hello view"
    return HttpResponse(content="Hello,world!")