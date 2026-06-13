import django_filters

from .models import Empleado


class EmpleadoFilter(django_filters.FilterSet):
    puesto = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Empleado
        fields = ['puesto']
