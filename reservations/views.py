from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm

# Home Page View
def home(request):
    return render(request, 'reservations/home.html')

# Make Reservation View
def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_reservations')
    else:
        form = ReservationForm()
    return render(request, 'reservations/make_reservation.html', {'form': form})

# View Reservations Page View
def view_reservations(request):
    reservations = Reservation.objects.all().order_by('-date', '-time')
    return render(request, 'reservations/view_reservations.html', {
        'reservations': reservations
    })

def reservation_success(request):
    return render(request, 'reservations/reservation_success.html')