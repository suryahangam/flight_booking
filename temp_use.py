airports = [
    {"name": "Heathrow Airport", "code": "LHR", "city": "London", "country": "UK", "latitude": 51.4700, "longitude": -0.4543},
    {"name": "Gatwick Airport", "code": "LGW", "city": "London", "country": "UK", "latitude": 51.1537, "longitude": -0.1821},
    {"name": "Manchester Airport", "code": "MAN", "city": "Manchester", "country": "UK", "latitude": 53.3651, "longitude": -2.2720},
    {"name": "Stansted Airport", "code": "STN", "city": "London", "country": "UK", "latitude": 51.8849, "longitude": 0.2349},
    {"name": "Luton Airport", "code": "LTN", "city": "London", "country": "UK", "latitude": 51.8747, "longitude": -0.3683},
    {"name": "Edinburgh Airport", "code": "EDI", "city": "Edinburgh", "country": "UK", "latitude": 55.9500, "longitude": -3.3725},
    {"name": "Birmingham Airport", "code": "BHX", "city": "Birmingham", "country": "UK", "latitude": 52.4539, "longitude": -1.7480},
    {"name": "Glasgow Airport", "code": "GLA", "city": "Glasgow", "country": "UK", "latitude": 55.8642, "longitude": -4.4326},
    {"name": "Bristol Airport", "code": "BRS", "city": "Bristol", "country": "UK", "latitude": 51.3827, "longitude": -2.7191},
    {"name": "Newcastle Airport", "code": "NCL", "city": "Newcastle", "country": "UK", "latitude": 55.0375, "longitude": -1.6917}
]


for airport in airports:
    obj, created = Airport.objects.get_or_create(
        name=airport["name"],
        code=airport["code"],
        city=airport["city"],
        country=airport["country"],
        latitude=airport["latitude"],
        longitude=airport["longitude"]
    )
    if created:
        print(f'Created {obj.name}')
    else:
        print(f'{obj.name} already exists')



# ----------------------------------------------------------------

