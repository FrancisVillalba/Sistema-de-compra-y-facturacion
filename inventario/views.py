from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView

from bases.views import SinPrivilegios
from .models import Categoria, Marca, Producto, SubCategoria, UnidadMedida
from .forms import CategoriaForm, MarcaForm, ProductoForm, SubCategoriaForm, UnidadMedidaForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

class CategoriaView(SinPrivilegios, LoginRequiredMixin, ListView):

    permission_required = 'inventario.view_categoria'

    login_url = 'bases/login-vw'

    model = Categoria
    template_name = 'inventario/categoria_lista.html'
    context_object_name = 'obj'
    

class CategoriaNuevo(SuccessMessageMixin,LoginRequiredMixin, CreateView):
    login_url='bases:login-vw'

    model = Categoria
    template_name = 'inventario/categoria_form.html'
    context_object_name = 'obj' 
    form_class = CategoriaForm
    success_message = 'Creado con exito!'
    success_url = reverse_lazy('inventario:categoria_lista-vw') 

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        # return super().form.valid(form)
        return super(CategoriaNuevo, self).form_valid(form)
    
class CategoriaEditar( SuccessMessageMixin,LoginRequiredMixin, UpdateView):
    login_url='bases:login-vw'

    model = Categoria
    template_name = 'inventario/categoria_form.html'
    context_object_name = 'obj' 
    form_class = CategoriaForm
    success_url = reverse_lazy('inventario:categoria_lista-vw')
    success_message = 'Modificado con exito!'

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        # return super().form.valid(form)
        return super(CategoriaEditar, self).form_valid(form) 
    

def update_categoria_estado(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    categoria.estado = 0  # Set estado to 0 (False)
    categoria.save()
    
    success_url = reverse_lazy('inventario:categoria_lista-vw')  # Define success_url here

    return redirect(success_url)

class SubCategoriaView(SinPrivilegios, LoginRequiredMixin, ListView):

    permission_required = 'inventario.view_subcategoria'

    login_url = 'bases/login-vw'

    model = SubCategoria
    template_name = 'inventario/subcategoria_lista.html'
    context_object_name = 'obj'

class SubCategoriaNuevo(LoginRequiredMixin, CreateView):
    login_url='bases:login-vw'

    model = SubCategoria
    template_name = 'inventario/subcategoria_form.html'
    context_object_name = 'obj' 
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inventario:subcategoria_lista-vw')
    

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        # return super().form.valid(form)
        return super(SubCategoriaNuevo, self).form_valid(form)
    
class SubCategoriaEditar(LoginRequiredMixin, UpdateView):
    login_url='bases:login-vw'

    model = SubCategoria
    template_name = 'inventario/subcategoria_form.html'
    context_object_name = 'obj' 
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inventario:subcategoria_lista-vw')
    

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        # return super().form.valid(form)
        return super(SubCategoriaEditar, self).form_valid(form) 
    
def update_supcategoria_estado(request, categoria_id):
    subcategoria = get_object_or_404(SubCategoria, pk=categoria_id)
    subcategoria.estado = 0  # Set estado to 0 (False)
    subcategoria.save()
    
    success_url = reverse_lazy('inventario:subcategoria_lista-vw')  # Define success_url here

    return redirect(success_url)

class MarcaLista(SinPrivilegios, LoginRequiredMixin, ListView):
    permission_required = 'inventario.view_marca'
    
    login_url = 'bases/login-vw'

    model = Marca
    template_name = 'inventario/marca_lista.html'
    context_object_name = 'obj'

class MarcaNuevo(LoginRequiredMixin, CreateView):
    login_url='bases:login-vw'

    model = Marca
    template_name = 'inventario/marca_form.html'
    context_object_name = 'obj' 
    form_class = MarcaForm
    success_url = reverse_lazy('inventario:marca_lista-vw')
    

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        # return super().form.valid(form)
        return super(MarcaNuevo, self).form_valid(form)
    
class MarcaEditar(LoginRequiredMixin, UpdateView):
    login_url='bases:login-vw'

    model = Marca
    template_name = 'inventario/marca_form.html'
    context_object_name = 'obj' 
    form_class = MarcaForm
    success_url = reverse_lazy('inventario:marca_lista-vw')
    

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        # return super().form.valid(form)
        return super(MarcaEditar, self).form_valid(form) 
    
def update_marca_estado(request, marca_id):
    marca = get_object_or_404(Marca, pk=marca_id)
    marca.estado = 0  # Set estado to 0 (False)
    marca.save() 

    success_url = reverse_lazy('inventario:marca_lista-vw')  # Define success_url here

    return redirect(success_url)


class UnidadMedidaLista(SinPrivilegios, LoginRequiredMixin, ListView):
    permission_required = 'inventario.view_unidad_medida'

    login_url = 'bases/login-vw'

    model = UnidadMedida
    template_name = 'inventario/unidad_medida_lista.html'
    context_object_name = 'obj'

class UnidadMedidaNuevo(LoginRequiredMixin, CreateView):
    login_url='bases:login-vw'

    model = UnidadMedida
    template_name = 'inventario/unidad_medida_form.html'
    context_object_name = 'obj' 
    form_class = UnidadMedidaForm
    success_url = reverse_lazy('inventario:unidad_medida_lista-vw')
    

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        # return super().form.valid(form)
        return super(UnidadMedidaNuevo, self).form_valid(form)
    
class UnidadMedidaEditar(LoginRequiredMixin, UpdateView):
    login_url='bases:login-vw'

    model = UnidadMedida
    template_name = 'inventario/unidad_medida_form.html'
    context_object_name = 'obj' 
    form_class = UnidadMedidaForm
    success_url = reverse_lazy('inventario:unidad_medida_lista-vw')
    

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        # return super().form.valid(form)
        return super(UnidadMedidaEditar, self).form_valid(form) 
    
def update_unidad_medida_estado(request, unidad_medida_id):
    unidad_medida = get_object_or_404(UnidadMedida, pk=unidad_medida_id)
    unidad_medida.estado = 0  # Set estado to 0 (False)
    unidad_medida.save()
    
    success_url = reverse_lazy('inventario:unidad_medida_lista-vw')  # Define success_url here

    return redirect(success_url)


class PruductoLista(SinPrivilegios, LoginRequiredMixin, ListView):

    permission_required = 'inventario.view_producto'

    login_url = 'bases/login-vw'

    model = Producto
    template_name = 'inventario/producto_lista.html'
    context_object_name = 'obj'

class ProductoNuevo(LoginRequiredMixin, CreateView):
    login_url='bases:login-vw'

    model = Producto
    template_name = 'inventario/producto_form.html'
    context_object_name = 'obj' 
    form_class = ProductoForm
    success_url = reverse_lazy('inventario:producto_lista-vw')
    

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        # return super().form.valid(form)
        return super(ProductoNuevo, self).form_valid(form)
    
class ProductoEditar(LoginRequiredMixin, UpdateView):
    login_url='bases:login-vw'

    model = Producto
    template_name = 'inventario/producto_form.html'
    context_object_name = 'obj' 
    form_class = ProductoForm
    success_url = reverse_lazy('inventario:producto_lista-vw')
    

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        # return super().form.valid(form)
        return super(ProductoEditar, self).form_valid(form) 
    
def update_producto_estado(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    producto.estado = 0  # Set estado to 0 (False)
    producto.save()
    
    success_url = reverse_lazy('inventario:producto_lista-vw')  # Define success_url here

    return redirect(success_url)
    