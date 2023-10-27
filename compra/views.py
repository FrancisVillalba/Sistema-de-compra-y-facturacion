import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from bases.views import SinPrivilegios
from compra.forms import CompraCabeceraForm, ProveedorForm
from compra.models import ComprasCabecera, ComprasDetalle, Proveedor 
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Sum

from inventario.models import Producto



# Create your views here.
class ProveedorLista(SinPrivilegios,  LoginRequiredMixin, ListView):
 
    permission_required = 'compra.view_proveedor'
    
    login_url = 'bases/login-vw'

    model = Proveedor
    template_name = 'compra/proveedor_lista.html'
    context_object_name = 'obj'

class ProveedorNuevo(LoginRequiredMixin, CreateView):
    login_url='bases:login-vw' 

    model = Proveedor
    template_name = 'compra/proveedor_form.html'
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url = reverse_lazy('compra:proveedor_lista-vw')
    

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        # return super().form.valid(form)
        return super(ProveedorNuevo, self).form_valid(form)


class ProveedorEditar(LoginRequiredMixin, UpdateView):
    login_url='bases:login-vw'

    model = Proveedor
    template_name = 'compra/proveedor_form.html'
    context_object_name = 'obj' 
    form_class = ProveedorForm
    success_url = reverse_lazy('compra:proveedor_lista-vw')
    

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        # return super().form.valid(form)
        return super(ProveedorEditar, self).form_valid(form) 
    

def update_proveedor_estado(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
    proveedor.estado = 0  # Set estado to 0 (False)
    proveedor.save()
    
    success_url = reverse_lazy('compra:proveedor_lista-vw')  # Define success_url here

    return redirect(success_url)


class CompraLista(SinPrivilegios, LoginRequiredMixin, ListView):
 
    permission_required = 'compra.view_comprascabecera'
    
    login_url = 'bases/login-vw'

    model = ComprasCabecera
    template_name = 'compra/compras_lista.html'
    context_object_name = 'obj'

@login_required(login_url = '/login/')
@permission_required('compra.view_compracabecera', login_url = 'bases:sin_privilegios-vw')
def compras(request, compra_id = None): 
    template_name = 'compra/compras.html'
    producto = Producto.objects.filter(estado = True)
    form_compra = {}
    contexto = {}
 
    if request.method == 'GET': 
        form_compra = CompraCabeceraForm()

        cabecera = ComprasCabecera.objects.filter(pk=compra_id).first()

        if cabecera: 
            detalle = ComprasDetalle.objects.filter(compra=cabecera)
            fecha_compra = datetime.date.isoformat(cabecera.fecha_compra)
            fecha_factura = datetime.date.isoformat(cabecera.fecha_factura)

            e = {
                'fecha_compra' : fecha_compra, 
                'proveedor': cabecera.proveedor,
                'observacion': cabecera.observacion,
                'numero_factura' : cabecera.numero_factura,
                'fecha_factura' : fecha_factura,
                'sub_total' : cabecera.sub_total,
                'descuento' : cabecera.descuento,
                'total' : cabecera.total
            } 

            form_compra = CompraCabeceraForm(e) 
        else:
            detalle = None

        contexto = {'productos': producto,
                    'encabezado': cabecera,
                    'detalle': detalle,
                    'form_cabecera' : form_compra}


    # Para insertar o actualizar registros 
    if request.method == 'POST': 
        fecha_compra = request.POST.get("fecha_compra")
        observacion = request.POST.get("observacion")
        numero_factura = request.POST.get("numero_factura")
        fecha_factura = request.POST.get("fecha_factura")
        proveedor = request.POST.get("proveedor")
        sub_total = 0
        descuento = 0
        total = 0 


        # Verificamos si compraID esta cargado para hacer un insert o un update  
        if not compra_id:
            
            proveedor=Proveedor.objects.get(pk=proveedor)
 
            cabecera = ComprasCabecera(
                fecha_compra = fecha_compra,
                observacion = observacion,
                numero_factura = numero_factura,
                fecha_factura = fecha_factura,
                proveedor = proveedor,
                usuario_creacion = request.user 
            )  
 
            if cabecera:
                cabecera.save()
                compra_id=cabecera.id
        else:
            cabecera=ComprasCabecera.objects.filter(pk=compra_id).first()
            if cabecera:
                cabecera.fecha_compra = fecha_compra
                cabecera.observacion = observacion
                cabecera.numero_factura=numero_factura
                cabecera.fecha_factura=fecha_factura
                cabecera.usuario_modificacion=request.user.id
                cabecera.save()
                    
         
        print("compra_id:-----:",compra_id)
        if not compra_id:
            return redirect("compra:compras_lista-vw")
            

        producto = request.POST.get("id_id_producto")
        cantidad = request.POST.get("id_cantidad_detalle")
        precio = request.POST.get("id_precio_detalle")
        sub_total_detalle = request.POST.get("id_sub_total_detalle")
        descuento_detalle  = request.POST.get("id_descuento_detalle")
        total_detalle  = request.POST.get("id_total_detalle")

        productoObj = Producto.objects.get(pk=producto)
        
        print("producto:---:",productoObj)

        detalle = ComprasDetalle(
            compra=cabecera,
            producto=productoObj,
            cantidad=cantidad,
            precio_proveedor=precio,
            descuento=descuento_detalle,
            costo=0,
            usuario_creacion = request.user
        )

        print("DETALLE:---:",detalle)

        if detalle:
            detalle.save()

            sub_total=ComprasDetalle.objects.filter(compra=compra_id).aggregate(Sum('sub_total'))
            descuento=ComprasDetalle.objects.filter(compra=compra_id).aggregate(Sum('descuento'))
            cabecera.sub_total = sub_total["sub_total__sum"]
            cabecera.descuento=descuento["descuento__sum"]
            cabecera.save()

        return redirect("compra:compras_editar-vw",compra_id=compra_id)

    return render(request, template_name, contexto)

def compra_eliminar_detalle(request, detalle_id):
    detalle = get_object_or_404(ComprasDetalle, pk=detalle_id)
    detalleId = detalle.compra.id 
    print(detalle.compra)
    detalle.delete()  # Elimina el registro

    success_url = reverse_lazy('compra:compras_editar-vw', kwargs={'compra_id': detalleId})

    return redirect(success_url)