from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, "global/home.html", context={
        "name" : "marcos",
    })


def contato(request):
    return render(request, "me-apaga/temp.html")

def sobre(request):
    return HttpResponse("sobre")