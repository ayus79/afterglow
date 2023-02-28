from django.db import models
from django.utils import timezone

now = timezone.now()
# Create your models here.
class Services(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

class Appointment(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=120)
    phonenumber = models.CharField(max_length=15)
    servicetype = models.CharField(max_length=100)
    
    def __str__(self):
        return self.fullname + ' | ' + self.servicetype