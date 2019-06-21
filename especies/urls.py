from django.conf.urls import url

from .views import EspeciesList, EspeciesAdd, EspeciesEdit

urlpatterns = [
    url(r'^especies/$', EspeciesList.as_view(), name='EspeciesList'),
    url(r'^especies/add/$', EspeciesAdd.as_view(), name='EspeciesAdd'),
    url(r'^especies/edit/(?P<pk>[0-9]+)/$', EspeciesEdit.as_view(), name='EspeciesEdit'),
]