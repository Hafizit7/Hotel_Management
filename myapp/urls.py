from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('room', room, name="room"),
    path('<int:id>', order, name="rooms_order"),
    path('order_registration', order_registration, name="order_registration")
    
]