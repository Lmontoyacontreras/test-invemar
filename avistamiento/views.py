from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from django.views.generic.edit import CreateView,UpdateView
from django.views.generic import ListView

from .models import Avistamientos
from .forms import AvistamientosForm

# Create your views here.
class AvistamientosList(ListView):
    model =  Avistamientos
    context_object_name = 'avistamientos'
    template_name = 'avistamientos/avistamientos_list.html'
    

class AvistamientosAdd(CreateView):
    model =  Avistamientos
    template_name = 'avistamientos/avistamientos_form.html'
    form_class = AvistamientosForm
    success_url = reverse_lazy('Avistamientos:AvistamientosList')
    

class AvistamientosEdit(UpdateView):
    model =  Avistamientos
    template_name = 'avistamientos/avistamientos_form.html'
    form_class = AvistamientosForm
    success_url = reverse_lazy('Avistamientos:AvistamientosList')