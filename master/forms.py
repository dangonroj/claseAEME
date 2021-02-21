from django import forms
from .models import *

class BuscarAlumForm(forms.Form):
   q = forms.CharField()