import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from empleados.models import Empleado


@pytest.mark.django_db
def test_email_unico(empleado):
    with pytest.raises(IntegrityError):
        Empleado.objects.create(
            nombre='Pedro',
            apellido='Martínez',
            email='juan@example.com',
            puesto='QA',
            salario=60000,
            fecha_ingreso='2024-01-01',
        )


@pytest.mark.django_db
def test_salario_no_negativo():
    empleado = Empleado(
        nombre='Carlos',
        apellido='Ruiz',
        email='carlos@example.com',
        puesto='DevOps',
        salario=-1000,
        fecha_ingreso='2024-01-01',
    )
    with pytest.raises(ValidationError):
        empleado.full_clean()
