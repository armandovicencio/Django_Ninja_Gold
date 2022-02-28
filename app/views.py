import re
from django.shortcuts import render, redirect
from django.urls import reverse
from acceso.utils.decoradores import login_requerido
from app.models import Camion, Chofer, Ruta
from django.contrib import messages

# Create your views here.
@login_requerido
def index(request):

    if request.method == "GET":
        return render(request, 'app/index.html')

    if request.method == "POST":
        print(request.POST)
        # PROCESAR EN BASE DE DATOS
        return redirect("/")


def camion(request, id):

    if request.method == "GET":

        contexto = {
            'camion': Camion.objects.get(id=id)
        }

        return render(request, 'app/camion.html', contexto)

def camiones(request):

    if request.method == "GET":

        contexto = {
            'camiones': Camion.objects.all().order_by("-updated_at"),
            'tipos' : Camion.TIPO_CAMION
        }

        return render(request, 'app/camiones.html', contexto)

    if request.method == "POST":
        print(request.POST)

        nombre = request.POST['nombre']
        tipo = request.POST['tipo']

        Camion.objects.create(nombre=nombre, tipo=tipo)

        return redirect("/camiones")


def rutas(request):

    if request.method == "GET":

        contexto = {
            'rutas': Ruta.objects.all().order_by('-updated_at'),
        }

        return render(request, 'app/rutas.html', contexto)

def ruta_add(request):
    if request.method == "GET":

        contexto = {
            'camiones': Camion.objects.all().order_by("nombre")
        }

        return render(request, 'app/form_ruta.html', contexto)

    if request.method == "POST":
        print(request.POST)

        origen = request.POST['origen']
        destino = request.POST['destino']
        camion_id = request.POST['camion']
        
        camion = Camion.objects.get(id=camion_id)

        Ruta.objects.create(camion=camion, origen=origen, destino=destino)

        return redirect("/rutas")

def choferes(request):

    if request.method == "GET":
        print(request.GET)

        data =  Chofer.objects.all()

        if 'nombre' in request.GET:
            data = data.filter(nombre__contains=request.GET['nombre'])

        contexto = {
            'choferes': data.order_by("-updated_at"),
        }

        return render(request, 'app/choferes.html', contexto)

    if request.method == "POST":
        print(request.POST)

        nombre = request.POST['nombre']

        Chofer.objects.create(nombre=nombre)

        return redirect("/choferes")

def chofer(request, id):

    if request.method == "GET":
        chofer_instancia =  Chofer.objects.get(id=id)
        contexto = {
            'chofer': chofer_instancia,
            'camiones': Camion.objects.exclude(choferes=chofer_instancia).order_by("nombre")
        }

        return render(request, 'app/chofer.html', contexto)


def chofer_add_camion(request, id):

    print(request.POST)

    camion = Camion.objects.get(id=request.POST['camion'])
    chofer = Chofer.objects.get(id=id)

    chofer.camiones.add(camion)
    # camion.choferes.add(chofer)

    return redirect(f"/chofer/{id}")