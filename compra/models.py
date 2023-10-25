from django.db import models

from bases.models import ClaseModelo
from inventario.models import Producto

# Create your models here.
class Proveedor(ClaseModelo):
    descripcion = models.CharField(max_length=100, null=True, help_text='Descripción del proveedor')
    direccion = models.CharField(max_length=250, null=True, blank=True)
    contacto = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=250, null=True) 

    def  __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Proveedor, self).save()

    class Meta:
        verbose_name_plural = 'Proveedores' 


class ComprasCabecera(ClaseModelo):
    fecha_compra = models.DateField(null=True, blank=True)
    observacion = models.TextField(blank=True, null=True)
    numero_factura = models.CharField(max_length=100)
    fecha_factura =models.DateField()
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)

    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return f'ID: {self.id}, Fecha de Compra: {self.fecha_compra}, Observación: {self.observacion}, Factura: {self.numero_factura}, Fecha de Factura: {self.fecha_factura}, Subtotal: {self.sub_total}, Descuento: {self.descuento}, Total: {self.total}, Proveedor: {self.proveedor}'
    
    def save(self):
        self.observacion = self.observacion.upper()
        if self.sub_total == None  or self.descuento == None:
            self.sub_total = 0
            self.descuento = 0
            
        self.total = self.sub_total - self.descuento
        # self.observacion = self.observacion.upper()
        # self.total = self.sub_total - self.descuento
        print("self:", self)
        super(ComprasCabecera,self).save()

    class Meta:
        verbose_name_plural = 'Encabezado compras'
        verbose_name = "Encabezado compra"


class ComprasDetalle(ClaseModelo): 
    cantidad = models.BigIntegerField(default=0)
    precio_proveedor = models.FloatField(default=0)
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)
    costo = models.FloatField(default=0)

    compra = models.ForeignKey(ComprasCabecera, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.producto)
    
    def save(self):
        self.sub_total = float(float(int(self.cantidad)) * float(self.precio_proveedor))
        self.total = self.sub_total - float(self.descuento)
        super(ComprasDetalle, self).save()

    class Meta:
        verbose_name_plural = 'Detalles compras'
        verbose_name = "Detalle compra"


     
