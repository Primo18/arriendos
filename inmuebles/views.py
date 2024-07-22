# inmuebles/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Inmueble
from .forms import InmuebleForm


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


def home(request):
    return render(request, "home.html")


def agregar_inmueble(request):
    if request.method == "POST":
        form = InmuebleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listar_inmuebles")
    else:
        form = InmuebleForm()
    return render(request, "agregar_inmueble.html", {"form": form})


def listar_inmuebles(request):
    inmuebles = Inmueble.objects.all()
    return render(request, "listar_inmuebles.html", {"inmuebles": inmuebles})


def editar_inmueble(request, pk):
    inmueble = get_object_or_404(Inmueble, pk=pk)
    if request.method == "POST":
        form = InmuebleForm(request.POST, request.FILES, instance=inmueble)
        if form.is_valid():
            form.save()
            return redirect("listar_inmuebles")
    else:
        form = InmuebleForm(instance=inmueble)
    return render(request, "editar_inmueble.html", {"form": form})


def eliminar_inmueble(request, pk):
    inmueble = get_object_or_404(Inmueble, pk=pk)
    if request.method == "POST":
        inmueble.delete()
        return redirect("listar_inmuebles")
    return render(request, "eliminar_inmueble.html", {"inmueble": inmueble})
