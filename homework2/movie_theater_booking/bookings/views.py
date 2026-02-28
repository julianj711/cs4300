from django.shortcuts import render, get_object_or_404
from .models import Movie, Seat, Booking
from rest_framework import viewsets
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

#For CRUD operations on movies.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

#For seat availability and booking
class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

#For users to book seats and view their booking history
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

#Renders movie list 
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

#Renders seat booking 
def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.all()
    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats})

#Renders booking history
def booking_history(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})