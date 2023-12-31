from collections.abc import Mapping
from typing import Any
from django import forms 
from .models import Categoria, Marca, Producto, SubCategoria, UnidadMedida

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

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo','codigo_barra','descripcion', 'estado','precio','existencia', 'ultima_compra', 'marca', 'subcategoria', 'unidad_medida']
        exclude = ['usuario_modificacion','usuario_creacion','fecha_modificacion', 'fecha_creacion']
        labels = {'codigo': 'Código:', 'codigo_barra': 'Código de barra:', 'descripcion': 'Descripción:', 'precio': 'Precio:', 'existencia': 'Existencia:','ultima_compra':'Ultima compra:', 'marca':'Marca:', 'unidad_medida':'Unidad de medida:', 'subcategoria':'Subcategoria:'}
        widget = {'descripcion': forms.TextInput} 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in iter(self.fields):
        
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })



         # Se bloquea el campo ultima_compra, existencia
        self.fields['ultima_compra'].widget.attrs['readonly'] = True
        self.fields['existencia'].widget.attrs['readonly'] = True

         # Agregar la clase "checkbox-custom" al campo "estado"
        self.fields['estado'].widget.attrs['class'] = 'checkbox-custom'

        # Agregar una etiqueta personalizada para el nombre del input en el html
        self.fields['estado'].label = 'Estado:'  
        