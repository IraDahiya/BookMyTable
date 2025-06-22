from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ✅ Home page view
    path('make/', views.make_reservation, name='make_reservation'),  # Reservation form
    path('view/', views.view_reservations, name='view_reservations'),  # User reservation view
    path('success/', views.reservation_success, name='reservation_success'),  # Success page
    path('all/', views.view_reservations, name='view_reservations'),  # Admin/all reservations (same view)
]
