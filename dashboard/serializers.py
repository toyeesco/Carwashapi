from rest_framework import serializers
from .models import CarWash, Booking



class CarWashSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    phone_number = serializers.CharField(max_length=15)
    city = serializers.CharField(max_length=200)


    class Meta:
        model = CarWash
        fields = ['id', 'name', 'phone_number', 'city', 'location']


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ['id',  'date', 'client_name', 'phone_number', 'address', 'email', 'vehicle', 'services', 'amount']





