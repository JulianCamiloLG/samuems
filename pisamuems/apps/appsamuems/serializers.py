from rest_framework import serializers
from .models import ArchivoSnippet


# Clase para serializar los datos del modelo para su transmision
class ArchivoSerializador(serializers.ModelSerializer):
    class Meta:
        model = ArchivoSnippet
        fields = ['id', 'creadoEn', 'nombreArchivo', 'cedulaPaciente']