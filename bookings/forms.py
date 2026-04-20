from django import forms
from datetime import date
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

    def clean_booking_date(self):
        booking_date = self.cleaned_data.get('booking_date')
        if booking_date and booking_date < date.today():
            raise forms.ValidationError("You cannot book a date in the past.")
        return booking_date

    def clean_guests(self):
        guests = self.cleaned_data.get('guests')
        if guests is not None and (guests < 1 or guests > 10):
            raise forms.ValidationError(
                "Number of guests must be between 1 and 10."
            )
        return guests