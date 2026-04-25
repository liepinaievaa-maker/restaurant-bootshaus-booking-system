# Restaurant bootshaus booking system

## Project Overwiev

 - Bootshaus Restaurant Booking System is a web application that allows users to create, manage, and modify table reservations online. The platform is designed to simplify the booking process for customers while providing restaurant staff with an efficient way to manage reservations.

 - Users can register an account, log in, and book tables for specific dates and times. The system includes validation rules such as limiting bookings per time slot and ensuring valid input for guest numbers and booking details.

 - The application also provides a contact form, allowing visitors to send inquiries directly to the restaurant.

 - The project was built using Django and deployed on Heroku.

## User Experience (UX)

### Target Audience

#### The Bootshaus Restaurant Booking System is designed for:

 - Customers who want to easily reserve a table online
 - Restaurant staff who need a simple way to manage bookings
 - Visitors who want to contact the restaurant with inquiries

### User Goals

#### Users visiting the website expect to:

 - Create an account and log in securely
 - Book a table for a specific date and time
 - View and manage their existing reservations
 - Edit or cancel bookings if needed
 - Contact the restaurant for additional questions

### Site Owner Goals

#### The site owner (restaurant) aims to:

 - Manage reservations efficiently
 - Prevent overbooking using time slot limits
 - Collect customer booking information
 - Receive messages through the contact form
 - View and manage bookings via the admin panel

### User Stories

#### As a user, I want to:

 - Register an account so that I can make bookings
 - Log in and log out securely
 - Book a table for a chosen date and time
 - View my bookings
 - Edit or cancel my bookings
 - Receive feedback when actions are successful or invalid 

#### As a site owner, I want to:

 - View all bookings in the admin panel
 - Manage customer reservations
 - Receive contact messages from users


## Features


### Navigation

- Responsive navigation bar available on all pages
- Links to Home, Book Table, Contact, Login, and Sign Up
- Dynamic navigation options based on user authentication

### User Authentication

- Users can register an account
- Users can log in and log out securely
- Only authenticated users can create bookings
- Booking pages are protected using login-required access

### Booking System

- Users can create table reservations
- Bookings are made for specific dates and time slots
- Time slots are limited to hourly intervals (12:00 – 21:00)
- Each time slot allows a maximum of 3 bookings
- Guest numbers are limited between 1 and 10

### Booking Management

- Users can view their bookings
- Users can edit existing bookings
- Users can delete bookings
- Bookings are filtered per user

### Validation and Error Handling

- Users cannot book past dates
- Guest numbers are validated (1–10 guests)
- Time slot availability is checked to prevent overbooking
- Full name must include at least first and last name
- Clear error messages are displayed for invalid input

### Contact Page

- Users can send messages to the restaurant
- Contact form includes name, email, and message
- Messages are stored in the database
- Admin can view contact requests

### Admin Panel

- Admin can view and manage all bookings
- Admin can view contact messages
- Admin has full control over booking data

### User Feedback

- Success messages displayed after:

- Creating bookings
- Editing bookings
- Deleting bookings
- Sending contact messages

### Responsive Design

- Built with Bootstrap for responsive layout
- Works across different screen sizes