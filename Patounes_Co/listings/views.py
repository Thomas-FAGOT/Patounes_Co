from django.shortcuts import render

def accueil(request):
    return render(request, 'listings/accueil.html')

def adopte(request):
    return render(request, 'listings/adopte.html')
    
def actualite(request):
    return render(request, 'listings/actualite.html')
    
def aPropos(request):
    return render(request, 'listings/aPropos.html')

def inscription(request):
    return render(request, 'listings/inscription.html')

def connexion(request):
    return render(request, 'listings/connexion.html')