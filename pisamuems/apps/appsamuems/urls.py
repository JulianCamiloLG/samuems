from django.conf.urls import url
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'aplicacion'

urlpatterns = [
    path('',home, name = "index"),
    #path('crear_paciente/',crearPaciente, name = "crear_paciente"),
    #path('listar_paciente/', listarPaciente, name="listar_paciente"),
    #path('editar_paciente/<int:cedula>/', editarPaciente, name="editar_paciente"),
    #path('eliminar_paciente/<int:cedula>/', eliminarPaciente, name="eliminar_paciente"),
    # forma usando vistas basadas en clases
    path('crear_paciente/', createPaciente.as_view(), name="crear_paciente"),
    path('listar_paciente/', listPaciente.as_view(), name="listar_paciente"),
    path('editar_paciente/<int:pk>/', updatePaciente.as_view(), name="editar_paciente"),
    path('eliminar_paciente/<int:pk>/', deletePaciente.as_view(), name="eliminar_paciente"),

    #Ambulancias
    path('crear_ambulancia/', createAmbulancia.as_view(), name="crear_ambulancia"),
    path('listar_ambulancia/', listAmbulancia.as_view(), name="listar_ambulancia"),
    path('editar_ambulancia/<int:pk>/', updateAmbulancia.as_view(), name="editar_ambulancia"),
    path('eliminar_ambulancia/<int:pk>/', deleteAmbulancia.as_view(), name="eliminar_ambulancia"),

    # Hospitales
    path('crear_hospital/', createHospital.as_view(), name="crear_hospital"),
    path('listar_hospital/', listHospital.as_view(), name="listar_hospital"),
    path('editar_hospital/<int:pk>/', updateHospital.as_view(), name="editar_hospital"),
    path('eliminar_hospital/<int:pk>/', deleteHospital.as_view(), name="eliminar_hospital"),

    path('crear_audio/', createAudio.as_view(), name="crear_audio"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)