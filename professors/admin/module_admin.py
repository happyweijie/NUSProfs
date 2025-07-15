from django.contrib import admin
from ..models import Module

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('module_code', 'name')
    search_fields = ('module_code', 'name')
    ordering = ('module_code',)
