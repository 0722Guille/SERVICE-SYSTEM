from django.shortcuts import render,redirect
from .models import Services

# Create your views here.

def services(request):
    
    services=Services.objects.all()
    
    
    context={
        'services':services
    }
    return render(request,'services.html',context)


def addServices(request):
    nameServices= request.POST['nameServices']
    descriptionServices= request.POST['descriptionServices']
    gmailServicesgmail= request.POST['gmailServicesgmail']
    princeServices=request.POST['princeServices']
    
    services= Services.objects.create(
        nameServices=nameServices,
        descriptionServices=descriptionServices,
        gmailServicesgmail=gmailServicesgmail,
        princeServices=princeServices
    )
    
    return redirect('services')



def deleteService(request,codigoServices):
    services=Services.objects.get(codigoServices=codigoServices)
    services.delete()
    return redirect('services')