routes = [{'source': 'LHR', 'destination': 'LGW', 'distance': '24.82'}, {'source': 'LHR', 'destination': 'MAN', 'distance': '151.70'}, {'source': 'LHR', 'destination': 'STN', 'distance': '41.16'}, {'source': 'LHR', 'destination': 'LTN', 'distance': '28.21'}, {'source': 'LHR', 'destination': 'EDI', 'distance': '331.69'}, {'source': 'LHR', 'destination': 'BHX', 'distance': '87.50'}, {'source': 'LHR', 'destination': 'GLA', 'distance': '344.42'}, {'source': 'LHR', 'destination': 'BRS', 'distance': '97.76'}, {'source': 'LHR', 'destination': 'NCL', 'distance': '251.75'}, {'source': 'LHR', 'destination': 'LPL', 'distance': '163.63'}, {'source': 'LHR', 'destination': 'EMA', 'distance': '101.08'}, {'source': 'LHR', 'destination': 'LBA', 'distance': '173.09'}, {'source': 'LHR', 'destination': 'ABZ', 'distance': '402.21'}, {'source': 'LHR', 'destination': 'BFS', 'distance': '324.99'}, {'source': 'LHR', 'destination': 'SOU', 'distance': '53.06'}, {'source': 'LHR', 'destination': 'NWI', 'distance': '111.28'}, {'source': 'LHR', 'destination': 'EXT', 'distance': '138.09'}, {'source': 'LHR', 'destination': 'CWL', 'distance': '124.54'}, {'source': 'LHR', 'destination': 'DSA', 'distance': '140.88'}, {'source': 'LGW', 'destination': 'MAN', 'distance': '176.51'}, {'source': 'LGW', 'destination': 'STN', 'distance': '53.61'}, {'source': 'LGW', 'destination': 'LTN', 'distance': '50.46'}, {'source': 'LGW', 'destination': 'EDI', 'distance': '356.26'}, {'source': 'LGW', 'destination': 'BHX', 'distance': '112.01'}, {'source': 'LGW', 'destination': 'GLA', 'distance': '369.22'}, {'source': 'LGW', 'destination': 'BRS', 'distance': '110.81'}, {'source': 'LGW', 'destination': 'NCL', 'distance': '275.56'}, {'source': 'LGW', 'destination': 'LPL', 'distance': '188.19'}, {'source': 'LGW', 'destination': 'EMA', 'distance': '125.74'}, {'source': 'LGW', 'destination': 'LBA', 'distance': '197.44'}, {'source': 'LGW', 'destination': 'ABZ', 'distance': '425.74'}, {'source': 'LGW', 'destination': 'BFS', 'distance': '348.83'}, {'source': 'LGW', 'destination': 'SOU', 'distance': '52.92'}, {'source': 'LGW', 'destination': 'NWI', 'distance': '122.30'}, {'source': 'LGW', 'destination': 'EXT', 'distance': '143.64'}, {'source': 'LGW', 'destination': 'CWL', 'distance': '137.66'}, {'source': 'LGW', 'destination': 'DSA', 'distance': '164.54'}, {'source': 'MAN', 'destination': 'STN', 'distance': '146.67'}, {'source': 'MAN', 'destination': 'LTN', 'distance': '130.31'}, {'source': 'MAN', 'destination': 'EDI', 'distance': '183.94'}, {'source': 'MAN', 'destination': 'BHX', 'distance': '66.64'}, {'source': 'MAN', 'destination': 'GLA', 'distance': '193.09'}, {'source': 'MAN', 'destination': 'BRS', 'distance': '138.27'}, {'source': 'MAN', 'destination': 'NCL', 'distance': '117.91'}, {'source': 'MAN', 'destination': 'LPL', 'distance': '23.93'}, {'source': 'MAN', 'destination': 'EMA', 'distance': '53.81'}, {'source': 'MAN', 'destination': 'LBA', 'distance': '42.73'}, {'source': 'MAN', 'destination': 'ABZ', 'distance': '265.13'}, {'source': 'MAN', 'destination': 'BFS', 'distance': '183.31'}, {'source': 'MAN', 'destination': 'SOU', 'distance': '171.30'}, {'source': 'MAN', 'destination': 'NWI', 'distance': '155.22'}, {'source': 'MAN', 'destination': 'EXT', 'distance': '188.13'}, {'source': 'MAN', 'destination': 'CWL', 'distance': '143.32'}, {'source': 'MAN', 'destination': 'DSA', 'distance': '52.54'}, {'source': 'STN', 'destination': 'LTN', 'distance': '25.74'}, {'source': 'STN', 'destination': 'EDI', 'distance': '316.84'}, {'source': 'STN', 'destination': 'BHX', 'distance': '92.77'}, {'source': 'STN', 'destination': 'GLA', 'distance': '334.14'}, {'source': 'STN', 'destination': 'BRS', 'distance': '131.35'}, {'source': 'STN', 'destination': 'NCL', 'distance': '231.78'}, {'source': 'STN', 'destination': 'LPL', 'distance': '163.60'}, {'source': 'STN', 'destination': 'EMA', 'distance': '92.87'}, {'source': 'STN', 'destination': 'LBA', 'distance': '158.05'}, {'source': 'STN', 'destination': 'ABZ', 'distance': '380.05'}, {'source': 'STN', 'destination': 'BFS', 'distance': '328.05'}, {'source': 'STN', 'destination': 'SOU', 'distance': '94.20'}, {'source': 'STN', 'destination': 'NWI', 'distance': '70.35'}, {'source': 'STN', 'destination': 'EXT', 'distance': '176.49'}, {'source': 'STN', 'destination': 'CWL', 'distance': '157.08'}, {'source': 'STN', 'destination': 'DSA', 'distance': '121.97'}, {'source': 'LTN', 'destination': 'EDI', 'distance': '306.92'}, {'source': 'LTN', 'destination': 'BHX', 'distance': '70.86'}, {'source': 'LTN', 'destination': 'GLA', 'distance': '321.45'}, {'source': 'LTN', 'destination': 'BRS', 'distance': '106.40'}, {'source': 'LTN', 'destination': 'NCL', 'distance': '225.21'}, {'source': 'LTN', 'destination': 'LPL', 'distance': '144.91'}, {'source': 'LTN', 'destination': 'EMA', 'distance': '77.51'}, {'source': 'LTN', 'destination': 'LBA', 'distance': '147.76'}, {'source': 'LTN', 'destination': 'ABZ', 'distance': '375.30'}, {'source': 'LTN', 'destination': 'BFS', 'distance': '308.65'}, {'source': 'LTN', 'destination': 'SOU', 'distance': '76.78'}, {'source': 'LTN', 'destination': 'NWI', 'distance': '89.09'}, {'source': 'LTN', 'destination': 'EXT', 'distance': '153.34'}, {'source': 'LTN', 'destination': 'CWL', 'distance': '131.78'}, {'source': 'LTN', 'destination': 'DSA', 'distance': '114.17'}, {'source': 'EDI', 'destination': 'BHX', 'distance': '250.32'}, {'source': 'EDI', 'destination': 'GLA', 'distance': '41.48'}, {'source': 'EDI', 'destination': 'BRS', 'distance': '316.72'}, {'source': 'EDI', 'destination': 'NCL', 'distance': '91.12'}, {'source': 'EDI', 'destination': 'LPL', 'distance': '181.99'}, {'source': 'EDI', 'destination': 'EMA', 'distance': '230.65'}, {'source': 'EDI', 'destination': 'LBA', 'distance': '159.24'}, {'source': 'EDI', 'destination': 'ABZ', 'distance': '97.37'}, {'source': 'EDI', 'destination': 'BFS', 'distance': '143.10'}, {'source': 'EDI', 'destination': 'SOU', 'distance': '355.24'}, {'source': 'EDI', 'destination': 'NWI', 'distance': '293.80'}, {'source': 'EDI', 'destination': 'EXT', 'distance': '360.39'}, {'source': 'EDI', 'destination': 'CWL', 'distance': '314.62'}, {'source': 'EDI', 'destination': 'DSA', 'distance': '194.92'}, {'source': 'BHX', 'destination': 'GLA', 'distance': '259.42'}, {'source': 'BHX', 'destination': 'BRS', 'distance': '84.80'}, {'source': 'BHX', 'destination': 'NCL', 'distance': '178.54'}, {'source': 'BHX', 'destination': 'LPL', 'distance': '76.18'}, {'source': 'BHX', 'destination': 'EMA', 'distance': '31.45'}, {'source': 'BHX', 'destination': 'LBA', 'distance': '97.63'}, {'source': 'BHX', 'destination': 'ABZ', 'distance': '328.56'}, {'source': 'BHX', 'destination': 'BFS', 'distance': '238.28'}, {'source': 'BHX', 'destination': 'SOU', 'distance': '105.24'}, {'source': 'BHX', 'destination': 'NWI', 'distance': '128.21'}, {'source': 'BHX', 'destination': 'EXT', 'distance': '138.66'}, {'source': 'BHX', 'destination': 'CWL', 'distance': '99.78'}, {'source': 'BHX', 'destination': 'DSA', 'distance': '77.29'}, {'source': 'GLA', 'destination': 'BRS', 'distance': '317.50'}, {'source': 'GLA', 'destination': 'NCL', 'distance': '121.64'}, {'source': 'GLA', 'destination': 'LPL', 'distance': '185.97'}, {'source': 'GLA', 'destination': 'EMA', 'distance': '243.99'}, {'source': 'GLA', 'destination': 'LBA', 'distance': '176.65'}, {'source': 'GLA', 'destination': 'ABZ', 'distance': '125.67'}, {'source': 'GLA', 'destination': 'BFS', 'distance': '109.00'}, {'source': 'GLA', 'destination': 'SOU', 'distance': '362.31'}, {'source': 'GLA', 'destination': 'NWI', 'distance': '318.75'}, {'source': 'GLA', 'destination': 'EXT', 'distance': '356.93'}, {'source': 'GLA', 'destination': 'CWL', 'distance': '311.89'}, {'source': 'GLA', 'destination': 'DSA', 'distance': '214.01'}, {'source': 'BRS', 'destination': 'NCL', 'distance': '256.08'}, {'source': 'BRS', 'destination': 'LPL', 'distance': '134.92'}, {'source': 'BRS', 'destination': 'EMA', 'distance': '116.19'}, {'source': 'BRS', 'destination': 'LBA', 'distance': '177.23'}, {'source': 'BRS', 'destination': 'ABZ', 'distance': '402.64'}, {'source': 'BRS', 'destination': 'BFS', 'distance': '268.86'}, {'source': 'BRS', 'destination': 'SOU', 'distance': '66.16'}, {'source': 'BRS', 'destination': 'NWI', 'distance': '192.13'}, {'source': 'BRS', 'destination': 'EXT', 'distance': '54.01'}, {'source': 'BRS', 'destination': 'CWL', 'distance': '26.93'}, {'source': 'BRS', 'destination': 'DSA', 'distance': '161.83'}, {'source': 'NCL', 'destination': 'LPL', 'distance': '126.70'}, {'source': 'NCL', 'destination': 'EMA', 'distance': '153.17'}, {'source': 'NCL', 'destination': 'LBA', 'distance': '80.96'}, {'source': 'NCL', 'destination': 'ABZ', 'distance': '150.82'}, {'source': 'NCL', 'destination': 'BFS', 'distance': '181.86'}, {'source': 'NCL', 'destination': 'SOU', 'distance': '282.76'}, {'source': 'NCL', 'destination': 'NWI', 'distance': '203.25'}, {'source': 'NCL', 'destination': 'EXT', 'distance': '305.86'}, {'source': 'NCL', 'destination': 'CWL', 'distance': '260.67'}, {'source': 'NCL', 'destination': 'DSA', 'distance': '111.04'}, {'source': 'LPL', 'destination': 'EMA', 'distance': '72.07'}, {'source': 'LPL', 'destination': 'LBA', 'distance': '61.07'}, {'source': 'LPL', 'destination': 'ABZ', 'distance': '268.52'}, {'source': 'LPL', 'destination': 'BFS', 'distance': '164.48'}, {'source': 'LPL', 'destination': 'SOU', 'distance': '176.42'}, {'source': 'LPL', 'destination': 'NWI', 'distance': '177.71'}, {'source': 'LPL', 'destination': 'EXT', 'distance': '181.19'}, {'source': 'LPL', 'destination': 'CWL', 'distance': '135.44'}, {'source': 'LPL', 'destination': 'DSA', 'distance': '76.42'}, {'source': 'EMA', 'destination': 'LBA', 'distance': '72.81'}, {'source': 'EMA', 'destination': 'ABZ', 'distance': '303.96'}, {'source': 'EMA', 'destination': 'BFS', 'distance': '236.18'}, {'source': 'EMA', 'destination': 'SOU', 'distance': '129.96'}, {'source': 'EMA', 'destination': 'NWI', 'distance': '109.71'}, {'source': 'EMA', 'destination': 'EXT', 'distance': '170.10'}, {'source': 'EMA', 'destination': 'CWL', 'distance': '130.89'}, {'source': 'EMA', 'destination': 'DSA', 'distance': '46.76'}, {'source': 'LBA', 'destination': 'ABZ', 'distance': '231.46'}, {'source': 'LBA', 'destination': 'BFS', 'distance': '191.77'}, {'source': 'LBA', 'destination': 'SOU', 'distance': '201.87'}, {'source': 'LBA', 'destination': 'NWI', 'distance': '146.80'}, {'source': 'LBA', 'destination': 'EXT', 'distance': '228.69'}, {'source': 'LBA', 'destination': 'CWL', 'distance': '184.62'}, {'source': 'LBA', 'destination': 'DSA', 'distance': '37.64'}, {'source': 'ABZ', 'destination': 'BFS', 'distance': '234.66'}, {'source': 'ABZ', 'destination': 'SOU', 'distance': '433.30'}, {'source': 'ABZ', 'destination': 'NWI', 'distance': '341.79'}, {'source': 'ABZ', 'destination': 'EXT', 'distance': '449.59'}, {'source': 'ABZ', 'destination': 'CWL', 'distance': '403.76'}, {'source': 'ABZ', 'destination': 'DSA', 'distance': '261.33'}, {'source': 'BFS', 'destination': 'SOU', 'distance': '326.67'}, {'source': 'BFS', 'destination': 'NWI', 'distance': '335.92'}, {'source': 'BFS', 'destination': 'EXT', 'distance': '295.32'}, {'source': 'BFS', 'destination': 'CWL', 'distance': '254.93'}, {'source': 'BFS', 'destination': 'DSA', 'distance': '226.11'}, {'source': 'SOU', 'destination': 'NWI', 'distance': '164.08'}, {'source': 'SOU', 'destination': 'EXT', 'distance': '90.98'}, {'source': 'SOU', 'destination': 'CWL', 'distance': '91.42'}, {'source': 'SOU', 'destination': 'DSA', 'distance': '175.44'}, {'source': 'NWI', 'destination': 'EXT', 'distance': '241.67'}, {'source': 'NWI', 'destination': 'CWL', 'distance': '215.54'}, {'source': 'NWI', 'destination': 'DSA', 'distance': '110.24'}, {'source': 'EXT', 'destination': 'CWL', 'distance': '45.87'}, {'source': 'EXT', 'destination': 'DSA', 'distance': '215.39'}, {'source': 'CWL', 'destination': 'DSA', 'distance': '174.29'}]


