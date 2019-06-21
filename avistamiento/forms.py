from django import forms

from .models import Avistamientos

class AvistamientosForm(forms.ModelForm):

    class Meta:
        model = Avistamientos
        fields = ['avistamientoLATITUD','avistamientoLONGITUD','avistamientoOBSERVACIONES','avistamientoAUTOR','especieID','lugarID']
        widgets = {
            'avistamientoLATITUD':forms.TextInput(attrs = {
                'type':'text',
                'name':'especieNOMBRECOMUN',
                'class':'form-control',
                'placeholder':'Ingrese Nombre Comun',
                'required':True
            }),
            'avistamientoLONGITUD':forms.TextInput(attrs = {
                'type':'text',
                'name':'especieNOMBRECIENTIFICO',
                'class':'form-control',
                'placeholder':'Ingrese Nombre Cientifico',
                'required':True
            }),
            'avistamientoAUTOR':forms.TextInput(attrs = {
                'type':'text',
                'name':'especieNOMBRECIENTIFICO',
                'class':'form-control',
                'placeholder':'Ingrese Nombre Cientifico',
                'required':True
            }),
            'avistamientoOBSERVACIONES': forms.Textarea(attrs={
                'class':'form-control',
                'row':'3',
                'placeholder':'Observaciones',
            }),
            'lugarID':forms.Select(attrs={
                'class':'form-control',
                'required':True,
            }),
            'especieID':forms.Select(attrs={
                'class':'form-control',
                'required':True,
            })
        }