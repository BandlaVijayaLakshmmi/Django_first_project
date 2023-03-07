from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def siri(request):
    return HttpResponse('<h1> siri and srujana best friends</h1>')
