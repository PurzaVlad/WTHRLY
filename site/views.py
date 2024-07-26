
from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

orase = ["Timisoara", "Arad", "caca"]

# Create your views here.
def index(request):
    return render(request,"wthrlyapp/index.html")

def localitate(request, orase):
    if request.method == "GET":
        form=
    return render(request, "wthrlyapp/localitate.html", {
        "orase": orase
    })
