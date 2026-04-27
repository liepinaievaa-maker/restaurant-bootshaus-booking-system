from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, time
from .forms import BookingForm
from .models import Booking

# Create your tests here.


class BookingFormTest(TestCase):
    """
    Tests for BookingForm validation.
    """

    def test_booking_form_valid_data(self):
        form = BookingForm(data={
            'full_name': 'John Smith',
            'email': 'john@example.com',
            'booking_date': date(2030, 5, 10),
            'booking_time': time(18, 0),
            'guests': 2,
            'special_request': 'Window seat please',
        })
        self.assertTrue(form.is_valid())

    def test_booking_form_rejects_single_name(self):
        form = BookingForm(data={
            'full_name': 'John',
            'email': 'john@example.com',
            'booking_date': date(2030, 5, 10),
            'booking_time': time(18, 0),
            'guests': 2,
        })
        self.assertFalse(form.is_valid())

    def test_booking_form_rejects_too_many_guests(self):
        form = BookingForm(data={
            'full_name': 'John Smith',
            'email': 'john@example.com',
            'booking_date': date(2030, 5, 10),
            'booking_time': time(18, 0),
            'guests': 40,
        })
        self.assertFalse(form.is_valid())

    def test_booking_form_rejects_past_date(self):
        form = BookingForm(data={
            'full_name': 'John Smith',
            'email': 'john@example.com',
            'booking_date': date(2020, 5, 10),
            'booking_time': time(18, 0),
            'guests': 2,
        })
        self.assertFalse(form.is_valid())

    def test_booking_slot_limit(self):
        user = User.objects.create_user(
            username='testuser',
            password='pass123'
        )

        for _ in range(3):
            Booking.objects.create(
                user=user,
                full_name='John Smith',
                email='john@example.com',
                booking_date=date(2030, 5, 10),
                booking_time=time(18, 0),
                guests=2,
            )

        form = BookingForm(data={
            'full_name': 'Jane Smith',
            'email': 'jane@example.com',
            'booking_date': date(2030, 5, 10),
            'booking_time': time(18, 0),
            'guests': 2,
        })

        self.assertFalse(form.is_valid())


class BookingViewTest(TestCase):
    """
    Tests for booking views.
    """

    def test_create_booking_requires_login(self):
        response = self.client.get(reverse('create_booking'))
        self.assertEqual(response.status_code, 302)