for i in routes:
    origin = Airport.objects.get(code=i['source'])
    destination = Airport.objects.get(code=i['destination'])
    obj, created = Route.objects.get_or_create(
        origin_airport=origin,
        destination_airport=destination,
        distance=i['distance']
    )
    
    if created:
        print(f'Created {obj.origin_airport} to {obj.destination_airport}')
    else:
        print(f'{obj.origin_airport} to {obj.destination_airport} already exists')
        
        

aircrafts = [
    {
        "aircraft_unique_id": "AC1-2024-UK01",
        "model": "Airbus A320",
        "manufacturer": "Airbus",
        "capacity": 180,
        "usage_capacity": 174,
        "year_of_manufacture": "2018-01-15",
        "last_maintenance_date": "2024-05-20"
    },
    {
        "aircraft_unique_id": "AC2-2024-UK02",
        "model": "Boeing 737-800",
        "manufacturer": "Boeing",
        "capacity": 189,
        "usage_capacity": 185,
        "year_of_manufacture": "2017-03-12",
        "last_maintenance_date": "2024-05-30"
    }
]

for aircraft in aircrafts:
    obj, created = Aircraft.objects.get_or_create(
        aircraft_unique_id=aircraft["aircraft_unique_id"],
        model=aircraft["model"],
        manufacturer=aircraft["manufacturer"],
        capacity=aircraft["capacity"],
        usage_capacity=aircraft["usage_capacity"],
        year_of_manufacture=aircraft["year_of_manufacture"],
        last_maintenance_date=aircraft["last_maintenance_date"]
    )
    
    
