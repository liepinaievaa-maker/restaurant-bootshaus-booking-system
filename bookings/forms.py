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

        widgets = {
            'full_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control'}
            ),
            'booking_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'booking_time': forms.TimeInput(
                attrs={'class': 'form-control', 'type': 'time'}
            ),
            'guests': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'special_request': forms.Textarea(
                attrs={'class': 'form-control'}
            ),
        }