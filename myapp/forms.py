from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'marca', 'precio']
        widgets = {
            'precio': forms.NumberInput(attrs={'step': '1', 'min': '0'}),
        }
