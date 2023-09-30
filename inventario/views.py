from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from .models import Categoria
from .forms import CategoriaForm
from django.urls import reverse_lazy

# Create your views here.

class CategoriaView(LoginRequiredMixin, ListView):
    login_url = 'bases/login-vw'

    model = Categoria
    template_name = 'inventario/categoria_list.html'
    context_object_name = 'obj'
    

class CategoriaNew(LoginRequiredMixin, CreateView):
    login_url='bases:login-vw'

    model = Categoria
    template_name = 'inventario/categoria_form.html'
    context_object_name = 'obj' 
    form_class = CategoriaForm
    success_url = reverse_lazy('inventario:categoria_list-vw')
    

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        # return super().form.valid(form)
        return super(CategoriaNew, self).form_valid(form)
    
class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    login_url='bases:login-vw'

    model = Categoria
    template_name = 'inventario/categoria_form.html'
    context_object_name = 'obj' 
    form_class = CategoriaForm
    success_url = reverse_lazy('inventario:categoria_list-vw')
    

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        # return super().form.valid(form)
        return super(CategoriaUpdate, self).form_valid(form)