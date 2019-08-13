from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Ambulancia)
admin.site.register(Hospital)
admin.site.register(NivelHospital)
admin.site.register(ArchivoSnippet)
admin.site.register(EmergenciaSnippet)
