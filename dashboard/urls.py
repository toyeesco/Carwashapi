from django.urls import path
from .views import CarWashListView, CarWashDetailView, BookingListView, BookingDetailView

urlpatterns = [
    path('car_wash_list/', CarWashListView.as_view(), name='car_wash_list'),
    path('car_wash_detail/<int:id>/', CarWashDetailView.as_view(), name='car_wash_detail'),
    path('booking_list/', BookingListView.as_view(), name='booking_list'),
    path('booking_detail/<int:id>/', BookingDetailView.as_view(), name='booking_detail')

]