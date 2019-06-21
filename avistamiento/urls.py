from django.conf.urls import url

from .views import AvistamientosList, AvistamientosAdd, AvistamientosEdit

urlpatterns = [
    url(r'^avistamientos/$', AvistamientosList.as_view(), name='AvistamientosList'),
    url(r'^avistamientos/add/$', AvistamientosAdd.as_view(), name='AvistamientosAdd'),
    url(r'^avistamientos/edit/(?P<pk>[0-9]+)/$', AvistamientosEdit.as_view(), name='AvistamientosEdit'),
]