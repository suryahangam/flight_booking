from typing import Any
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from .models import Flight, Airport, Seat
from booking.models import Booking, Passenger, CustomUser, SeatHold
from django.views.generic import DetailView
from django.http import JsonResponse
from booking.algorithm.main import AdvancedAirplaneSeating


class HomeView(View):
    def get(self, request):
        airports = Airport.objects.values('code', 'name')
        data = []
        
        for a in airports:
            data.append(
            {
                "name": a['name'].replace('Airport', ''),
                "code": a["code"]
            }
            )
            
        context = {
            'data': data
        }
        print(data)
        
        return render(request, 'index.html', context=context)
    
    def post(self, request):
        pass


class FlightListView(ListView):
    model = Flight
    template_name = 'flight_list.html'
    context_object_name = 'flights'
    
    def get_queryset(self):
        query_params = self.request.GET
        print("query_params", query_params)
        if query_params:
            origin = query_params.get('origin')
            destination = query_params.get('destination')
            departure_date = query_params.get('flight_date')
            
            if 'query_params' in self.request.session:
                del self.request.session['query_params']
                
            self.request.session['query_params'] = {
                "origin": origin,
                "destination": destination,
                "departure_date": departure_date,
                "total_travellers": query_params.get('total_travellers')
            }
            
            print("origin", origin)
            print("destination", destination)
            print("departure_date", departure_date)
            return Flight.objects.filter(route__origin_airport__code=origin, 
                                         route__destination_airport__code=destination,
                                         departure_time__date=departure_date).select_related('route').all()
            
        return Flight.objects.select_related('route').all()
    
    def get_context_data(self, **kwargs):
        from datetime import datetime
        
        context = super().get_context_data(**kwargs)
        origin = self.request.GET.get('origin')
        destination = self.request.GET.get('destination')
        
        routes = Airport.objects.filter(code__in=[origin, destination]).values('code', 'name')
        routes_dict = {route['code']: route['name'] for route in routes}

        context['origin'] = routes_dict.get(origin)
        context['destination'] = routes_dict.get(destination)
        context['departure_date'] = datetime.strptime(self.request.GET.get('flight_date'), '%Y-%m-%d').strftime('%a, %d %b')
        return context
    

class FlightDetailView(DetailView):
    model = Flight
    slug_field = 'flight_number' 
    slug_url_kwarg = 'flight_number'
    template_name = 'flight-detail.html'
    context_object_name = 'flight'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        obj = self.get_object()
        
        # Remove the session key if it exists
        if 'selected_flight' in self.request.session:
            del self.request.session['selected_flight']
        
         # Set all flight to session
        self.request.session['selected_flight'] = {
            "aircraft_unique_id": obj.aircraft.aircraft_unique_id,
            "aircraft": obj.aircraft.model,
            "flight_number": obj.flight_number,
            "origin_airport_name": obj.route.origin_airport.name,
            "destination_airport_name": obj.route.destination_airport.name,
            "origin_airport_code": obj.route.origin_airport.code,
            "destination_airport_code": obj.route.destination_airport.code,
            "departure_time": obj.departure_time.strftime('%H:%M'),
            "departure_date": obj.departure_time.strftime('%a, %d %b'),
            "arrival_time": obj.arrival_time.strftime('%H:%M'),
            "arrival_date": obj.arrival_time.strftime('%a, %d %b'),
            "duration": obj.get_duration(),
            "flight_status": obj.flight_status,
            "basic_rate": str(obj.basic_rate),
            "origin_terminal": obj.origin_terminal,
            "destination_terminal": obj.destination_terminal
        }
        return context    


class SeatSelectionView(View):
    # assign, free, occupied, low, high, ''
    def get(self, request):
        # Check if the selected flight is of aircraft type 'AC1-2024-UK01'
        if request.session.get('selected_flight').get("aircraft_unique_id") == 'AC1-2024-UK01':
            flight_number = request.session.get('selected_flight').get('flight_number')
            
            # Get the booking details for the flight
            booking = Booking.objects.filter(
                flight__flight_number=flight_number).first()
            booking_details = booking.bookingdetail_set.all()
            reserved_seats = [booking_detail.seat.seat_number for booking_detail in booking_details]
            
            # Get the haulted seats for the flight
            haulted_seats = list(SeatHold.objects.filter(
                flight__flight_number=flight_number).values_list('seat__seat_number', flat=True))
            
            if haulted_seats:
                reserved_seats.extend(haulted_seats)
                print("reserved_seats", reserved_seats)
                
            # Get all the seats for the aircraft
            seats = Seat.objects.filter(aircraft__aircraft_unique_id='AC1-2024-UK01').all()
                
            context = {
                "reserved_seats": reserved_seats,
                "first_class_seats": [seat for seat in seats if seat.class_type == 'First Class'],
                "business_class_seats": [seat for seat in seats if seat.class_type == 'Business Class'],
                "economy_class_seats": [seat for seat in seats if seat.class_type == 'Economy Class']
            }
            
            return render(request, 'aircraft1-seat.html', context=context) # Should be aircraft2 here
        return render(request, 'aircraft1-seat.html')
    
    def initiate_algorithm(self, request):
        # Get the aircraft unique id from the selected flight
        aircraft_unique_id = request.session.get('selected_flight').get("aircraft_unique_id")
        return AdvancedAirplaneSeating(aircraft_unique_id)
    
    def reserve_seat(self, request, num_seats):
        algorithm = self.initiate_algorithm()
        return algorithm.find_seats(num_seats)
    
    def check_if_seat_is_valid(self, request, seat_number):
        # Get the aircraft unique id from the selected flight
        aircraft_unique_id = request.session.get('selected_flight').get("aircraft_unique_id")
        seat = Seat.objects.filter(aircraft__aircraft_unique_id=aircraft_unique_id, seat_number=seat_number).first()
        
        if seat:
            row = seat.row
            column = seat.column
            
            algorithm = self.initiate_algorithm()
            return algorithm.can_reserve_seat_without_creating_odd(row, column)
    
    def post(self, request):
        pass
    

