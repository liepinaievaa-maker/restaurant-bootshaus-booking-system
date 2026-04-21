from django import forms
from datetime import date, time
from .models import Booking

TIME_SLOT_CHOICES = [
    (time(12, 0), '12:00'),
    (time(13, 0), '13:00'),
    (time(14, 0), '14:00'),
    (time(15, 0), '15:00'),
    (time(16, 0), '16:00'),
    (time(17, 0), '17:00'),
    (time(18, 0), '18:00'),
    (time(19, 0), '19:00'),
    (time(20, 0), '20:00'),
    (time(21, 0), '21:00'),
]


class BookingForm(forms.ModelForm):
    """
    Form for creating and updating bookings.
    """

    booking_time = forms.TypedChoiceField(
        choices=TIME_SLOT_CHOICES,
        coerce=lambda x: time.fromisoformat(x) if isinstance(x, str) else x,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

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
            'guests': forms.NumberInput(
                attrs={'class': 'form-control', 'min': 1, 'max': 10}
            ),
            'special_request': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 4}
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

    def clean(self):
        cleaned_data = super().clean()
        booking_date = cleaned_data.get('booking_date')
        booking_time = cleaned_data.get('booking_time')

        if booking_date and booking_time:
            existing_bookings = Booking.objects.filter(
                booking_date=booking_date,
                booking_time=booking_time
            )

            # If editing an existing booking, exclude that booking itself
            if self.instance.pk:
                existing_bookings = (
                    existing_bookings.exclude(pk=self.instance.pk)
                )

            if existing_bookings.count() >= 3:
                raise forms.ValidationError(
                    "This hourly booking slot is fully booked. "
                    "Please choose another available hour."
                )

        return cleaned_data