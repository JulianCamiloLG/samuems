# formularios que se van a utilizar html
from django.urls import reverse_lazy
from django import forms
from .models import Paciente, Ambulancia, Hospital

# Formulario para los datos del paciente
class pacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = (
            'cedula',
            'apellidoPaterno',
            'apellidoMaterno',
            'nombre',
            'fechaNacimiento',
            'sexo',
            'apP',
            'apnP',
            'emailP',
            'telefonoP',
        )
        labels = {
            "cedula": ("Cédula de ciudadanía"),
            "apellidoPaterno": ("Apellido paterno"),
            "apellidoMaterno": ("Apellido materno"),
            "nombre": ("Nombre(s)"),
            "fechaNacimiento": ("Fecha de nacimiento"),
            "sexo": ("Sexo"),
            "apP": ("Antecedentes personales patológicos"),
            "apnP": ("Antecedentes personales no patológicos"),
            "emailP": ("Direccion e-mail"),
            "telefonoP": ("Teléfono"),
        }

# Formulario para los datos de la ambulancia:
class ambulanciaForm(forms.ModelForm):
    class Meta:
        model = Ambulancia
        fields=(
            'numeroMovil',
            'clase',
            'marca',
            'modeloA',
            'placa',
            'servicio',
            'foto',
            'ubicacion'
        )
        labels ={
            'numeroMovil':("Móvil"),
            'clase':("Clase"),
            'marca':("Marca"),
            'modeloA':("Modelo"),
            'placa':("Placa"),
            'servicio':("Servicio"),
            'foto':("Foto"),
            'ubicacion':("Última ubicación registrada")
        }

# Formulario para los datos del Hospital:
class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = {
            'nombre',
            'direccion',
            'telefono',
            'nivel',
            'especialidad',
            'numeroCamas'
        }
        labels = {
                'nombre':("Nombre"),
                'direccion':("Dirección"),
                'telefono':("Teléfono"),
                'nivel':("Nivel"),
                'especialidad':("Especialidad"),
                'numeroCamas':("Número de Camas")
        }