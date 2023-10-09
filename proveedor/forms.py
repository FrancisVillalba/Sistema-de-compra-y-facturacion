from django import forms

from proveedor.models import Proveedor


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