from django.http import HttpResponse
from django.shortcuts import render
from core.models import Animal

def home(request):
    context = { 'nome': 'Yuri', 'idade': 16 }
    return render(request, 'index.html', context=context)

def animais(request):
    animais = Animal.objects.all()
    print(animais)
    
    context = {'animais': animais}
    return render(request, 'animais.html', context)

