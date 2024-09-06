from django.urls import path
from bill.views import bill


urlpatterns = [
    path('bill/',bill,name='bill')
]
