#viewwthrly
from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.text import slugify

orase = ["Timisoara", "Arad", "caca"]

class CityForm(forms.Form):
    oras=forms.CharField(label="", required=False, widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter city name'
        }))

def index(request):
    if request.method == "GET":
        form = CityForm(request.GET)
        if form.is_valid():
            oras = form.cleaned_data["oras"]
            oras_slug = slugify(oras)
            if oras_slug in [slugify(city) for city in orase]:
                return redirect(reverse("wthrlyapp:localitate", args=[oras_slug]))
            else:
                return render(request,"wthrlyapp/index.html", {"form":form})


    else:
        form = CityForm()
    return render(request,"wthrlyapp/index.html", {"form":form})

def localitate(request, oras):
    return render(request, "wthrlyapp/localitate.html", {
                  "oras" : oras
                  })
