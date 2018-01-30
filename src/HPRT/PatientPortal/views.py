from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse("Returning from index")

# Create your views here.
