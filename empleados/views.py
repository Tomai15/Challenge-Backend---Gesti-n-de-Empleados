from django.db.models import Avg, Count
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .filters import EmpleadoFilter
from .models import Empleado
from .serializers import EmpleadoSerializer


class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    filterset_class = EmpleadoFilter

    @action(detail=False, methods=['get'], url_path='salario-promedio')
    def salario_promedio(self, request):
        resultado = self.get_queryset().aggregate(
            promedio=Avg('salario'),
            cantidad_empleados=Count('id'),
        )
        return Response({
            'promedio_salarial': resultado['promedio'],
            'cantidad_empleados': resultado['cantidad_empleados'],
        })
