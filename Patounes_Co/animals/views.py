from django.shortcuts import render
import requests

# Create your views here.

def index(request):

    url = "http://localhost:3001/adopte"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("Error: ", response.status_code)

    return render(request, 'animals/index.html', {'data': data})