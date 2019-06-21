from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from django.views.generic.edit import CreateView,UpdateView
from django.views.generic import ListView
from .models import Lugares
from .forms import LugarForm

# Create your views here.
class LugaresList(ListView):
    model = Lugares
    context_object_name = 'lugares'
    template_name = 'lugares/lugares_list.html'
    

class LugaresAdd(CreateView):
    model = Lugares
    template_name = 'lugares/lugares_form.html'
    form_class = LugarForm
    success_url = reverse_lazy('Lugares:LugaresList')
    

class LugaresEdit(UpdateView):
    model = Lugares
    template_name = 'lugares/lugares_form.html'
    form_class = LugarForm
    success_url = reverse_lazy('Lugares:LugaresList')