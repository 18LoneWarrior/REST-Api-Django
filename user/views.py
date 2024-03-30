from django.shortcuts import render
import requests


# Create your views here.

def home(request):
    response = requests.get("http://http://127.0.0.1:8000/chaindata/")
    data = response.json()
    return render(request, 'home.html', {'data': data})
