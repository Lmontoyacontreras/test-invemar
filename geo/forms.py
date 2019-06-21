from django import forms

from .models import Lugares

class LugarForm(forms.ModelForm):

    class Meta:
        model = Lugares
        fields = ['lugarTITULO','lugarALIAS','departamentoID']
        widgets = {
            'lugarTITULO':forms.TextInput(attrs = {
                'type':'text',
                'name':'lugarTITULO',
                'class':'form-control',
                'placeholder':'Ingrese Titulo',
                'required':True
            }),
            'lugarALIAS':forms.TextInput(attrs = {
                'type':'text',
                'name':'lugarALIAS',
                'class':'form-control',
                'placeholder':'Ingrese Alias',
                'required':True
            }),
            'departamentoID':forms.Select(attrs={
                'class':'form-control',
                'required':True,
            })
        }