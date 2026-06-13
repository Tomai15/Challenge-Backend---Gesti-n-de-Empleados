from django.contrib import admin

from .models import Empleado


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'apellido', 'nombre', 'email', 'puesto', 'salario', 'fecha_ingreso')
    list_filter = ('puesto',)
    search_fields = ('nombre', 'apellido', 'email', 'puesto')
    ordering = ('apellido', 'nombre')
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
