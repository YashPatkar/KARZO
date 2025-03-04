from rest_framework import serializers
from .models import DriverUser, PersonalDetails, VehicleDetails

class DriverUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverUser
        fields = ['id', 'email', 'created_at', 'updated_at']

class PersonalDetailsSerializer(serializers.ModelSerializer):
    driver = serializers.PrimaryKeyRelatedField(queryset=DriverUser.objects.all())  # Include driver reference

    class Meta:
        model = PersonalDetails
        fields = ['driver', 'name', 'age', 'birth_date', 'gender', 'phone', 'location', 'pincode', 'address']

class VehicleDetailsSerializer(serializers.ModelSerializer):
    driver = serializers.PrimaryKeyRelatedField(queryset=DriverUser.objects.all())  # Include driver reference

    class Meta:
        model = VehicleDetails
        fields = ['driver', 'vehicle_number', 'vehicle_manufacturer', 'vehicle_type', 'vehicle_model', 'vehicle_color', 'vehicle_registration_date']
