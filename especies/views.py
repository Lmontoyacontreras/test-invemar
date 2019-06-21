from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from django.views.generic.edit import CreateView,UpdateView
from django.views.generic import ListView

from .models import Especies
from .forms import EspeciesForm


class EspeciesList(ListView):
    model =  Especies
    context_object_name = 'especies'
    template_name = 'especies/especies_list.html'
    

class EspeciesAdd(CreateView):
    model =  Especies
    template_name = 'especies/especies_form.html'
    form_class = EspeciesForm
    success_url = reverse_lazy('Especies:EspeciesList')
    

class EspeciesEdit(UpdateView):
    model =  Especies
    template_name = 'especies/especies_form.html'
    form_class = EspeciesForm
    success_url = reverse_lazy('Especies:EspeciesList')