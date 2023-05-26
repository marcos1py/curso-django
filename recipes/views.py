from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, "recipes/pages/home.html", context={
        "name" : "marcos",
    })


def contato(request):
    return render(request, "recipes/contatos.html")

def sobre(request):
    return HttpResponse("sobre")