# ----------------------------------------------------------------
import datetime
from django.utils import timezone
from decimal import Decimal
from flight.models import Flight, Route, Aircraft  # Replace 'myapp' with the name of your Django app

# Start date
start_date = datetime.date(2024, 6, 1)

# Retrieve aircrafts
aircraft1 = Aircraft.objects.get(aircraft_unique_id="AC1-2024-UK01")
aircraft2 = Aircraft.objects.get(aircraft_unique_id="AC2-2024-UK02")
aircrafts = [aircraft1, aircraft2]

# Assume routes have been created in the database and fetched here
routes = Route.objects.all()

# Generate flights
for day in range(7):  # One week
    for route in routes:
        for flight_number in range(2):  # Two flights per day per route
            departure_time = datetime.datetime.combine(start_date + datetime.timedelta(days=day),
                                                       datetime.time(9 + 12 * flight_number, 0))  # 9 AM and 9 PM
            flight_duration = datetime.timedelta(hours=route.distance / 100 + 1)  # Simple formula to estimate flight time
            arrival_time = timezone.make_aware(departure_time + flight_duration)
            
            Flight.objects.create(
                route=route,
                aircraft=aircrafts[flight_number % len(aircrafts)],
                departure_time=timezone.make_aware(departure_time),
                arrival_time=arrival_time,
                flight_status='Scheduled',
                basic_rate=Decimal(round(50 + route.distance * 0.5, 2))  # Example fare calculation
            )

