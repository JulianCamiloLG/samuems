# Generated by Django 2.2.2 on 2019-07-07 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appsamuems', '0006_auto_20190706_1858'),
    ]

    operations = [
        migrations.RunSQL(
            'DELETE FROM "public"."appsamuems_ambulancia";'
            'DELETE FROM "public"."appsamuems_hospital";'
            'DELETE FROM "public"."appsamuems_paciente";'
        ),
    ]
