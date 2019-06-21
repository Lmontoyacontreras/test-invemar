from django.conf.urls import url

from .views import LugaresList, LugaresAdd, LugaresEdit

urlpatterns = [
    url(r'^$', LugaresList.as_view(), name='LugaresList'),
    url(r'^lugares/add/$', LugaresAdd.as_view(), name='LugaresAdd'),
    url(r'^lugares/edit/(?P<pk>[0-9]+)/$', LugaresEdit.as_view(), name='LugaresEdit'),
]