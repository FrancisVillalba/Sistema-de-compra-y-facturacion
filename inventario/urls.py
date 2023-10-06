from django.urls import path

from inventario.views import CategoriaNuevo, CategoriaEditar, CategoriaView, MarcaEditar, MarcaLista, MarcaNuevo, SubCategoriaEditar, SubCategoriaNuevo, SubCategoriaView, update_categoria_estado, update_marca_estado,update_supcategoria_estado

urlpatterns = [
    path('categorias/', CategoriaView.as_view(), name='categoria_lista-vw'), 
    path('categorias/new', CategoriaNuevo.as_view(), name='categoria_nuevo-vw'), 
    path('categorias/editar/<int:pk>', CategoriaEditar.as_view(), name='categoria_editar-vw'), 
    path('categorias/editar/estado/<int:categoria_id>/', update_categoria_estado, name='categoria_editar_estado-vw'), 
    path('subcategorias/', SubCategoriaView.as_view(), name='subcategoria_lista-vw'), 
    path('subcategorias/nuevo', SubCategoriaNuevo.as_view(), name='subcategoria_nuevo-vw'), 
    path('subcategorias/editar/<int:pk>', SubCategoriaEditar.as_view(), name='subcategoria_editar-vw'), 
    path('subcategorias/editar/estado/<int:categoria_id>/', update_supcategoria_estado, name='subcategoria_editar_estado-vw'),
    path('marcas/', MarcaLista.as_view(), name='marca_lista-vw'), 
    path('marcas/nuevo', MarcaNuevo.as_view(), name='marca_nuevo-vw'), 
    path('marcas/editar/<int:pk>', MarcaEditar.as_view(), name='marca_editar-vw'), 
    path('marcas/editar/estado/<int:marca_id>/', update_marca_estado, name='marca_editar_estado-vw'),
    
]