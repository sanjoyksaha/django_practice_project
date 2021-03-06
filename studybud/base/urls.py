from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('rooms', views.room, name="rooms"),
    path('room/<str:id>', views.room_details, name="room_details")
]