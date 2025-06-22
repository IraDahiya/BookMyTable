from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('make/', views.make_reservation, name='make_reservation'),
    path('view/', views.view_reservations, name='view_reservations'),
    path('success/', views.reservation_success, name='reservation_success'),
    path('all/', views.view_reservations, name='view_reservations'),
]
