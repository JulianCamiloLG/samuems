from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pickle
import sys
import os
from decimal import Decimal

from datetime import datetime

from .models import *
from .forms import *
from .serializers import *
# Crear vistas basadas en clases
from django.views.generic import CreateView,UpdateView,ListView,DeleteView


# Create your views here.
def home(request):
    return render(request, 'index.html')


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
    success_url = reverse_lazy('aplicacion:listar_paciente')


class listPaciente(ListView):
    model = Paciente
    template_name = 'aplicacion/listar_paciente.html'


class updatePaciente(UpdateView):
    model = Paciente
    form_class = pacienteForm
    template_name = 'aplicacion/crear_paciente.html'
    success_url = reverse_lazy('aplicacion:listar_paciente')


class deletePaciente(DeleteView):
    model = Paciente
    template_name = 'aplicacion/eliminar_paciente.html'
    success_url = reverse_lazy('aplicacion:listar_paciente')


# Crear ambulancia
def crearAmbulancia(request):
    if request.method == 'POST':
        form = ambulanciaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ambulanciaForm()
    return render(request, 'aplicacion/crear_ambulancia.html', {'form': form})


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
        ambulancia.foto.delete(save=True)
        ambulancia.delete()
        return redirect('index')
    return render(request,'aplicacion/eliminar_ambulancia.html',{'ambulancia':ambulancia})


# Forma de crear vistas basadas en clases
class createAmbulancia(CreateView):
    model = Ambulancia
    form_class = ambulanciaForm
    template_name = 'aplicacion/crear_ambulancia.html'
    success_url = reverse_lazy('aplicacion:listar_ambulancia')


class listAmbulancia(ListView):
    model = Ambulancia
    template_name = 'aplicacion/listar_ambulancia.html'


class updateAmbulancia(UpdateView):
    model = Ambulancia
    form_class = ambulanciaForm
    template_name = 'aplicacion/crear_ambulancia.html'
    success_url = reverse_lazy('aplicacion:listar_ambulancia')


class deleteAmbulancia(DeleteView):
    model = Ambulancia
    template_name = 'aplicacion/eliminar_ambulancia.html'
    success_url = reverse_lazy('aplicacion:listar_ambulancia')


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
    success_url = reverse_lazy('aplicacion:listar_hospital')


class listHospital(ListView):
    model = Hospital
    template_name = 'aplicacion/listar_hospital.html'


class updateHospital(UpdateView):
    model = Hospital
    form_class = HospitalForm
    template_name = 'aplicacion/crear_hospital.html'
    success_url = reverse_lazy('aplicacion:listar_hospital')


class deleteHospital(DeleteView):
    model = Hospital
    template_name = 'aplicacion/eliminar_hospital.html'
    success_url = reverse_lazy('aplicacion:listar_hospital')


# Vista para obtener todos los archivos
@api_view(['GET'])
def listar_archivos(request):
    if request.method == 'GET':
        archivos = ArchivoSnippet.objects.all()
        serializarArchivos = ArchivoSerializador(archivos,many=True)
        return Response(serializarArchivos.data)


def cambiarServicioAmbulancia(movilMasCercano):
    Ambulancia.objects.filter(pk=movilMasCercano).update(servicio='O')


def ambulanciaMasCercana(lat, lon):
    ambulancias = Ambulancia.objects.all()
    menor = sys.maxsize
    ambulanciaMasCercana = 0
    for ambulancia in ambulancias:
        distanciaLat = abs(ambulancia.latitud - Decimal(lat))
        distanciaLon = abs(ambulancia.longitud - Decimal(lon))
        menorLocal = distanciaLat + distanciaLon
        if menorLocal < menor and ambulancia.servicio is not 'O':
            menor = menorLocal
            ambulanciaMasCercana = ambulancia.numeroMovil
    return ambulanciaMasCercana


def hospitalMasCercano(lat, lon):
    hospitales = Hospital.objects.all()
    menor = sys.maxsize
    hospitalMasCercano = 0
    for hospital in hospitales:
        distanciaLat = abs(hospital.latitud - Decimal(lat))
        distanciaLon = abs(hospital.longitud - Decimal(lon))
        menorLocal = distanciaLat + distanciaLon
        if menorLocal < menor:
            menor = menorLocal
            hospitalMasCercano = hospital.id
    return hospitalMasCercano


def crearEmergencia(paciente, sintomas, lat, lon):
    fecha = datetime.now()
    stringFecha = fecha.strftime("%Y-%m-%d %H-%M-%S")
    idAmbulancia = ambulanciaMasCercana(lat, lon)
    idHospital = hospitalMasCercano(lat, lon)
    #with open('clf', 'rb') as clasificador:
     #   modelo = pickle.load(clasificador)
    #diagnostico = modelo.String(sintomas)
    datos = {
        "paciente": paciente,
        "ambulancia": idAmbulancia,
        "hospital": idHospital,
        "diagnostico": "prueba1",
        "lat": lat,
        "lon": lon,
        "sintomas": sintomas,
        "fechaReporte": stringFecha,
    }
    emergenciaSerializada = EmergenciaSerializador(data=datos)
    if emergenciaSerializada.is_valid():
        emergenciaSerializada.save()
        #cambiarServicioAmbulancia(idAmbulancia)
        return emergenciaSerializada
    else:
        for error in emergenciaSerializada.errors:
            print(error)

