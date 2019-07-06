# Generated by Django 2.2.2 on 2019-07-04 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsamuems', '0003_auto_20190627_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=35)),
                ('direccion', models.CharField(max_length=35)),
                ('telefono', models.IntegerField()),
                ('nivel', models.CharField(choices=[('1', 'Nivel I'), ('2', 'Nivel II'), ('3', 'Nivel III')], default='1', max_length=10)),
                ('especialidad', models.CharField(choices=[('T', 'Traumatología'), ('U', 'Urología'), ('O', 'Otorrinolaringología'), ('OF', 'Oftalmología'), ('GOT', 'Ginecología y obstetricia o tocología'), ('DQV', 'Dermatología médico-quirúrgica y venereología')], default='T', max_length=35)),
                ('numeroCamas', models.IntegerField()),
            ],
        ),
    ]
