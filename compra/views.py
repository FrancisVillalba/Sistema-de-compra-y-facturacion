from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from bases.views import SinPrivilegios
from compra.forms import ProveedorForm
from compra.models import Proveedor 
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

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
