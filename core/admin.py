from django.contrib import admin

from .models import Role, Employee, Service
# Register your models here.

@admin.register(Role)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('role', 'active', 'updated_at')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service', 'icon', 'active', 'updated_at')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'active', 'updated_at')