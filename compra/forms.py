from django import forms

from compra.models import ComprasCabecera, Proveedor


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['descripcion', 'direccion', 'contacto', 'telefono', 'email', 'estado']
        labels = {'descripcion': 'Descripción:', 'direccion': 'Dirección:', 'contacto': 'Contacto:', 'telefono': 'Teléfono:', 'email': 'Email:', 'estado': 'Estado:'}
        widgets = {
            'descripcion': forms.TextInput,
            'email': forms.EmailInput,  # Usar EmailInput para el campo de correo electrónico
            'telefono': forms.NumberInput(attrs={'min': 0}),  # Usar NumberInput para campos numéricos
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        # Agregar la clase "checkbox-custom" al campo "estado"
        self.fields['estado'].widget.attrs['class'] = 'checkbox-custom'

        # Agregar una etiqueta personalizada para el nombre del input en el html
        self.fields['estado'].label = 'Estado:'  

class CompraCabeceraForm(forms.ModelForm):
    class Meta:
        model = ComprasCabecera
        fields = ['proveedor', 'fecha_compra', 'observacion', 'numero_factura', 'fecha_factura', 
                  'sub_total', 'descuento', 'total']
        
        labels = {'proveedor': 'Proveedor:', 
                  'fecha_compra': 'Fecha compra:', 
                  'observacion': 'Observación:', 
                  'numero_factura': 'Nro. factura:', 
                  'fecha_factura': 'Fecha factura:', 
                  'sub_total': 'Sub total:',
                  'descuento':'Descuento',
                  'total':'Total'}
        
        # widgets = {
        #     'observacion': forms.TextInput,
        #     'fecha_compra' : forms.DateTimeInput,
        #     'fecha_factura' : forms.DateTimeInput,
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['fecha_compra'].widget.attrs['readonly'] = True
        self.fields['fecha_factura'].widget.attrs['readonly'] = True
        self.fields['sub_total'].widget.attrs['readonly'] = True
        self.fields['descuento'].widget.attrs['readonly'] = True
        self.fields['total'].widget.attrs['readonly'] = True  
