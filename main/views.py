from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("The main page")
    return render(request, 'main/main.html')
    
