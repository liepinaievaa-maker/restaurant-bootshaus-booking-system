"""
URL configuration for bootshaus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from bookings.views import (
    home, create_booking, my_bookings, edit_booking, delete_booking, signup,
    contact
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('book/', create_booking, name='create_booking'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('my-bookings/', my_bookings, name='my_bookings'),
    path('edit-booking/<int:booking_id>/', edit_booking, name='edit_booking'),
    path(
        'delete-booking/<int:booking_id>/',
        delete_booking,
        name='delete_booking'
    ),
    path('accounts/signup/', signup, name='signup'),
    path('contact/', contact, name='contact'),
]
