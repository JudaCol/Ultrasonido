# Generated by Django 4.1.3 on 2022-11-17 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_alter_patient_patient_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='id',
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Cedula del Paciente'),
        ),
    ]
