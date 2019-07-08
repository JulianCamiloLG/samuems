# formularios que se van a utilizar html
from django.urls import reverse_lazy
from django import forms
from .models import Paciente, Ambulancia, Hospital

# Formulario para los datos del paciente
class pacienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(pacienteForm, self).__init__(*args, **kwargs)
        self.fields['tnc'].required = True

    class Meta:
        model = Paciente
        fields = (
            'nombre',
            'apellidoPaterno',
            'apellidoMaterno',
            'cedula',
            'fechaNacimiento',
            'sexo',
            'rhP',
            'apP',
            'apnP',
            'alergias',
            'emailP',
            'telefonoP',
            'direccionP',
            'acudienteP',
            'telefonoA',
            'correoA',
            'tnc',
        )
        labels = {
            "nombre": ("Nombre(s)"),
            "apellidoPaterno": ("Apellido paterno"),
            "apellidoMaterno": ("Apellido materno"),
            "cedula": ("Cédula de ciudadanía"),
            "fechaNacimiento": ("Fecha de nacimiento"),
            "sexo": ("Sexo"),
            "rhP": ("Grupo sanguineo (Rh)"),
            "apP": ("Antecedentes personales patológicos"),
            "apnP": ("Antecedentes personales no patológicos"),
            "Alergias": ("Antecedentes de alergias"),
            "emailP": ("Direccion e-mail"),
            "telefonoP": ("Teléfono"),
            "direccionP": ("Dirección de residencia"),
            "acudienteP": ("Nombre(s) y apellidos del acudiente del paciente"),
            "telefonoA": ("Teléfono del acudiente"),
            "correoA": ("Dirección e-mail del acudiente"),
            "tnc": ("Aceptar términos y condiciones"),
        }
        help_texts = {
            "nombre": ("Nombre(s) del paciente"),
            "apellidoPaterno": ("Apellido paterno del paciente"),
            "apellidoMaterno": ("Apellido materno del paciente"),
            "cedula": ("Cédula de ciudadanía del paciente"),
            "fechaNacimiento": ("Fecha de nacimiento del paciente"),
            "sexo": ("Sexo del paciente"),
            "rhP": ("Grupo sanguineo (Rh) del paciente"),
            "apP": ("Antecedentes personales patológicos del paciente"),
            "apnP": ("Antecedentes personales no patológicos del paciente"),
            "Alergias": ("Antecedentes de alergias sufridas por el paciente"),
            "emailP": ("Direccion e-mail del paciente"),
            "telefonoP": ("Teléfono del paciente"),
            "direccionP": ("Dirección de residencia del paciente"),
            "tnc": ("Aceptar términos y condiciones"),
        }
        widgets = {
            'fechaNacimiento': forms.DateInput(format=('%Y-%m-%d'),
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
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