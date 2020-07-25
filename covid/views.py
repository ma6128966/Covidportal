from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse("HIdj")
    return render(request, 'covid/home.html')

# Create your views here.
