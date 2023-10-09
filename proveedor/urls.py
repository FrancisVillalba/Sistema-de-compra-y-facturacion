from django.urls import path

from proveedor.views import ProveedorEditar, ProveedorLista, ProveedorNuevo, update_proveedor_estado

urlpatterns = [
    path('proveedores/', ProveedorLista.as_view(), name='proveedor_lista-vw'), 
    path('proveedores/nuevo', ProveedorNuevo.as_view(), name='proveedor_nuevo-vw'), 
    path('proveedores/editar/<int:pk>', ProveedorEditar.as_view(), name='proveedor_editar-vw'), 
    path('proveedores/editar/estado/<int:proveedor_id>/', update_proveedor_estado, name='proveedor_editar_estado-vw'),
]