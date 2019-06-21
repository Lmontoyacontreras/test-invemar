from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

@python_2_unicode_compatible
class Paises(models.Model):
    paisCODIGO = models.CharField('Codigo',max_length=250)
    paisNOMBRE = models.CharField('Nombre',max_length=250)
    
    def __str__(self):
        return self.paisNOMBRE
        
    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
        
@python_2_unicode_compatible
class Departamentos(models.Model):
    departamentoCODIGO = models.CharField('Codigo',max_length=250)
    departamentoNOMBRE = models.CharField('Nombre',max_length=250)
    paisID = models.ForeignKey(Paises, verbose_name='Pais')
    
    def __str__(self):
        return self.departamentoNOMBRE
        
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        
@python_2_unicode_compatible
class Lugares(models.Model):
    lugarTITULO = models.CharField('Codigo',max_length=250)
    lugarALIAS = models.CharField('Nombre',max_length=250)
    departamentoID = models.ForeignKey(Departamentos, verbose_name='Departamento')
    
    def __str__(self):
        return self.lugarTITULO
        
    class Meta:
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'