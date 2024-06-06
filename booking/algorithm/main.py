from flight.models import Seat


class AdvancedAirplaneSeating:
    def __init__(self, aircraft_id):
        # Fetch seats from the Seat model
        seats = Seat.objects.filter(aircraft__aircraft_unique_id=aircraft_id)

        # Calculate the number of rows and seats per row
        self.rows = max(int(seat.seat_number[:-1]) for seat in seats)
        self.seats_per_row = max(ord(seat.seat_number[-1]) - ord('A') + 1 for seat in seats)

        # Initialize the seating layout
        self.seating = [['O' for _ in range(self.seats_per_row)] for _ in range(self.rows)]

        # Update the seating layout
        for seat in seats:
            # Extract row and column from seat_number
            row = int(seat.seat_number[:-1]) - 1  # Subtract 1 to make it zero-indexed
            column = ord(seat.seat_number[-1]) - ord('A')  # Convert letter to number

            # Check if the seat is within the seating layout
            if 0 <= row < self.rows and 0 <= column < self.seats_per_row:
                # Update the seating layout
                self.seating[row][column] = 'X'  # Mark the seat as occupied

    def find_seats(self, num_seats, preference=None):
        best_fit = None
        for row_index in range(self.rows):
            free_slots = []
            start_seat = 0

            while start_seat < self.seats_per_row:
                while start_seat < self.seats_per_row and self.seating[row_index][start_seat] != 'O':
                    start_seat += 1
                end_seat = start_seat
                while end_seat < self.seats_per_row and self.seating[row_index][end_seat] == 'O':
                    end_seat += 1

                length = end_seat - start_seat
                if length >= num_seats:
                    if preference == 'window' and (start_seat == 0 or end_seat == self.seats_per_row):
                        return (row_index, start_seat)
                    elif preference == 'aisle' and (start_seat == 0 or end_seat == self.seats_per_row or start_seat > 0 or end_seat < self.seats_per_row):
                        return (row_index, start_seat)
                    free_slots.append((start_seat, length))
                start_seat = end_seat + 1

            # Find the best fit for the group to minimize wasted space
            for start, length in free_slots:
                if best_fit is None or abs(length - num_seats) < abs(best_fit[2] - num_seats):
                    best_fit = (row_index, start, length)

        if best_fit and best_fit[2] >= num_seats:
            return (best_fit[0], best_fit[1])
        return None

    def can_reserve_seat_without_creating_odd(self, row, col):
        # Check the left side
        if col > 0 and self.seating[row][col - 1] == 'O':
            if col == 1 or self.seating[row][col - 2] == 'X':
                return False
        
        # Check the right side
        if col < self.seats_per_row - 1 and self.seating[row][col + 1] == 'O':
            if col == self.seats_per_row - 2 or self.seating[row][col + 2] == 'X':
                return False

        return True

    def reserve_seats(self, num_seats, preference=None):
        position = self.find_seats(num_seats, preference)
        if position:
            row, start_index = position
            for i in range(num_seats):
                if not self.can_reserve_seat_without_creating_odd(row, start_index + i):
                    return False  # If reserving the seat creates an odd seat, cancel the reservation
            for i in range(num_seats):
                self.seating[row][start_index + i] = 'X'
            return True
        return False

    def reserve_manual_seat(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.seats_per_row and self.seating[row][col] == 'O':
            if self.can_reserve_seat_without_creating_odd(row, col):
                self.seating[row][col] = 'X'
                return True
        return False