# Vista para crear un nuevo archivo
'''@api_view(['POST'])
def crear_emergencia(request):
    if request.method == 'POST':
        archivoSerializado = ArchivoSerializador(data=request.data)
        if archivoSerializado.is_valid():
            cedula = request.POST['cedulaPaciente']
            sintomas = request.POST['texto']
            lat = request.POST['lat']
            lon = request.POST['lon']
            archivoSerializado.save()
            emergencia = crearEmergencia(cedula, sintomas, lat, lon)
            nombreArchivo = crearArchivo(cedula, sintomas, lat, lon,
                                         emergencia.data['hospital'], emergencia.data['ambulancia'], emergencia.data['diagnostico'])
            archivo = ArchivoSnippet.objects.last()
            archivoSerializado.update(archivo, nombreArchivo)
            return Response(archivoSerializado.data, status=status.HTTP_201_CREATED)
    return Response(archivoSerializado.errors, status=status.HTTP_400_BAD_REQUEST)
'''
@api_view(['GET'])
def crear_emergencia(request):
    if request.method == 'GET':
        archivoSerializado = ArchivoSerializador(data=request.data)
        if archivoSerializado.is_valid():
            cedula = request.GET['cedulaPaciente']
            sintomas = request.GET['texto']
            lat = request.GET['lat']
            lon = request.GET['lon']
            archivoSerializado.save()
            emergencia = crearEmergencia(cedula, sintomas, lat, lon)
            nombreArchivo = crearArchivo(cedula, sintomas, lat, lon,
                                         emergencia.data['hospital'], emergencia.data['ambulancia'], emergencia.data['diagnostico'])
            archivo = ArchivoSnippet.objects.last()
            archivoSerializado.update(archivo, nombreArchivo)
            return Response(archivoSerializado.data, status=status.HTTP_201_CREATED)
    return Response(archivoSerializado.errors, status=status.HTTP_400_BAD_REQUEST)

# Método interno que crea el archivo
def crearArchivo(cedualPaciente, texto, lat, lon, hospital, ambulancia, diagnostico):
    path = 'media/archivos/'
    if not os.path.exists(path):
        os.makedirs(path)
    fecha = datetime.now()
    stringFecha = fecha.strftime("%d-%m-%Y_%H-%M-%S_")
    nombreArchivo = stringFecha + cedualPaciente
    archivoNuevo = open(os.path.join(path, nombreArchivo), "w+")
    archivoNuevo.write("Paciente: %s \n" % cedualPaciente)
    archivoNuevo.write("Sintomas: %s \n" % texto)
    archivoNuevo.write("Pedido desde: %s %s \n" % (str(lat), str(lon)))
    archivoNuevo.write("Asignado a la ambulancia: %s \n" % str(ambulancia))
    archivoNuevo.write("Asignado al hospital: %s \n" % str(hospital))
    archivoNuevo.write("Diagnosticado con: %s \n" % diagnostico)
    return nombreArchivo

# Vista para listar un unico archivo por id
@api_view(['GET'])
def listar_un_archivo(request, pk):
    if request.method == 'GET':
        try:
            archivo = ArchivoSnippet.objects.get(pk=pk)
        except ArchivoSnippet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializarArchivo = ArchivoSerializador(archivo)
        serializarArchivo.data['archivo'] = open('media/archivos/'+serializarArchivo.data['nombreArchivo'], "r")
        return Response(serializarArchivo.data)

# Vista para retornar la emergencia asignada
@api_view(['GET'])
def emergencia_ambulancia(request, numeroMovil):
    if request.method == 'GET':
        try:
            emergencia = EmergenciaSnippet.objects.get(ambulancia=numeroMovil)
        except EmergenciaSnippet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializarEmergencia = EmergenciaSerializador(emergencia.last)
        return Response(serializarEmergencia.data)

# Vista para retornar la emergencia asignada
@api_view(['GET'])
def emergencias(request):
    if request.method == 'GET':
        emergencia = EmergenciaSnippet.objects.all()
        serializarEmergencia = EmergenciaSerializador(emergencia, many=True)
        return Response(serializarEmergencia.data)

# Vista para terminar y actualizar el comentario de una emergencia
@api_view(['POST'])
def terminar_emergencia(request):
    if request.method == 'POST':
        try:
            emergencia = EmergenciaSnippet.objects.get(request.POST['id'])
        except EmergenciaSnippet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializarEmergencia = EmergenciaSerializador(emergencia)
        serializarEmergencia.update(emergencia, request.POST['comentario'])
        return Response(serializarEmergencia.data)