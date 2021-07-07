from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=122)
    lastname = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    address = models.CharField(max_length=122)
    city = models.CharField(max_length=122)
    state= models.CharField(max_length=122)
    zip= models.CharField(max_length=122)
    message= models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.firstname
    

