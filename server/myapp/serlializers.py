from rest_framework import serializers
from .models import Laundry,Repair,Customer

class LaundrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laundry
        fields = ('id', 'Name', 'Latitude', 'Longitude', 'Address')

class RepairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repair
        fields = ('id', 'Name', 'Latitude', 'Longitude', 'Address')

class CustomerSelializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('ID', 'PW', 'Phone', 'IsMale', 'BirthDate', 'Email', 'FavoriteLaundry', 'FavoriteRepair')
