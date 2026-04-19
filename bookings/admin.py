from django.contrib import admin
from .models import Booking


# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Booking model.
    """

    list_display = (
        'full_name',
        'booking_date',
        'booking_time',
        'guests',
        'status',
    )
    list_filter = ('status', 'booking_date')
    search_fields = ('full_name', 'email')
