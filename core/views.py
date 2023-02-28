from django.shortcuts import render, redirect
from .models import Services, Appointment
from django.contrib import messages
import datetime

# Create your views here.
def homepage(request):
    service = Services.objects.all()
    today = datetime.date.today()
    year = today.year
    context = {
        'service': service,
        'year': year
    }
    return render(request, 'index.html', context)

def servicepage(request, id):
    service = Services.objects.filter(id=id)
    context = {
        'service': service
    }
    return render(request, 'service.html', context)

def appointmentform(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        servicetype = request.POST.get('servicetype')
        appointment_data = Appointment(
            fullname = fullname,
            email = email,
            phonenumber = phonenumber,
            servicetype = servicetype
        )
        appointment_data.save()
    return redirect('home')