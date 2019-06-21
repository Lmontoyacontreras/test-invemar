from django.contrib import admin

from .models import Especies, EspeciesFamilias

# Register your models here.
@admin.register(EspeciesFamilias)
class AdminEspeciesFamilias(admin.ModelAdmin):
    list_display = ( 'id', 'especieFamiliaTITULO' )

@admin.register(Especies)
class AdminEspecies(admin.ModelAdmin):
    list_display = ( 'id', 'especieNOMBRECOMUN', 'especieNOMBRECIENTIFICO' )
    search_fields = ('especieNOMBRECOMUN','especieNOMBRECIENTIFICO')