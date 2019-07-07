from django.db import models

# Create your models here.
class Paciente(models.Model):
    cedula = models.IntegerField(primary_key= True)
    apellidoPaterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    nombre = models.CharField(max_length=35)
    fechaNacimiento = models.DateField()
    Sexos = (('F', 'Femenino'), ('M', 'Masculino'))
    sexo = models.CharField(max_length=1, choices=Sexos, default='M')
    # Antecedentes personales patologicos
    apP = models.CharField(max_length=255)
    # Antecedentes personales patologicos
    apnP = models.CharField(max_length=255)
    emailP = models.EmailField()
    telefonoP = models.IntegerField()

    def __str__(self):
        return self.nombre

class Ambulancia(models.Model):
    numeroMovil=models.IntegerField(primary_key=True)
    clases = (('A', 'Avanzada'), ('B', 'Basica'))
    clase=models.CharField(max_length=1, choices=clases, default='B')
    marca=models.CharField(max_length=35)
    modeloA=models.CharField(max_length=35)
    placa=models.CharField(max_length=35)
    servicios = (('L', 'Libre'), ('O', 'Ocupado'))
    servicio = models.CharField(max_length=1, choices=servicios, default='L')
    fechaIngreso = models.DateField(auto_now_add=True)
    foto=models.ImageField(upload_to='img/')
    ubicacion=models.CharField(max_length=255)

    def __str__(self):
        return self.placa

class Hospital(models.Model):
    nombre=models.CharField(max_length=35)
    direccion=models.CharField(max_length=35)
    telefono=models.IntegerField()
    niveles=(('1','Nivel I'),('2','Nivel II'),('3','Nivel III'))
    nivel = models.CharField(max_length=10, choices=niveles, default='1')
    especialidades = (('T', 'Traumatología'), ('U', 'Urología'), ('O', 'Otorrinolaringología'), ('OF', 'Oftalmología'), ('GOT', 'Ginecología y obstetricia o tocología'), ('DQV', 'Dermatología médico-quirúrgica y venereología'))
    especialidad = models.CharField(max_length=35, choices=especialidades, default='T')
    numeroCamas = models.IntegerField()

    def __str__(self):
        return self.nombre
