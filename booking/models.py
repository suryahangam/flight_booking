from django.db import models
from user.models import CustomUser, Passenger
from flight.models import Flight, Seat
import uuid
import django.utils.timezone as timezone


# Booking
class Booking(models.Model):
    booking_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    num_of_passengers = models.IntegerField()

# BookingDetail
class BookingDetail(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    meal_preferences = models.CharField(max_length=255)
    special_request = models.CharField(max_length=255)

# Transaction
class Transaction(models.Model):
    booking_detail = models.ForeignKey(BookingDetail, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=255)
    booking_time = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField()
    payment_method = models.CharField(max_length=50)
    status = models.BooleanField(default=True)

# Baggage
class Baggage(models.Model):
    booking_detail = models.ForeignKey(BookingDetail, on_delete=models.CASCADE)
    weight = models.FloatField()
    extra_fees = models.DecimalField(max_digits=7, decimal_places=2)
    baggage_type = models.CharField(max_length=50)
    frequent_flyer_number = models.CharField(max_length=50)
    
    
class SeatHold(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    hold_time = models.DateTimeField(default=timezone.now)
    is_confirmed = models.BooleanField(default=False)

    def is_hold_expired(self):
        # Assuming a hold time limit of 15 minutes
        hold_duration = timezone.now() - self.hold_time
        return hold_duration.total_seconds() > 600  # 10 minutes
    
    
    