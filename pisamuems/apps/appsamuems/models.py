from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Paciente(models.Model):
    nombre = models.CharField(max_length=35)
    apellidoPaterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    cedula = models.IntegerField(primary_key=True)
    fechaNacimiento = models.DateField()
    Sexos = (('F', 'Femenino'), ('M', 'Masculino'))
    sexo = models.CharField(max_length=1, choices=Sexos, default='M')
    # Tipos de sangre para seleccionar uno
    tipoSangre = (('O-', 'O Negativo'),('O+', 'O Positivo'),('A-', 'A Negativo'),('A+', 'A Positivo'),
                  ('B-', 'B Negativo'),('B+', 'B Positivo'),('AB-', 'AB Negativo'),('AB+', 'AB Positivo'))
    rhP = models.CharField(max_length=3, choices=tipoSangre, default="")
    # Antecedentes personales patologicos
    apP = models.CharField(max_length=255)
    # Antecedentes personales patologicos
    apnP = models.CharField(max_length=255)
    # Alergias del paciente, campo no obligatorio
    alergias = models.TextField(blank=True)
    emailP = models.EmailField()
    telefonoP = models.BigIntegerField()
    direccionP = models.CharField(max_length=255, default="")
    # Datos sobre el acudiente del paciente
    acudienteP = models.CharField(max_length=255, default="")
    telefonoA = models.BigIntegerField(default=0)
    correoA = models.EmailField(blank=True)
    # Campo para aceptar terminos y condiciones
    tnc = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Ambulancia(models.Model):
    numeroMovil=models.IntegerField(primary_key=True)
    clases = (('A', 'Avanzada'), ('B', 'Basica'))
    clase=models.CharField(max_length=1, choices=clases, default='B')
    responsable = models.CharField(max_length=35, default="")
    cedulaR = models.IntegerField(default=0)
    telefonoR = models.BigIntegerField(default=0)
    marca=models.CharField(max_length=35)
    modeloA=models.CharField(max_length=35)
    placa=models.CharField(max_length=35)
    servicios = (('L', 'Libre'), ('O', 'Ocupado'))
    servicio = models.CharField(max_length=1, choices=servicios, default='L')
    fechaIngreso = models.DateField(auto_now_add=True)
    foto=models.ImageField(upload_to='img/')
    ubicacion=models.CharField(max_length=255)
    latitud = models.DecimalField(max_digits=10, decimal_places=10, blank=False, default=0.0)
    longitud = models.DecimalField(max_digits=10, decimal_places=10, blank=False, default=0.0)

    def __str__(self):
        return self.placa

class NivelHospital(models.Model):
    nivel=models.IntegerField(primary_key=True)
    tipoAtencion=models.CharField(max_length=255)
    tipoServicio=models.CharField(max_length=255)

class Hospital(models.Model):
    nombre=models.CharField(max_length=35)
    direccion=models.CharField(max_length=35)
    latitud=models.DecimalField(max_digits=10, decimal_places=10, blank=False, default=0.0)
    longitud=models.DecimalField(max_digits=10, decimal_places=10, blank=False, default=0.0)
    telefono=models.BigIntegerField()
    niveles=(('1','Nivel I'),('2','Nivel II'),('3','Nivel III'))
    #nivel = models.CharField(max_length=10, choices=niveles, default='1')
    nivel = models.ForeignKey(NivelHospital, choices=niveles, on_delete=models.CASCADE)
    especialidades = (('T', 'Traumatología'), ('U', 'Urología'), ('O', 'Otorrinolaringología'), ('OF', 'Oftalmología'), ('GOT', 'Ginecología y obstetricia o tocología'), ('DQV', 'Dermatología médico-quirúrgica y venereología'))
    especialidad = models.CharField(max_length=35, choices=especialidades, default='T')
    numeroCamas = models.IntegerField()

    def __str__(self):
        return self.nombre