def select_or_remove_seat(request):
    import json
    
    if request.method == 'POST':
        # Get the selected seat
        data = json.loads(request.body)
        selected_seat = data.get('seat_number')
        flight_number = request.session.get('selected_flight').get('flight_number')
        
        print("selected_seat", selected_seat)
        # Create a new seat hold
        seat = Seat.objects.filter(aircraft__aircraft_unique_id='AC1-2024-UK01', seat_number=selected_seat).first()
        user = request.user
        seat_hold, created = SeatHold.objects.get_or_create(
            user=user,
            flight=Flight.objects.get(flight_number=flight_number),
            seat=seat,
        )
        if not created:
            seat_hold.delete()
            return JsonResponse({'message': 'Seat removed successfully', 'code': 0}, status=200)
        
        return JsonResponse({'message': 'Seat selected successfully', 'code': 1}, status=200)
    
    
def booking_login_redirection(request):
    if not request.session.get("booking_in_progress"):
        request.session["booking_in_progress"] = True
        
    return redirect('login')
    
    
class TravellerDetailView(View):
    def get(self, request):
        if self.request.session.get('query_params'):
            query_params = self.request.session.get('query_params')
            total_travellers = int(query_params.get('total_travellers'))
            print(f'total number of travellers: {total_travellers}', total_travellers)
            travellers = [f"traveller{i+1}" for i in range(total_travellers)]
            return render(request, 'traveller-info.html', context={'travellers': travellers})
            
        return render(request, 'traveller-info.html')
    
    def post(self, request):
        travelers_data = []
        total_travellers = request.session.get('query_params').get('total_travellers')
        for i in range(1, int(total_travellers)+1):
            traveler = {
                'title': request.POST.get(f'title_{i}'),
                'first_name': request.POST.get(f'first_name_{i}'),
                'last_name': request.POST.get(f'last_name_{i}'),
                'dob_date': request.POST.get(f'dob_date_{i}'),
                'dob_month': request.POST.get(f'dob_month_{i}'),
                'dob_year': request.POST.get(f'dob_year_{i}'),
                'passport_number': request.POST.get(f'passport_number_{i}'),
                'nationality': request.POST.get(f'nationality_{i}'),
                'issued_country': request.POST.get(f'issued_country_{i}'),
                'expiry_date': request.POST.get(f'expiry_date_{i}')
            }
            travelers_data.append(traveler)
            
            if 'travelers_data' in request.session:
                del request.session['travelers_data']
                
            request.session['travelers_data'] = travelers_data
            
        print(f'travelers_data: {travelers_data}')
        return redirect('payment')  # Redirect after successful processing


class PaymentView(View):
    def get(self, request):
        return render(request, 'booking-payment.html')
    
    def post(self, request):
        from datetime import datetime
        # Add all booking details to the database
        
        # Create booking/ INSTEAD UPDATE THE BOOKING
        booking = Booking.objects.create(
            # user = request.user,
            user = CustomUser.objects.get(email='admin1@gmail.com'),
            flight=Flight.objects.get(flight_number=request.session.get('selected_flight').get('flight_number')),
            total_cost=0,
            status='SUCCESS',
            num_of_passengers=len(request.session.get('travelers_data'))
        )
        # Add traveller details
        
         # Retrieve the travelers data from session
        travelers_data = request.session.get('travelers_data', [])

        for data in travelers_data:
            
            # Create the Passenger instance
            passenger = Passenger(
                full_name=f"{data['title']} {data['first_name']} {data['last_name']}",
                passport_number=data['passport_number'],
                date_of_birth=f"{data['dob_year']}-{data['dob_month']}-{data['dob_date']}",
                special_needs="",  # Assuming special needs is optional and set later
                frequent_flyer_number=""  # Assuming frequent flyer number is optional and set later
            )
            passenger.save()
            
            # TODO: Add booking detail and assign seating here

        # Clear the session data if no longer needed
        if 'travelers_data' in request.session:
            del request.session['travelers_data']
            
            # Transaction details
            
        booking_id = booking.booking_id  # Assuming booking_id is available
        return redirect('booking_confirmation', booking_id=booking_id)
    

class BookingConfirmationView(View):
    def get(self, request, booking_id):
        context = {
            "booking": Booking.objects.get(booking_id=booking_id)
        }
        return render(request, 'booking-confirmation.html', context=context)
    
    def post(self, request):
        pass