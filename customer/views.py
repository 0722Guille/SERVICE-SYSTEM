from django.shortcuts import render,redirect
from .models import Customer

# Create your views here.

def customer(request):
    customers= Customer.objects.all()
    
    context={
        'customers':customers
    }
    
    
    return render(request,'customer.html',context)


def addCustomer(request):
    
    name=request.POST['addCustomer']
    lastName= request.POST['addlastName']
    phone=request.POST['addPhone']
    address= request.POST['addAddress']
    image= request.FILES.get('image')
    
    
    customer=Customer.objects.create(
        name=name,
        lastName=lastName,
        phone= phone,
        address=address,
        image=image
        
    )
    
    return redirect('customer')


def deleteCustomer(request,codigo):
    customer=Customer.objects.get(codigo=codigo)
    customer.delete()
    
    
    return redirect('customer')




def editCustomer(request):
    
    if request.method=='POST':
        
        idcodigo=request.POST['idCodigo']
        name=request.POST['editCustomer']
        lastName= request.POST['editlastName']
        phone=request.POST['editPhone']
        address=request.POST['editAddress']
        
        
        
        customer= Customer.objects.get(pk=idcodigo)
        customer.name=name
        customer.lastName=lastName
        customer.phone=phone
        customer.address=address
        customer.save()
    return redirect('customer')