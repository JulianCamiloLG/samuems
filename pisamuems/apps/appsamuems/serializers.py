from pip._vendor.cachecontrol import serialize
from rest_framework import serializers
from .models import ArchivoSnippet, EmergenciaSnippet


# Clase para serializar los datos del modelo para su transmision
class ArchivoSerializador(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    creadoEn = serializers.DateTimeField(required=False)
    nombreArchivo = serializers.CharField(required=False)
    cedulaPaciente = serializers.IntegerField()
    archivo = serializers.FileField(required=False)

    class Meta:
        model = ArchivoSnippet
        fields = '__all__'

    def update(self,instance,archivo):
        instance.nombreArchivo = archivo
        instance.save()
        return instance


# Clase para serializar el reporte de emergencias
class EmergenciaSerializador(serializers.ModelSerializer):
    class Meta:
        model = EmergenciaSnippet
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.comentarios = validated_data
        instance.save()
        return instance
