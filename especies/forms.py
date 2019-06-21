from django import forms

from .models import Especies

class EspeciesForm(forms.ModelForm):

    class Meta:
        model = Especies
        fields = ['especieNOMBRECOMUN','especieNOMBRECIENTIFICO','especieFamiliaID']
        widgets = {
            'especieNOMBRECOMUN':forms.TextInput(attrs = {
                'type':'text',
                'name':'especieNOMBRECOMUN',
                'class':'form-control',
                'placeholder':'Ingrese Nombre Comun',
                'required':True
            }),
            'especieNOMBRECIENTIFICO':forms.TextInput(attrs = {
                'type':'text',
                'name':'especieNOMBRECIENTIFICO',
                'class':'form-control',
                'placeholder':'Ingrese Nombre Cientifico',
                'required':True
            }),
            'especieFamiliaID':forms.Select(attrs={
                'class':'form-control',
                'required':True,
            })
        }