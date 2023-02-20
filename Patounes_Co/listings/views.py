from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band

def accueil(request):
    bands = Band.objects.all()
    return render(request, 'listings/accueil.html', {'bands': bands})


def about(request):
    return HttpResponse('<h1>A propos</1> <p>Nous adorons Patounes & Co</p>')