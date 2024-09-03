from django.urls import path,include
from login.views import index
from login.views import signOff
from login.views import start


urlpatterns = [
    path('',include('customer.urls')),
    path('',index,name='index'),
    path('signOff/',signOff,name='signOff'),
    path('start/',start,name='start')
]

