from django.core.management.base import BaseCommand

from empleados.models import Empleado


EMPLEADOS = [
    {'nombre': 'Laura',     'apellido': 'Martínez', 'email': 'laura.martinez@peopleflow.com',    'puesto': 'Backend Developer',  'salario': 95000,  'fecha_ingreso': '2022-03-14'},
    {'nombre': 'Matías',    'apellido': 'González', 'email': 'matias.gonzalez@peopleflow.com',   'puesto': 'Frontend Developer', 'salario': 88000,  'fecha_ingreso': '2021-07-01'},
    {'nombre': 'Sofía',     'apellido': 'Romero',   'email': 'sofia.romero@peopleflow.com',      'puesto': 'Product Manager',    'salario': 110000, 'fecha_ingreso': '2020-11-20'},
    {'nombre': 'Nicolás',   'apellido': 'López',    'email': 'nicolas.lopez@peopleflow.com',     'puesto': 'Backend Developer',  'salario': 92000,  'fecha_ingreso': '2023-01-10'},
    {'nombre': 'Valentina', 'apellido': 'García',   'email': 'valentina.garcia@peopleflow.com',  'puesto': 'UX Designer',        'salario': 80000,  'fecha_ingreso': '2022-08-15'},
    {'nombre': 'Tomás',     'apellido': 'Díaz',     'email': 'tomas.diaz@peopleflow.com',        'puesto': 'DevOps Engineer',    'salario': 105000, 'fecha_ingreso': '2021-04-03'},
    {'nombre': 'Camila',    'apellido': 'Pérez',    'email': 'camila.perez@peopleflow.com',      'puesto': 'QA Engineer',        'salario': 75000,  'fecha_ingreso': '2023-06-01'},
    {'nombre': 'Agustín',   'apellido': 'Torres',   'email': 'agustin.torres@peopleflow.com',    'puesto': 'Frontend Developer', 'salario': 85000,  'fecha_ingreso': '2022-12-01'},
    {'nombre': 'Florencia', 'apellido': 'Álvarez',  'email': 'florencia.alvarez@peopleflow.com', 'puesto': 'Backend Developer',  'salario': 98000,  'fecha_ingreso': '2021-09-15'},
    {'nombre': 'Santiago',  'apellido': 'Muñoz',    'email': 'santiago.munoz@peopleflow.com',    'puesto': 'Data Analyst',       'salario': 87000,  'fecha_ingreso': '2022-05-10'},
    {'nombre': 'Lucía',     'apellido': 'Herrera',  'email': 'lucia.herrera@peopleflow.com',     'puesto': 'Product Manager',    'salario': 115000, 'fecha_ingreso': '2020-02-28'},
    {'nombre': 'Martín',    'apellido': 'Castro',   'email': 'martin.castro@peopleflow.com',     'puesto': 'DevOps Engineer',    'salario': 102000, 'fecha_ingreso': '2023-03-01'},
    {'nombre': 'Julieta',   'apellido': 'Sánchez',  'email': 'julieta.sanchez@peopleflow.com',   'puesto': 'UX Designer',        'salario': 83000,  'fecha_ingreso': '2022-10-17'},
    {'nombre': 'Federico',  'apellido': 'Vega',     'email': 'federico.vega@peopleflow.com',     'puesto': 'QA Engineer',        'salario': 78000,  'fecha_ingreso': '2023-07-05'},
    {'nombre': 'Micaela',   'apellido': 'Ríos',     'email': 'micaela.rios@peopleflow.com',      'puesto': 'Frontend Developer', 'salario': 90000,  'fecha_ingreso': '2021-11-22'},
    {'nombre': 'Ignacio',   'apellido': 'Blanco',   'email': 'ignacio.blanco@peopleflow.com',    'puesto': 'Data Analyst',       'salario': 91000,  'fecha_ingreso': '2022-01-08'},
    {'nombre': 'Mora',      'apellido': 'Acosta',   'email': 'mora.acosta@peopleflow.com',       'puesto': 'Backend Developer',  'salario': 96000,  'fecha_ingreso': '2020-08-14'},
    {'nombre': 'Ezequiel',  'apellido': 'Vargas',   'email': 'ezequiel.vargas@peopleflow.com',   'puesto': 'DevOps Engineer',    'salario': 108000, 'fecha_ingreso': '2021-03-30'},
    {'nombre': 'Pilar',     'apellido': 'Medina',   'email': 'pilar.medina@peopleflow.com',      'puesto': 'QA Engineer',        'salario': 76000,  'fecha_ingreso': '2023-09-01'},
    {'nombre': 'Rodrigo',   'apellido': 'Ortiz',    'email': 'rodrigo.ortiz@peopleflow.com',     'puesto': 'Frontend Developer', 'salario': 86000,  'fecha_ingreso': '2022-06-20'},
]


class Command(BaseCommand):
    help = 'Carga empleados de prueba en la base de datos'

    def handle(self, *args, **kwargs):
        if Empleado.objects.exists():
            self.stdout.write('Ya existen empleados, se omite la siembra.')
            return

        for datos in EMPLEADOS:
            Empleado.objects.create(**datos)

        self.stdout.write(self.style.SUCCESS(f'{len(EMPLEADOS)} empleados creados.'))
