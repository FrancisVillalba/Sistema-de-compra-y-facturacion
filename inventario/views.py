from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DeleteView, CreateView, UpdateView
from .models import Categoria, Marca, SubCategoria
from .forms import CategoriaForm, MarcaForm, SubCategoriaForm
from django.urls import reverse_lazy

# Create your views here.

class CategoriaView(LoginRequiredMixin, ListView):
    login_url = 'bases/login-vw'

    model = Categoria
    template_name = 'inventario/categoria_lista.html'
    context_object_name = 'obj'
    

class CategoriaNuevo(LoginRequiredMixin, CreateView):
    login_url='bases:login-vw'

    model = Categoria
    template_name = 'inventario/categoria_form.html'
    context_object_name = 'obj' 
    form_class = CategoriaForm
    success_url = reverse_lazy('inventario:categoria_lista-vw')
    

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        # return super().form.valid(form)
        return super(CategoriaNuevo, self).form_valid(form)
    
class CategoriaEditar(LoginRequiredMixin, UpdateView):
    login_url='bases:login-vw'

    model = Categoria
    template_name = 'inventario/categoria_form.html'
    context_object_name = 'obj' 
    form_class = CategoriaForm
    success_url = reverse_lazy('inventario:categoria_lista-vw')
    

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

class SubCategoriaView(LoginRequiredMixin, ListView):
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

class MarcaLista(LoginRequiredMixin, ListView):
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
    subcategoria = get_object_or_404(Marca, pk=marca_id)
    subcategoria.estado = 0  # Set estado to 0 (False)
    subcategoria.save()
    
    success_url = reverse_lazy('inventario:marca_lista-vw')  # Define success_url here

    return redirect(success_url)
    