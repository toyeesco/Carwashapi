from django.shortcuts import render
from .models import Booking, CarWash
from .serializers import BookingSerializer, CarWashSerializer
from rest_framework import generics
from  rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

# Create your views here.


class CarWashListView(generics.ListCreateAPIView):
    queryset = CarWash.objects.all()
    serializer_class = CarWashSerializer
    permission_classes = [IsAuthenticated]


class CarWashDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarWash.objects.all()
    serializer_class = CarWashSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookingListView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "id"
