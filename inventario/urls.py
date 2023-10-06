from django.urls import path

from inventario.views import CategoriaNuevo, CategoriaEditar, CategoriaView, SubCategoriaEditar, SubCategoriaNuevo, SubCategoriaView, update_categoria_estado,update_supcategoria_estado

urlpatterns = [
    path('categorias/', CategoriaView.as_view(), name='categoria_lista-vw'), 
    path('categorias/new', CategoriaNuevo.as_view(), name='categoria_nuevo-vw'), 
    path('categorias/editar/<int:pk>', CategoriaEditar.as_view(), name='categoria_editar-vw'), 
    path('categorias/editar/estado/<int:categoria_id>/', update_categoria_estado, name='categoria_editar_estado-vw'), 
    path('subcategorias/', SubCategoriaView.as_view(), name='subcategoria_lista-vw'), 
    path('subcategorias/nuevo', SubCategoriaNuevo.as_view(), name='subcategoria_nuevo-vw'), 
    path('subcategorias/editar/<int:pk>', SubCategoriaEditar.as_view(), name='subcategoria_editar-vw'), 
    path('subcategorias/editar/estado/<int:categoria_id>/', update_supcategoria_estado, name='subcategoria_editar_estado-vw'),
]