from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('service/<str:id>', views.servicepage, name='service'),
    path('appointment/', views.appointmentform, name='appointment'),
]