print("Flights scheduled successfully.")




# Seat creation -------------------------------------
seats_data = []

# First Class
for row in range(1, 3):
    for col in ['A', 'B', 'C', 'D']:
        seat_number = f"{row}{col}"
        seats_data.append({
            "seat_number": seat_number,
            "aircraft": aircraft1,
            "class_type": "First Class",
            "is_window_seat": col in ['A', 'D'],
            "is_aisle_seat": col in ['B', 'C'],
            "is_emergency_exit": False,
            "seat_ranking": "Premium",
            "description": "First Class seat with extra legroom and premium service."
        })
        
# Business Class
for row in range(3, 7):
    for col in ['A', 'B', 'C', 'D']:
        seat_number = f"{row}{col}"
        seats_data.append({
            "seat_number": seat_number,
            "aircraft": aircraft1,
            "class_type": "Business Class",
            "is_window_seat": col in ['A', 'D'],
            "is_aisle_seat": col in ['B', 'C'],
            "is_emergency_exit": row == 6,
            "seat_ranking": "High",
            "description": "Business Class seat with extra legroom and premium service."
        })

# Economy Class
for row in range(7, 32):
    for col in ['A', 'B', 'C', 'D', 'E', 'F']:
        seat_number = f"{row}{col}"
        seats_data.append({
            "seat_number": seat_number,
            "aircraft": aircraft1,
            "class_type": "Economy Class",
            "is_window_seat": col in ['A', 'F'],
            "is_aisle_seat": col in ['C', 'D'],
            "is_emergency_exit": row in [7, 22],
            "seat_ranking": "Standard",
            "description": "Economy Class seat with standard amenities."
        })
