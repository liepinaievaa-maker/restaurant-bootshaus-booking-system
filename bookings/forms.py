from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Form for creating and updating bookings.
    """

    class Meta:
        model = Booking
        fields = [
            'full_name',
            'email',
            'booking_date',
            'booking_time',
            'guests',
            'special_request',
        ]