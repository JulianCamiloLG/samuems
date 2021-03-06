# Generated by Django 2.2.4 on 2019-08-15 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambulancia',
            fields=[
                ('numeroMovil', models.IntegerField(primary_key=True, serialize=False)),
                ('clase', models.CharField(choices=[('A', 'Avanzada'), ('B', 'Basica')], default='B', max_length=1)),
                ('responsable', models.CharField(default='', max_length=35)),
                ('cedulaR', models.IntegerField(default=0)),
                ('telefonoR', models.BigIntegerField(default=0)),
                ('marca', models.CharField(max_length=35)),
                ('modeloA', models.CharField(max_length=35)),
                ('placa', models.CharField(max_length=35)),
                ('servicio', models.CharField(choices=[('L', 'Libre'), ('O', 'Ocupado')], default='L', max_length=1)),
                ('fechaIngreso', models.DateField(auto_now_add=True)),
                ('foto', models.ImageField(upload_to='img/')),
                ('ubicacion', models.CharField(max_length=255)),
                ('latitud', models.DecimalField(decimal_places=10, default=0.0, max_digits=20)),
                ('longitud', models.DecimalField(decimal_places=10, default=0.0, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='ArchivoSnippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creadoEn', models.DateTimeField(auto_now_add=True)),
                ('nombreArchivo', models.CharField(max_length=100)),
                ('cedulaPaciente', models.IntegerField()),
                ('archivo', models.FileField(blank=True, upload_to='archivos/')),
            ],
        ),
        migrations.CreateModel(
            name='NivelHospital',
            fields=[
                ('nivel', models.IntegerField(primary_key=True, serialize=False)),
                ('tipoAtencion', models.CharField(max_length=255)),
                ('tipoServicio', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('nombre', models.CharField(max_length=35)),
                ('apellidoPaterno', models.CharField(max_length=35)),
                ('apellidoMaterno', models.CharField(max_length=35)),
                ('cedula', models.IntegerField(primary_key=True, serialize=False)),
                ('fechaNacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='M', max_length=1)),
                ('rhP', models.CharField(choices=[('O-', 'O Negativo'), ('O+', 'O Positivo'), ('A-', 'A Negativo'), ('A+', 'A Positivo'), ('B-', 'B Negativo'), ('B+', 'B Positivo'), ('AB-', 'AB Negativo'), ('AB+', 'AB Positivo')], default='', max_length=3)),
                ('apP', models.CharField(max_length=255)),
                ('apnP', models.CharField(max_length=255)),
                ('alergias', models.TextField(blank=True)),
                ('medicamentos', models.TextField(blank=True)),
                ('emailP', models.EmailField(max_length=254)),
                ('telefonoP', models.BigIntegerField()),
                ('direccionP', models.CharField(default='', max_length=255)),
                ('acudienteP', models.CharField(default='', max_length=255)),
                ('telefonoA', models.BigIntegerField(default=0)),
                ('correoA', models.EmailField(blank=True, max_length=254)),
                ('tnc', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=35)),
                ('direccion', models.CharField(max_length=35)),
                ('latitud', models.DecimalField(decimal_places=10, default=0.0, max_digits=20)),
                ('longitud', models.DecimalField(decimal_places=10, default=0.0, max_digits=20)),
                ('telefono', models.BigIntegerField()),
                ('especialidad', models.CharField(choices=[('T', 'Traumatología'), ('U', 'Urología'), ('O', 'Otorrinolaringología'), ('OF', 'Oftalmología'), ('GOT', 'Ginecología y obstetricia o tocología'), ('DQV', 'Dermatología médico-quirúrgica y venereología')], default='T', max_length=35)),
                ('numeroCamas', models.IntegerField()),
                ('nivel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsamuems.NivelHospital')),
            ],
        ),
    ]
