from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking
from django.contrib import messages


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

            messages.success(request, "Your booking has been created successfully.")
            return redirect('my_bookings')

    else:
        form = BookingForm()

    return render(request, 'bookings/create_booking.html', {'form': form})


@login_required
def my_bookings(request):
    """
    View to display bookings for the logged-in user.
    """
    bookings = Booking.objects.filter(user=request.user).order_by(
        '-booking_date'
    )
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})


@login_required
def edit_booking(request, booking_id):
    """
    View to edit a booking.
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking has been updated.")
            return redirect('my_bookings')
    else:
        form = BookingForm(instance=booking)

    return render(request, 'bookings/edit_booking.html', {'form': form})


@login_required
def delete_booking(request, booking_id):
    """
    View to delete a booking.
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Your booking has been deleted.")
        return redirect('my_bookings')

    return render(
        request,
        'bookings/delete_booking.html',
        {'booking': booking}
    )