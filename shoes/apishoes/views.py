from django.shortcuts import render
from django.http import HttpResponse
from .models import chauss

def home(request):
    apishoes = chauss.objects.all()
    return render(request, 'hom.html', {'apishoes': apishoes})
