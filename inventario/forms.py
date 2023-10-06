from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Categoria, Marca, SubCategoria, UnidadMedida

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        labels = {'descripcion': 'Descripción:', 'estado': 'Estado:'}
        widget = {'descripcion': forms.TextInput} 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in iter(self.fields):
        
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class SubCategoriaForm(forms.ModelForm):

    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True).order_by('descripcion')
    )
    class Meta:
        model = SubCategoria
        fields = ['categoria', 'descripcion', 'estado']
        labels = {'categoria': 'Categoria:', 'descripcion': 'Descripción', 'estado': 'Estado:'}
        widgets = {'descripcion': forms.TextInput(attrs={'placeholder': 'Ingrese la descripción'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        # Quitar la clase "form-control" del campo "estado"
        del self.fields['estado'].widget.attrs['class']

         # Agregar la clase "checkbox-custom" al campo "estado"
        self.fields['estado'].widget.attrs['class'] = 'checkbox-custom'

        # Agregar una etiqueta personalizada para el nombre del input en el html
        self.fields['estado'].label = 'Estado:'
        # self.fields['descripcion'].label = 'Descripción:'
        # self.fields['categoria'].label = 'Categorías:'


        self.fields['categoria'].empty_label = 'Seleccione categoría'

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['descripcion', 'estado']
        labels = {'descripcion': 'Descripción:', 'estado': 'Estado:'}
        widget = {'descripcion': forms.TextInput} 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in iter(self.fields):
        
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

         # Quitar la clase "form-control" del campo "estado"
        del self.fields['estado'].widget.attrs['class']

         # Agregar la clase "checkbox-custom" al campo "estado"
        self.fields['estado'].widget.attrs['class'] = 'checkbox-custom'

        # Agregar una etiqueta personalizada para el nombre del input en el html
        self.fields['estado'].label = 'Estado:' 


class UnidadMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields = ['descripcion', 'estado']
        labels = {'descripcion': 'Descripción:', 'estado': 'Estado:'}
        widget = {'descripcion': forms.TextInput} 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in iter(self.fields):
        
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

         # Quitar la clase "form-control" del campo "estado"
        del self.fields['estado'].widget.attrs['class']

         # Agregar la clase "checkbox-custom" al campo "estado"
        self.fields['estado'].widget.attrs['class'] = 'checkbox-custom'

        # Agregar una etiqueta personalizada para el nombre del input en el html
        self.fields['estado'].label = 'Estado:' 