from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # 👈 Add this line

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservations/', include('reservations.urls')),

    # 👇 Redirect root URL to /reservations/
    path('', lambda request: redirect('home')),
]
