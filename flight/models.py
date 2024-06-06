from django.db import models
import uuid

# Aircraft
class Aircraft(models.Model):
    aircraft_unique_id = models.CharField(max_length=255, unique=True)
    model = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    capacity = models.IntegerField()
    usage_capacity = models.IntegerField()
    year_of_manufacture = models.DateField()
    last_maintenance_date = models.DateField()
    
    def __str__(self):
        return self.model

# Seat
class Seat(models.Model):
    seat_number = models.CharField(max_length=10)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    class_type = models.CharField(max_length=50)
    is_window_seat = models.BooleanField(default=False)
    is_aisle_seat = models.BooleanField(default=False)
    is_emergency_exit = models.BooleanField(default=False)
    seat_ranking = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.seat_number} - {self.aircraft}'

# Flight
class Flight(models.Model):
    flight_number = models.CharField(max_length=255, null=True)
    route = models.ForeignKey('Route', on_delete=models.CASCADE)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    flight_status = models.CharField(max_length=50)
    basic_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    
    origin_terminal = models.CharField(max_length=50, default='Terminal 1')
    destination_terminal = models.CharField(max_length=50, default='Terminal 2')
    
    # Add baggage allowance as well
    
    def __str__(self):
        return f'{self.route} - {self.departure_time}: Flight number: {self.flight_number}'

    def get_duration(self):
        duration = self.arrival_time - self.departure_time
        hours = duration.seconds // 3600
        minutes = (duration.seconds % 3600) // 60
        return f'{hours} hours {minutes} minutes'

# Route
class Route(models.Model):
    origin_airport = models.ForeignKey('Airport', related_name='origin_routes', on_delete=models.CASCADE)
    destination_airport = models.ForeignKey('Airport', related_name='destination_routes', on_delete=models.CASCADE)
    distance = models.FloatField() # in miles
    
    def __str__(self) -> str:
        return f'{self.origin_airport} to {self.destination_airport}'

# Airport
class Airport(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3, null=True)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name