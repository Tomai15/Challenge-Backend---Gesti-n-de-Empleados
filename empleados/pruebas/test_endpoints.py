import pytest

from empleados.models import Empleado


@pytest.mark.django_db
def test_crear_empleado(cliente_autenticado):
    data = {
        'nombre': 'María',
        'apellido': 'Fernández',
        'email': 'maria@example.com',
        'puesto': 'Product Manager',
        'salario': '95000.00',
        'fecha_ingreso': '2024-06-01',
    }
    respuesta = cliente_autenticado.post('/api/empleados/', data, format='json')
    assert respuesta.status_code == 201


@pytest.mark.django_db
def test_listar_empleados(cliente_autenticado, empleado):
    respuesta = cliente_autenticado.get('/api/empleados/')
    assert respuesta.status_code == 200
    assert respuesta.data['count'] == 1


@pytest.mark.django_db
def test_filtrar_por_puesto(cliente_autenticado, empleado):
    respuesta = cliente_autenticado.get('/api/empleados/?puesto=Dev')
    assert respuesta.data['count'] == 1

    respuesta = cliente_autenticado.get('/api/empleados/?puesto=NoExiste')
    assert respuesta.data['count'] == 0


@pytest.mark.django_db
def test_obtener_empleado_por_id(cliente_autenticado, empleado):
    respuesta = cliente_autenticado.get(f'/api/empleados/{empleado.id}/')
    assert respuesta.status_code == 200
    assert respuesta.data['id'] == empleado.id


@pytest.mark.django_db
def test_actualizar_empleado(cliente_autenticado, empleado):
    respuesta = cliente_autenticado.patch(
        f'/api/empleados/{empleado.id}/',
        {'salario': '90000.00'},
        format='json',
    )
    assert respuesta.status_code == 200
    assert respuesta.data['salario'] == '90000.00'


@pytest.mark.django_db
def test_eliminar_empleado(cliente_autenticado, empleado):
    respuesta = cliente_autenticado.delete(f'/api/empleados/{empleado.id}/')
    assert respuesta.status_code == 204


@pytest.mark.django_db
def test_salario_promedio(cliente_autenticado):
    Empleado.objects.create(
        nombre='Ana', apellido='López', email='ana@example.com',
        puesto='Dev', salario=80000, fecha_ingreso='2024-01-01',
    )
    Empleado.objects.create(
        nombre='Luis', apellido='Pérez', email='luis@example.com',
        puesto='Dev', salario=100000, fecha_ingreso='2024-01-01',
    )
    respuesta = cliente_autenticado.get('/api/empleados/salario-promedio/')
    assert respuesta.status_code == 200
    assert float(respuesta.data['promedio_salarial']) == 90000.0


@pytest.mark.django_db
def test_sin_token_retorna_401(api_client):
    respuesta = api_client.get('/api/empleados/')
    assert respuesta.status_code == 401
