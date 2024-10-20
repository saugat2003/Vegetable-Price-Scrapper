# Create your views here.
from django.shortcuts import render
from .models import VegetablePrice

def price_list(request):
    prices = VegetablePrice.objects.all().order_by('-date')
    return render(request, 'scraper/price_list.html', {'prices': prices})
