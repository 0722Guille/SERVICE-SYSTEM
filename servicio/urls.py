from django.urls import path,include
from servicio.views import services
from servicio.views import addServices
from servicio.views import deleteService


urlpatterns = [
    path('',include('bill.urls')),
    path('services/',services,name='services'),
    path('addServices/',addServices, name='addServices'),
    path('services/deleteService/<int:codigoServices>',deleteService,name='codigoServices')
]
