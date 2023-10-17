import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from bases.views import SinPrivilegios
from compra.forms import CompraCabeceraForm, ProveedorForm
from compra.models import ComprasCabecera, ComprasDetalle, Proveedor 
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

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
            detalle = ComprasDetalle.objects.filter(compras=cabecera)
            fecha_compra = datetime.date.isoformat(cabecera.fecha_compra)
            fecha_compra = datetime.date.isoformat(cabecera.fecha_factura)

            e = {
                'fecha_compra' : fecha_compra, 
                'proveedor': cabecera.proveedor,
                'observacion': cabecera.observacion,
                'numero_factura' : cabecera.numero_factura,
                'fecha_factura' : cabecera.fecha_factura,
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

        print(form_compra)
        return render(request, template_name, contexto)
