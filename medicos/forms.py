from django import forms
from medicos.models import Medico


class MedicoForm(forms.ModelForm):

    def clean_especialidad(self):
        especialidad = self.cleaned_data['especialidad']
        
        existe = Medico.objects.filter(especialidad=especialidad).exists()

        if existe:
            raise forms.ValidationError("Especialidad ya existe")


    class Meta:
        model = Medico
        fields = ['nombre', 'apellido', 'especialidad', 'telefono', 'email']
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'especialidad': 'Especialidad',
            'telefono': 'Telefono',
            'email': 'Email',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidad': forms.Select(attrs={'class': 'form-select'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }