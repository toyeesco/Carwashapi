from django.db import models
from location_field.models.plain import PlainLocationField


# Create your models here.

class CarWash(models.Model):
    name = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=200, unique=True)
    city = models.CharField(max_length=250)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Booking(models.Model):

    SERVICES = [
        ('VACUUM', 'VACUUM'),
        ('WAX', 'WAX'),
        ('TIREBLACK', 'TIREBLACK'),
        ('WASH', 'WASH')
    ]

    VEHICLE_TYPE = [
        ('CAR', 'CAR'),
        ('BICYCLE', 'BICYCLE'),
        ('TRUCK', 'TRUCK'),
        ('CASTER', 'CASTER')
    ]

    car_wash = models.ForeignKey(CarWash, on_delete=models.CASCADE, blank=True,null=True)
    client_name = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=50, unique=True)
    address = models.CharField(max_length=250, blank=True, null=False)
    vehicle = models.CharField(choices=VEHICLE_TYPE, max_length=200)
    services = models.CharField(choices=SERVICES, max_length=200)
    amount = models.DecimalField(max_length=200, max_digits=10, decimal_places=2)
    date = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.client_name

