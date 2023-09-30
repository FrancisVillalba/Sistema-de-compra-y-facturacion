from django.urls import path
from .views import CategoriaView, CategoriaNew, CategoriaUpdate

urlpatterns = [
    path('categorias/', CategoriaView.as_view(), name='categoria_list-vw'), 
    path('categorias/new', CategoriaNew.as_view(), name='categoria_new-vw'), 
    path('categorias/edit/<int:pk>', CategoriaUpdate.as_view(), name='categoria_edit-vw'), 
]