from django.db import models

# Create your models here.
class Aplication(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    password=models.CharField(max_length=250)
    
    def __str__(self):
        return f"name: {self.name}, email: {self.email}, password: {self.password}"
        
