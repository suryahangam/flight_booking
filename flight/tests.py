from django.test import TestCase, Client
from django.urls import reverse
from flight.models import Airport, Flight, Route, Aircraft, Seat
from booking.models import Booking, SeatHold, CustomUser

from datetime import datetime
from django.utils import timezone



class HomeViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        Airport.objects.create(code='LHR', name='Heathrow Airport', city='London', country='United Kingdom', latitude=51.4700, longitude=-0.4543)
        Airport.objects.create(code='LCY', name='London City Airport', city='London', country='United Kingdom', latitude=51.5052, longitude=0.0553)


    def test_home_view_get(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIn('data', response.context)
        self.assertEqual(len(response.context['data']), 2)
        self.assertEqual(response.context['data'][0]['name'].strip(), 'Heathrow')
        self.assertEqual(response.context['data'][1]['name'].strip(), 'London City')
        

class FlightListViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.origin_airport = Airport.objects.create(code='LHR', name='Heathrow Airport', city='London', country='United Kingdom', latitude=51.4700, longitude=-0.4543)
        self.destination_airport = Airport.objects.create(code='LGW', name='Gatwick Airport', city='London', country='United Kingdom', latitude=51.5052, longitude=0.0553)
        
        self.route = Route.objects.create(origin_airport=self.origin_airport, destination_airport=self.destination_airport, distance=50)
        self.aircraft = Aircraft.objects.create(aircraft_unique_id='AC1-2024-UK01', model='Boeing 747', manufacturer='Boeing', capacity=200, usage_capacity=180, year_of_manufacture='2020-01-01', last_maintenance_date='2024-01-01')
        self.flight = Flight.objects.create(flight_number='BA123', route=self.route, aircraft=self.aircraft, departure_time='2024-06-01 10:00:00', arrival_time='2024-06-01 11:00:00', flight_status='On Time', basic_rate=100.00)

    def test_flight_list_view_get(self):
        response = self.client.get(reverse('flight_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'flight_list.html')
        self.assertIn('flights', response.context)
        self.assertEqual(len(response.context['flights']), 1)

    def test_flight_list_view_with_query_params(self):
        response = self.client.get(reverse('flight_list'), {'origin': 'LHR', 'destination': 'LGW', 'flight_date': '2024-06-01'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'flight_list.html')
        self.assertIn('flights', response.context)
        self.assertEqual(len(response.context['flights']), 1)


class FlightDetailViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.origin_airport = Airport.objects.create(code='LHR', name='Heathrow Airport', city='London', country='UK', latitude=51.4700, longitude=-0.4543)
        self.destination_airport = Airport.objects.create(code='LGW', name='Gatwick Airport', city='London', country='UK', latitude=51.1537, longitude=-0.1821)
        self.route = Route.objects.create(origin_airport=self.origin_airport, destination_airport=self.destination_airport, distance=50)
        self.aircraft = Aircraft.objects.create(
            aircraft_unique_id='AC1-2024-UK01',
            model='Boeing 747',
            manufacturer='Boeing',
            capacity=200,
            usage_capacity=180,
            year_of_manufacture='2020-01-01',
            last_maintenance_date='2024-01-01'
        )
        departure_time = timezone.make_aware(datetime(2024, 6, 1, 10, 0, 0))
        arrival_time = timezone.make_aware(datetime(2024, 6, 1, 11, 0, 0))
        self.flight = Flight.objects.create(
            flight_number='BA123',
            route=self.route,
            aircraft=self.aircraft,
            departure_time=departure_time,
            arrival_time=arrival_time,
            flight_status='On Time',
            basic_rate=100.00,
            origin_terminal='Terminal 1',
            destination_terminal='Terminal 2'
        )

    def test_flight_detail_view_get(self):
        response = self.client.get(reverse('flight_detail', args=[self.flight.flight_number]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'flight-detail.html')
        self.assertIn('flight', response.context)
        self.assertEqual(response.context['flight'], self.flight)
        self.assertEqual(response.context['flight'].departure_time, timezone.make_aware(datetime(2024, 6, 1, 10, 0, 0)))
        self.assertEqual(response.context['flight'].arrival_time, timezone.make_aware(datetime(2024, 6, 1, 11, 0, 0)))
        self.assertEqual(response.context['flight'].flight_status, 'On Time')
        self.assertEqual(response.context['flight'].basic_rate, 100.00)
        self.assertEqual(response.context['flight'].origin_terminal, 'Terminal 1')
        self.assertEqual(response.context['flight'].destination_terminal, 'Terminal 2')
        
        
from django.test import TestCase, Client
from django.urls import reverse
from flight.models import Aircraft, Flight, Seat, Route, Airport
from booking.models import CustomUser
from datetime import datetime
from django.utils import timezone

class SeatSelectionViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            username='testuser', 
            email='testuser@example.com', 
            password='password', 
            first_name='Test', 
            last_name='User'
        )
        self.origin_airport = Airport.objects.create(code='LHR', name='Heathrow Airport', city='London', country='UK', latitude=51.4700, longitude=-0.4543)
        self.destination_airport = Airport.objects.create(code='LGW', name='Gatwick Airport', city='London', country='UK', latitude=51.1537, longitude=-0.1821)
        self.route = Route.objects.create(origin_airport=self.origin_airport, destination_airport=self.destination_airport, distance=50)
        self.aircraft = Aircraft.objects.create(
            aircraft_unique_id='AC1-2024-UK01', 
            model='Boeing 747', 
            manufacturer='Boeing', 
            capacity=200, 
            usage_capacity=180, 
            year_of_manufacture='2020-01-01', 
            last_maintenance_date='2024-01-01'
        )
        departure_time = timezone.make_aware(datetime(2024, 6, 1, 10, 0, 0), timezone.get_current_timezone())
        arrival_time = timezone.make_aware(datetime(2024, 6, 1, 11, 0, 0), timezone.get_current_timezone())
        self.flight = Flight.objects.create(
            flight_number='BA123', 
            route=self.route, 
            aircraft=self.aircraft, 
            departure_time=departure_time, 
            arrival_time=arrival_time, 
            flight_status='On Time', 
            basic_rate=100.00,
            origin_terminal='Terminal 1',
            destination_terminal='Terminal 2'
        )
        Seat.objects.create(
            seat_number='1A', 
            aircraft=self.aircraft, 
            class_type='First Class', 
            is_window_seat=True, 
            is_aisle_seat=False, 
            is_emergency_exit=False, 
            seat_ranking='A', 
            description='First class window seat'
        )
        Seat.objects.create(
            seat_number='1B', 
            aircraft=self.aircraft, 
            class_type='First Class', 
            is_window_seat=False, 
            is_aisle_seat=True, 
            is_emergency_exit=False, 
            seat_ranking='B', 
            description='First class aisle seat'
        )
        Seat.objects.create(
            seat_number='2A', 
            aircraft=self.aircraft, 
            class_type='Economy Class', 
            is_window_seat=True, 
            is_aisle_seat=False, 
            is_emergency_exit=False, 
            seat_ranking='C', 
            description='Economy class window seat'
        )
        Seat.objects.create(
            seat_number='2B', 
            aircraft=self.aircraft, 
            class_type='Economy Class', 
            is_window_seat=False, 
            is_aisle_seat=True, 
            is_emergency_exit=False, 
            seat_ranking='D', 
            description='Economy class aisle seat'
        )

    def test_seat_selection_view_get(self):
        self.client.login(username='testuser', password='password')
        session = self.client.session
        session['selected_flight'] = {
            "aircraft_unique_id": 'AC1-2024-UK01',
            "flight_number": 'BA123'
        }
        session.save()

        response = self.client.get(reverse('seat_selection'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'aircraft1-seat.html')
        self.assertIn('reserved_seats', response.context)
        self.assertIn('first_class_seats', response.context)
        self.assertIn('economy_class_seats', response.context)
        self.assertEqual(len(response.context['first_class_seats']), 2)
        self.assertEqual(len(response.context['economy_class_seats']), 2)

class SeatSelectionViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            email='testuser@example.com', 
            password='password', 
            first_name='Test', 
            last_name='User'
        )
        self.origin_airport = Airport.objects.create(code='LHR', name='Heathrow Airport', city='London', country='UK', latitude=51.4700, longitude=-0.4543)
        self.destination_airport = Airport.objects.create(code='LGW', name='Gatwick Airport', city='London', country='UK', latitude=51.1537, longitude=-0.1821)
        self.route = Route.objects.create(origin_airport=self.origin_airport, destination_airport=self.destination_airport, distance=50)
        self.aircraft = Aircraft.objects.create(
            aircraft_unique_id='AC1-2024-UK01', 
            model='Boeing 747', 
            manufacturer='Boeing', 
            capacity=200, 
            usage_capacity=180, 
            year_of_manufacture='2020-01-01', 
            last_maintenance_date='2024-01-01'
        )
        departure_time = timezone.make_aware(datetime(2024, 6, 1, 10, 0, 0), timezone.get_current_timezone())
        arrival_time = timezone.make_aware(datetime(2024, 6, 1, 11, 0, 0), timezone.get_current_timezone())
        self.flight = Flight.objects.create(
            flight_number='BA123', 
            route=self.route, 
            aircraft=self.aircraft, 
            departure_time=departure_time, 
            arrival_time=arrival_time, 
            flight_status='On Time', 
            basic_rate=100.00,
            origin_terminal='Terminal 1',
            destination_terminal='Terminal 2'
        )
        Seat.objects.create(
            seat_number='1A', 
            aircraft=self.aircraft, 
            class_type='First Class', 
            is_window_seat=True, 
            is_aisle_seat=False, 
            is_emergency_exit=False, 
            seat_ranking='A', 
            description='First class window seat'
        )
        Seat.objects.create(
            seat_number='1B', 
            aircraft=self.aircraft, 
            class_type='First Class', 
            is_window_seat=False, 
            is_aisle_seat=True, 
            is_emergency_exit=False, 
            seat_ranking='B', 
            description='First class aisle seat'
        )
        Seat.objects.create(
            seat_number='2A', 
            aircraft=self.aircraft, 
            class_type='Economy Class', 
            is_window_seat=True, 
            is_aisle_seat=False, 
            is_emergency_exit=False, 
            seat_ranking='C', 
            description='Economy class window seat'
        )
        Seat.objects.create(
            seat_number='2B', 
            aircraft=self.aircraft, 
            class_type='Economy Class', 
            is_window_seat=False, 
            is_aisle_seat=True, 
            is_emergency_exit=False, 
            seat_ranking='D', 
            description='Economy class aisle seat'
        )

    def test_seat_selection_view_get(self):
        self.client.login(email='testuser@example.com', password='password')
        session = self.client.session
        session['selected_flight'] = {
            "aircraft_unique_id": 'AC1-2024-UK01',
            "flight_number": 'BA123'
        }
        session.save()

        response = self.client.get(reverse('seat_selection'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'aircraft1-seat.html')
        self.assertIn('reserved_seats', response.context)
        self.assertIn('first_class_seats', response.context)
        self.assertIn('economy_class_seats', response.context)
        self.assertEqual(len(response.context['first_class_seats']), 2)
        self.assertEqual(len(response.context['economy_class_seats']), 2)
