# inmuebles/forms.py
from django import forms
from .models import Inmueble


class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = [
            "nombre",
            "descripcion",
            "comuna",
            "direccion",
            "precio",
            "tipo",
            "foto",
        ]
