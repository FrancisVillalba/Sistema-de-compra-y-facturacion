from django.urls import path

from inventario.views import CategoriaNuevo, CategoriaEditar, CategoriaView, MarcaEditar, MarcaLista, MarcaNuevo, ProductoEditar, ProductoNuevo, PruductoLista, SubCategoriaEditar, \
  SubCategoriaNuevo,  SubCategoriaView, update_categoria_estado, update_marca_estado, update_producto_estado, \
  update_supcategoria_estado, UnidadMedidaEditar, UnidadMedidaLista, UnidadMedidaNuevo, update_unidad_medida_estado

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


    path('unidad_medidas/', UnidadMedidaLista.as_view(), name='unidad_medida_lista-vw'), 
    path('unidad_medidas/nuevo', UnidadMedidaNuevo.as_view(), name='unidad_medida_nuevo-vw'), 
    path('unidad_medidas/editar/<int:pk>', UnidadMedidaEditar.as_view(), name='unidad_medida_editar-vw'), 
    path('unidad_medidas/editar/estado/<int:unidad_medida_id>/', update_unidad_medida_estado, name='unidad_medida_editar_estado-vw'),


    path('producto/', PruductoLista.as_view(), name='producto_lista-vw'), 
    path('producto/nuevo', ProductoNuevo.as_view(), name='producto_nuevo-vw'), 
    path('producto/editar/<int:pk>', ProductoEditar.as_view(), name='producto_editar-vw'), 
    path('producto/editar/estado/<int:producto_id>/', update_producto_estado, name='producto_editar_estado-vw'),
    
]