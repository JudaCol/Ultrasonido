from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_id = models.IntegerField(verbose_name='Cedula del Paciente', primary_key=True)
    first_lastname = models.CharField(max_length=20, verbose_name='Apellido Paterno')
    second_lastname = models.CharField(max_length=20, verbose_name='Apellido Materno')
    first_name = models.CharField(max_length=20, verbose_name='Primer Nombre')
    middle_name = models.CharField(max_length=30, verbose_name='Segundo Nombre')
    date_of_birth = models.DateField(max_length=30, null=True, blank=True, verbose_name='Fecha de Nacimiento')
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.first_lastname)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        db_table = 'paciente'
        ordering = ['patient_id']
