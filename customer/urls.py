from django.urls import path
from customer.views import customer
from customer.views import addCustomer
from customer.views import deleteCustomer
from customer.views import editCustomer
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('customer/',customer,name='customer'),
    path('addCustomer/',addCustomer,name='addCustomer'),
    path('customer/deleteCustomer/<int:codigo>',deleteCustomer,name='deleteCustomer'),
    path('editCustomer/',editCustomer,name='editCustomer')



]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
