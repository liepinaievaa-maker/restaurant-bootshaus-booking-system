from django.shortcuts import render
from .forms import BookingForm


# Create your views here.
def home(request):
    """
    View for homepage.
    """
    return render(request, 'bookings/home.html')


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