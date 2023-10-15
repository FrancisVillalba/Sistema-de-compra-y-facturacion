from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('bases.urls','bases'), namespace='bases-vw')),
    path('inventario/',include(('inventario.urls','inventario'), namespace='inventario-vw')),
    path('compra/',include(('compra.urls','compra'), namespace='compra-vw')),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)