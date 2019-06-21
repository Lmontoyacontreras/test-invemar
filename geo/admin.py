from django.contrib import admin

from .models import Departamentos, Lugares, Paises
# Register your models here.

@admin.register(Paises)
class AdminPaises(admin.ModelAdmin):
    list_display = ( 'id', 'paisCODIGO', 'paisNOMBRE' )
    search_fields = ('paisCODIGO','paisNOMBRE')
    
@admin.register(Departamentos)
class AdminDepartamentos(admin.ModelAdmin):
    list_display = ( 'id', 'departamentoCODIGO', 'departamentoNOMBRE' )
    search_fields = ('departamentoCODIGO','departamentoNOMBRE')
    
@admin.register(Lugares)
class AdminLugares(admin.ModelAdmin):
    list_display = ( 'id', 'lugarTITULO', 'lugarALIAS' )
    search_fields = ('lugarTITULO','lugarALIAS')