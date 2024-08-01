from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Favorite
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

orase = ["Timisoara", "Arad", "caca", "Bacau", "Craiova"]

class CityForm(forms.Form):
    oras=forms.CharField(label="", required=False, widget=forms.TextInput(attrs={
            'class': 'form-control rounded-pill custom-input form',
            'placeholder': 'Enter city name',
            'autofocus': 'autofocus'
        }))

def index(request):

    if request.method == "GET":
        form = CityForm(request.GET)
        if form.is_valid():
            oras = form.cleaned_data["oras"]
            if oras in orase:
                return redirect(reverse("wthrlyapp:localitate", args=[oras]))
            else:
                return render(request,"wthrlyapp/index.html", {"form": form, "favorites": Favorite.objects.all()})

    return render(request,"wthrlyapp/index.html", {"form": form, "favorites": Favorite.objects.all()} )

def localitate(request, oras):

    return render(request, "wthrlyapp/localitate.html", {"oras" : oras})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("wthrlyapp:index"))
        else:
            return render(request, "wthrlyapp/login.html", {
                "message": "Invalid Credentials"
            })

    return render(request, "wthrlyapp/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("wthrlyapp:index"))

#apikey:92a76a09a521f40e970e466cfbdf2432
