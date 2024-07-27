from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse

orase = ["Timisoara", "Arad", "caca"]

class CityForm(forms.Form):
    oras=forms.CharField(label="", required=False, widget=forms.TextInput(attrs={
            'class': 'form-control rounded-pill',
            'placeholder': 'Enter city name'
        }))

def index(request):
    if request.method == "GET":
        form = CityForm(request.GET)
        if form.is_valid():
            oras = form.cleaned_data["oras"]
            if oras in orase:
                return redirect(reverse("wthrlyapp:localitate", args=[oras]))
            else:
                return render(request,"wthrlyapp/index.html", {"form":form})

    return render(request,"wthrlyapp/index.html", {"form":form})

def localitate(request, oras):
    return render(request, "wthrlyapp/localitate.html", {
                  "oras" : oras
                  })

#apikey:92a76a09a521f40e970e466cfbdf2432
