from django.shortcuts import render
from core.erp.models import *


# Create your views here.
def myfisrtsview(request):
    data = {
        'mueche': 'Esta monda si funciona',
        'patients': Patient.objects.all()
    }
    return render(request, 'index.html', data)


# Create your views here.
def mysecondview(request):
    data = {
        'mueche': 'Esta monda si funciona',
        'patients': Patient.objects.all()
    }
    return render(request, 'index2.html', data)
