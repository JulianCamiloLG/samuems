from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import pacienteForm
from .forms import ambulanciaForm
from .forms import HospitalForm
# Crear vistas basadas en clases
from django.views.generic import CreateView,UpdateView,ListView,DeleteView

# Create your views here.

def home(request):
    return render(request,'index.html')

# Crear paciente
def crearPaciente(request):
    if request.method == 'POST':
        form = pacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = pacienteForm()
    return render(request,'aplicacion/crear_paciente.html',{'form':form})

# Listar Paciente
def listarPaciente(request):
    paciente = Paciente.objects.all()
    context = {'paciente': paciente}
    return render(request,'aplicacion/listar_paciente.html',context)

# Editar paciente
def editarPaciente(request, cedula):
    paciente = Paciente.objects.get(cedula = cedula)
    if request.method == 'GET':
        form = pacienteForm(instance = paciente)
    else:
        form = pacienteForm(request.POST, instance = paciente)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request,'aplicacion/crear_paciente.html',{'form':form})

# Eliminar paciente
def eliminarPaciente(request, cedula):
    paciente = Paciente.objects.get(cedula = cedula)
    if request.method == 'POST':
        paciente.delete()
        return redirect('index')
    return render(request,'aplicacion/eliminar_paciente.html',{'paciente':paciente})

# Forma de crear vistas basadas en clases
class createPaciente(CreateView):
    model = Paciente
    form_class = pacienteForm
    template_name = 'aplicacion/crear_paciente.html'
    success_url = reverse_lazy('index')

class listPaciente(ListView):
    model = Paciente
    template_name = 'aplicacion/listar_paciente.html'

class updatePaciente(UpdateView):
    model = Paciente
    form_class = pacienteForm
    template_name = 'aplicacion/crear_paciente.html'
    success_url = reverse_lazy('index')

class deletePaciente(DeleteView):
    model = Paciente
    template_name = 'aplicacion/eliminar_paciente.html'
    success_url = reverse_lazy('index')

# Crear ambulancia
def crearAmbulancia(request):
    if request.method == 'POST':
        form = ambulanciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ambulanciaForm()
    return render(request,'aplicacion/crear_ambulancia.html',{'form':form})

# Listar Ambulancia
def listarAmbulancia(request):
    ambulancia = Ambulancia.objects.all()
    context = {'ambulancia': ambulancia}
    return render(request,'aplicacion/listar_ambulancia.html',context)

# Editar ambulancia
def editarAmbulancia(request, movil):
    ambulancia = Ambulancia.objects.get(numeroMovil = movil)
    if request.method == 'GET':
        form = ambulanciaForm(instance = ambulancia)
    else:
        form = ambulanciaForm(request.POST, instance = ambulancia)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request,'aplicacion/crear_ambulancia.html',{'form':form})

# Eliminar ambulancia
def eliminarAmbulancia(request, movil):
    ambulancia = Ambulancia.objects.get( numeroMovil = movil)
    if request.method == 'POST':
        ambulancia.delete()
        return redirect('index')
    return render(request,'aplicacion/eliminar_ambulancia.html',{'ambulancia':ambulancia})

# Forma de crear vistas basadas en clases
class createAmbulancia(CreateView):
    model = Ambulancia
    form_class = ambulanciaForm
    template_name = 'aplicacion/crear_ambulancia.html'
    success_url = reverse_lazy('index')

class listAmbulancia(ListView):
    model = Ambulancia
    template_name = 'aplicacion/listar_ambulancia.html'

class updateAmbulancia(UpdateView):
    model = Ambulancia
    form_class = ambulanciaForm
    template_name = 'aplicacion/crear_ambulancia.html'
    success_url = reverse_lazy('index')

class deleteAmbulancia(DeleteView):
    model = Ambulancia
    template_name = 'aplicacion/eliminar_ambulancia.html'
    success_url = reverse_lazy('index')

# Crear Hospital
def crearHospital(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = HospitalForm()
    return render(request,'aplicacion/crear_hospital.html',{'form':form})

# Listar Hospital
def listarHospital(request):
    hospital = Hospital.objects.all()
    context = {'hospital': hospital}
    return render(request,'aplicacion/listar_hospital.html',context)

# Editar Hospital
def editarHospital(request, id):
    hospital = Hospital.objects.get(id1= id)
    if request.method == 'GET':
        form = HospitalForm(instance = hospital)
    else:
        form = HospitalForm(request.POST, instance = hospital)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request,'aplicacion/crear_hospital.html',{'form':form})

# Eliminar Hospital
def eliminarHospital(request, id):
    hospital = Hospital.objects.get( id1= id)
    if request.method == 'POST':
        hospital.delete()
        return redirect('index')
    return render(request,'aplicacion/eliminar_hospital.html',{'hospital':hospital})

# Forma de crear vistas basadas en clases
class createHospital(CreateView):
    model = Hospital
    form_class = HospitalForm
    template_name = 'aplicacion/crear_hospital.html'
    success_url = reverse_lazy('index')

class listHospital(ListView):
    model = Hospital
    template_name = 'aplicacion/listar_hospital.html'

class updateHospital(UpdateView):
    model = Hospital
    form_class = HospitalForm
    template_name = 'aplicacion/crear_hospital.html'
    success_url = reverse_lazy('index')

class deleteHospital(DeleteView):
    model = Hospital
    template_name = 'aplicacion/eliminar_hospital.html'
    success_url = reverse_lazy('index')

