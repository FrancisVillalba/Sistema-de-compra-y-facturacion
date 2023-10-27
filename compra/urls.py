from django.urls import path

from compra.views import  CompraLista, ProveedorEditar, ProveedorLista, ProveedorNuevo, compras, update_proveedor_estado, compra_eliminar_detalle

urlpatterns = [
    path('proveedores/', ProveedorLista.as_view(), name='proveedor_lista-vw'), 
    path('proveedores/nuevo', ProveedorNuevo.as_view(), name='proveedor_nuevo-vw'), 
    path('proveedores/editar/<int:pk>', ProveedorEditar.as_view(), name='proveedor_editar-vw'), 
    path('proveedores/editar/estado/<int:proveedor_id>/', update_proveedor_estado, name='proveedor_editar_estado-vw'),

    path('compras/', CompraLista.as_view(), name='compras_lista-vw'), 
    path('compras/nuevo', compras, name='compras_nuevo-vw'), 
    path('compras/editar/<int:compra_id>', compras, name='compras_editar-vw'),  
    path('compras/detalle/delete/<int:detalle_id>/', compra_eliminar_detalle, name='compra_detalle_eliminar-vw'),
]