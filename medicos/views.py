from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from medicos.forms import MedicoForm
from django.contrib import messages
from medicos.models import Medico

# Create your views here.

class MedicosView(View):
    def get(self, request):

        contexto = {
            'formModel': MedicoForm(),
            'medicos': Medico.objects.all(),
        }

        return render(request, 'medicos/index.html', contexto )

    def post(self, request):
        form = MedicoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado correctamente')
            return redirect(reverse('medicos:index'))
        else:
            messages.error(request, 'Con errores, solucionar.')
            return render(request, 'medicos/index.html', {'formModel'  : form})    

class MedicosDetail(View):
    def get(self, request, id):

        medico = Medico.objects.get(id=id)
        form = MedicoForm(instance=medico)

        contexto = {
            'formModel': form,
            'medicos': Medico.objects.all(),
        }

        return render(request, 'medicos/index.html', contexto)

    def post(self, request, id):
        medico = Medico.objects.get(id=id)
        form = MedicoForm(request.POST, instance=medico)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario editado correctamente')
            return redirect(reverse('medicos:index'))
        else:
            messages.error(request, 'Con errores, solucionar.')
            return render(request, 'medicos/index.html', {'formModel'  : form})    