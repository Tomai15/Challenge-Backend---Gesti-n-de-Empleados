import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from empleados.models import Empleado


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def usuario(db):
    return User.objects.create_user(username='testuser', password='testpass123')


@pytest.fixture
def cliente_autenticado(usuario):
    client = APIClient()
    refresh = RefreshToken.for_user(usuario)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return client


@pytest.fixture
def empleado(db):
    return Empleado.objects.create(
        nombre='Juan',
        apellido='García',
        email='juan@example.com',
        puesto='Developer',
        salario=85000,
        fecha_ingreso='2023-01-15',
    )
