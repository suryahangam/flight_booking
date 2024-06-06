from django.urls import path
from .views import HomeView, FlightListView, FlightDetailView, \
    SeatSelectionView, TravellerDetailView, PaymentView, BookingConfirmationView, \
    select_or_remove_seat, booking_login_redirection


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('flight-list/', FlightListView.as_view(), name='flight_list'),
    path('flight-detail/<slug:flight_number>/', FlightDetailView.as_view(), name='flight_detail'),
    path('seat-selection/', SeatSelectionView.as_view(), name='seat_selection'),
    path('traveller-detail/', TravellerDetailView.as_view(), name='traveller_detail'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('booking-confirmation/<str:booking_id>', 
         BookingConfirmationView.as_view(), 
         name='booking_confirmation'),
    path('select-seat/', select_or_remove_seat, name='select_seat'),
    path('booking-login-redirection/', booking_login_redirection, 
         name='booking_login_redirection'),
]