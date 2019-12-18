from django.shortcuts import render
from rest_framework import viewsets
from .models import Laundry,Repair, Customer
from .serlializers import LaundrySerializer, RepairSerializer, CustomerSelializer

class LaundryView(viewsets.ModelViewSet):
    queryset = Laundry.objects.all()
    serializer_class = LaundrySerializer

class RepairView(viewsets.ModelViewSet):
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer

class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSelializer



