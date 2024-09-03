from django.db import models

# Create your models here.

class Customer(models.Model):
    codigo= models.AutoField(primary_key=True)
    name= models.CharField(max_length=255)
    lastName= models.CharField(max_length=255)
    phone= models.CharField(max_length=12)
    address= models.TextField()
    image= models.ImageField(upload_to='customer.image', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.codigo}: {self.name}"
