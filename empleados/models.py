from django.core.validators import MinValueValidator
from django.db import models


class Empleado(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    email = models.EmailField(
        unique=True,
        verbose_name='Email',
        help_text='Debe ser único en la empresa.',
    )
    puesto = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name='Puesto',
    )
    salario = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0, message='El salario no puede ser negativo.')],
        verbose_name='Salario',
        help_text='Monto en la moneda de la empresa. No puede ser negativo.',
    )
    fecha_ingreso = models.DateField(verbose_name='Fecha de ingreso')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return f'{self.apellido}, {self.nombre} ({self.puesto})'
