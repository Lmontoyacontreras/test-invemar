from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

from geo.models import Lugares
from especies.models import Especies


# Create your models here.
@python_2_unicode_compatible
class Avistamientos(models.Model):
    avistamientoLATITUD = models.CharField('Latitud',max_length=250)
    avistamientoLONGITUD = models.CharField('Longitud',max_length=250)
    avistamientoOBSERVACIONES = models.CharField('Observaciones',max_length=250)
    avistamientoAUTOR = models.CharField('Nombre de Autor',max_length=250)
    especieID = models.ForeignKey(Especies, verbose_name='Especie')
    lugarID = models.ForeignKey(Lugares, verbose_name='Lugar')
    
    def __str__(self):
        return self.avistamientoOBSERVACIONES
        
    class Meta:
        verbose_name = 'Avistamiento'
        verbose_name_plural = 'Avistamientos'