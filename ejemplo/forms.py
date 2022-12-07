from django import forms
from ejemplo.models import Familiar

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=10)
    widget =forms.TextInput(attrs={'placeholder':'Busque algo...'}) # es un atributo del charfield

class Buscar(forms.Form):
  nombre = forms.CharField(max_length=100)

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']

