from django.db import models

# Create your models here.

class Services(models.Model):
    codigoServices= models.AutoField(primary_key=True)
    nameServices= models.CharField(max_length=255)
    descriptionServices= models.CharField(max_length=255)
    gmailServicesgmail= models.CharField(max_length=255)
    princeServices= models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self) -> str:
        return f'{self.codigoServices}, {self.nameServices}'    
