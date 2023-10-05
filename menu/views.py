from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.

def index(request):
    '''pizzas = Pizza.objects.all()
    pizzas_names = [f"{pizza.name} : {pizza.price}$" for pizza in pizzas]
    pizzas_names_str = ", ".join(pizzas_names)
    return HttpResponse("Our pizzas : " + pizzas_names_str)'''

    pizzas = Pizza.objects.all().order_by('price')
    return render(request, 'menu/index.html', {'pizzas': pizzas})
