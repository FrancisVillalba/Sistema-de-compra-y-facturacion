from django.urls import path  
from bases.views import Home, HomeSinPrivilegios
from django.contrib.auth import views as auth_views


urlpatterns = [ 
      path('',Home.as_view(), name='home-vw'), 
      path('login/',auth_views.LoginView.as_view(template_name='bases/login.html'), name='login-vw'),
      path('logout/',auth_views.LogoutView.as_view(template_name='bases/login.html'), name='logout-vw'),
      path('sin_privilegios/',HomeSinPrivilegios.as_view(), name='sin_privilegios-vw'),
]
