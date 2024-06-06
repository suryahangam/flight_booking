import random
from flight.models import Flight



def generate_flight_number(aircraft_id, departure_time):
    base_number = 1000
    time_category = determine_time_category(departure_time)
    increment = time_category * 100  # Each time category increments by 100
    
    while True:
        # Generate a potential flight number within the time category range
        flight_number = base_number + increment + random.randint(0, 99)
        random2 = aircraft_id + str(random.randint(1, 9))
        
        unique_flight_number = f'{flight_number}-{random2}'
        if not flight_number_in_use(unique_flight_number):
            return unique_flight_number

def determine_time_category(departure_time):
    # Converts hour of departure time to a time category
    hour = departure_time.hour
    if 6 <= hour < 12:
        return 1  # Morning
    elif 12 <= hour < 18:
        return 2  # Afternoon
    elif 18 <= hour < 24:
        return 3  # Evening
    else:
        return 4  # Night

def flight_number_in_use(flight_number):
    # Placeholder function to check if a flight number is already in use
    return Flight.objects.filter(flight_number=flight_number).exists()
 

# # Example usage with datetime
# import datetime


# flights = Flight.objects.all()
# for flight in flights:
#     dep_time = flight.departure_time
#     aircraft_id = flight.aircraft.aircraft_unique_id
#     flight.flight_number = generate_flight_number(aircraft_id[-4:], dep_time)
#     flight.save()

# print(generate_flight_number(aircraft_id, datetime.datetime(2024, 6, 1, 9, 0)))  # International morning flight
# print(generate_flight_number(datetime.datetime(2024, 6, 1, 22, 0)))  # Domestic night flight
