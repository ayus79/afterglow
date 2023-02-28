from django.contrib import admin
from .models import Services, Appointment

# Register your models here.
admin.site.register([Services, Appointment])
