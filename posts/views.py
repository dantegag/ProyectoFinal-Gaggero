from django.shortcuts import render, redirect
from .models import Pelicula, Director, Genero
from .forms import PeliculaForm, DirectorForm, GeneroForm, BusquedaForm

# Create your views here.

def inicio(request):
    form = BusquedaForm()
    peliculas = None

    if request.GET.get("titulo"):
        peliculas = Pelicula.objects.filter(titulo__icontains=request.GET["titulo"])

    return render(request, "posts/inicio.html", {"form": form, "peliculas": peliculas})

def peliculas(request):
    if request.method == "POST":
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("peliculas")
    else:
        form = PeliculaForm()

    lista = Pelicula.objects.all()
    return render(request, "posts/peliculas.html", {"form": form, "peliculas": lista})

def directores(request):
    if request.method == "POST":
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("directores")
    else:
        form = DirectorForm()

    lista = Director.objects.all()
    return render(request, "posts/directores.html", {"form": form, "directores": lista})

def generos(request):
    if request.method == "POST":
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("generos")
    else:
        form = GeneroForm()

    lista = Genero.objects.all()
    return render(request, "posts/generos.html", {"form": form, "generos": lista})
