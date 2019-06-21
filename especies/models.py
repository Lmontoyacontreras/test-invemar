from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.
@python_2_unicode_compatible
class EspeciesFamilias(models.Model):
    especieFamiliaTITULO = models.CharField('Especie Familia Titulo',max_length=250)

    def __str__(self):
        return self.especieFamiliaTITULO
        
    class Meta:
        verbose_name = 'Familia Especie'
        verbose_name_plural = 'Familia Especie'
        
@python_2_unicode_compatible
class Especies(models.Model):
    especieNOMBRECOMUN = models.CharField('Nombre',max_length=250)
    especieNOMBRECIENTIFICO = models.CharField('Nombre Cientifico',max_length=250)
    especieFamiliaID = models.ForeignKey(EspeciesFamilias, verbose_name='EspecieFamilia')
    
    def __str__(self):
        return self.especieNOMBRECOMUN
        
    class Meta:
        verbose_name = 'Especie'
        verbose_name_plural = 'Especies'