from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band

def accueil(request):
    bands = Band.objects.all()
    return render(request, 'listings/accueil.html', {'bands': bands})

def adopte(request):
    return render(request, 'listings/adopte.html')
    
def actualite(request):
    return render(request, 'listings/actualite.html')
    
def aPropos(request):
    return render(request, 'listings/aPropos.html')