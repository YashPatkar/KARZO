from rest_framework import serializers
from .models import DriverUser, PersonalDetails, VehicleDetails

class DriverUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverUser
        fields = ['id', 'email', 'created_at', 'updated_at']

class PersonalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetails
        fields = ['name', 'age', 'birth_date', 'gender', 'phone', 'location', 'pincode', 'address']

class VehicleDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleDetails
        fields = ['vehicle_number', 'vehicle_manufacturer', 'vehicle_type', 'vehicle_model', 'vehicle_color', 'vehicle_registration_date']