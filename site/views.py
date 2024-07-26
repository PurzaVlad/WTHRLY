
from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

orase = ["Timisoara", "Arad", "caca"]

class NewTaskSearch(forms.Form):
    oras=forms.CharField(label="Search your city")

# Create your views here.
def index(request):
    return render(request,"wthrlyapp/index.html")

def localitate(request, oras):
    if request.method == "GET":
        form=NewTaskSearch(request.GET)
        if form.is_valid():
            oras = form.cleaned_data["oras"]
        return render(request, "wthrlyapp/localitate.html",{
            "oras": oras
        })
    else:
        form = NewTaskSearch()
        return render(request, "wthrlyapp/localitate.html", {"form": form})
