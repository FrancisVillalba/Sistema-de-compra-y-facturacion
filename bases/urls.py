from django.urls import path
from bases.views import Home

app_name = 'bases'

urlpatterns = [ 
     path('', Home.as_view(), name='home-vw'),
]
