from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking


# Create your views here.
def home(request):
    """
    View for homepage.
    """
    return render(request, 'bookings/home.html')


@login_required
def create_booking(request):
    """
    View for creating a booking.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return render(request, 'bookings/success.html')
    else:
        form = BookingForm()

    return render(request, 'bookings/create_booking.html', {'form': form})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})