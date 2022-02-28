
from django import forms
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from usuarios.models import Usuario
from app.models import Camion


class UsuarioForm(forms.ModelForm):

    confirmar_password = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput(attrs={'class':'form-control'}))

    

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if nombre == "PANCHO": 
            self.add_error('nombre', "El nombre es PANCHO")
        return nombre

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)

        if cleaned_data.get('password') != cleaned_data.get('confirmar_password'):
            raise forms.ValidationError(
                    "Las contraseñas no coinciden"
                )

    class Meta:
        model = Usuario
        fields  = ['nombre','apellido','username','email','password']

        labels = {
            'title':'title: ',
            'apellido':'Apellido: ',
            'username':'Nombre Usuario: ',
            'email':'Correo: ',
            'description': 'Descripción'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class UsuarioFormPlus(UsuarioForm):

    camion = forms.ModelChoiceField(queryset=Camion.objects.all(),widget=forms.Select(attrs={'class':'form-select'}))

    class Meta:
        model = Usuario
        fields  = ['nombre','apellido','username','description','email','password']

        labels = {
            'nombre':'Nombre: ',
            'apellido':'Apellido: ',
            'username':'Nombre Usuario: ',
            'email':'Correo: ',
            'password':'Contraseña: ',
            'description': 'Descripción'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
    

def add_usuarios_forms(request):

    if request.method == 'GET':
        return render(request, 'usuarios/formulario_form.html', {'formModel'  : UsuarioFormPlus()})
    
    if request.method == "POST":
        print(request.POST)

        form = UsuarioFormPlus(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado correctamente')
            return redirect(reverse('usuarios:listado'))
        else:
            messages.error(request, 'Con errores, solucionar.')
            return render(request, 'usuarios/formulario_form.html', {'formModel'  : form})    


def edit_usuarios_forms(request, id):
    
    if request.method == 'GET':
        usuario = Usuario.objects.get(id=id)
        form = UsuarioFormPlus(instance=usuario)

        return render(request, 'usuarios/formulario_form.html', {'formModel'  : form})

    if request.method == "POST":
        print(request.POST)
        usuario = Usuario.objects.get(id=id)
        form = UsuarioFormPlus(request.POST,instance=usuario)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario editado correctamente')
            return redirect(reverse('usuarios:listado'))
        else:
            messages.error(request, 'Con errores, solucionar.')
            return render(request, 'usuarios/formulario_form.html', {'formModel'  : form})    