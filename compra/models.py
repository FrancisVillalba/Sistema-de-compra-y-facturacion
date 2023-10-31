from django.db import models
from bases.models import ClaseModelo
from inventario.models import Producto
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum

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
        return f'Cantidad: {self.cantidad}, Precio Proveedor: {self.precio_proveedor}, Subtotal: {self.sub_total}, Descuento: {self.descuento}, Total: {self.total}, Costo: {self.costo}, Producto: {self.producto}, Compra: {self.compra}'
    
    def save(self):
        self.sub_total = float(float(int(self.cantidad)) * float(self.precio_proveedor))
        self.total = self.sub_total - float(self.descuento)
        super(ComprasDetalle, self).save()

    class Meta:
        verbose_name_plural = 'Detalles compras'
        verbose_name = "Detalle compra"

@receiver(post_delete, sender=ComprasDetalle)
def detalle_compra_borrar(sender,instance, **kwargs):
    print(instance)
    id_producto = instance.producto.id
    id_compra = instance.compra.id

    cabecera = ComprasCabecera.objects.filter(pk=id_compra).first()
    if cabecera:
        sub_total = ComprasDetalle.objects.filter(compra=id_compra).aggregate(Sum('sub_total'))
        descuento = ComprasDetalle.objects.filter(compra=id_compra).aggregate(Sum('descuento'))
        cabecera.sub_total=sub_total['sub_total__sum']
        cabecera.descuento=descuento['descuento__sum']
        cabecera.save()
    
    prod=Producto.objects.filter(pk=id_producto).first()
    if prod:
        cantidad = int(prod.existencia) - int(instance.cantidad)
        prod.existencia = cantidad
        prod.save()

@receiver(post_save, sender=ComprasDetalle)
def detalle_compra_guardar(sender,instance,**kwargs):
    id_producto = instance.producto.id
    fecha_compra=instance.compra.fecha_compra

    prod=Producto.objects.filter(pk=id_producto).first()
    if prod:
        cantidad = int(prod.existencia) + int(instance.cantidad)
        prod.existencia = cantidad
        prod.ultima_compra=fecha_compra
        prod.save()



     
