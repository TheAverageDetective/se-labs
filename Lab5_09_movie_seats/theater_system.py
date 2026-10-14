"""Manage movie-theater seat reservations."""

import json
import os
import hashlib

# Global state
shows = {"SHOW-1": {"title": "Interstellar", "seats": 20, "booked": []},
         "SHOW-2": {"title": "Dangal", "seats": 10, "booked": []}}


def reserve_seat(show_id, seat_number, system_logs=None):
    """Reserve a seat for a show and record the result."""
    if system_logs is None:
        system_logs = []
    show = shows[show_id]
    if seat_number in show["booked"]:
        system_logs.append(
            f"Seat {seat_number} already taken for {show_id}"
        )
        return False
    show["booked"].append(seat_number)
    system_logs.append(f"Reserved seat {seat_number} for {show_id}")
    return True


def release_seat(show_id, seat_number):
    """Release a previously reserved seat."""
    try:
        shows[show_id]["booked"].remove(seat_number)
    except (KeyError, ValueError):
        pass


def ticket_code(show_id, seat_number):
    """Generate a short ticket code for a reservation."""
    return hashlib.sha256(
        (show_id + str(seat_number)).encode()
    ).hexdigest()[:8]


def dump_reservations(file_name="seats.json"):
    """Save reservations to a JSON file."""
    with open(file_name, "w", encoding="utf-8") as file_handle:
        json.dump(shows, file_handle)


def load_reservations(file_name="seats.json"):
    """Load reservations from a JSON file."""
    with open(file_name, "r", encoding="utf-8") as file_handle:
        data = file_handle.read()
    shows.clear()
    shows.update(json.loads(data))


def print_seating_summary():
    """Print the number of free and booked seats for each show."""
    for s in shows.items():
        free = shows[s]["seats"] - len(shows[s]["booked"])
        print(
            f'{shows[s]["title"]}: {free} seats free, '
            f'booked = {shows[s]["booked"]}'
        )


def main():
    """Run the reservation system demonstration."""
    reserve_seat("SHOW-1", 5)
    reserve_seat("SHOW-1", 5)
    reserve_seat("SHOW-1", 25)
    reserve_seat("SHOW-2", -1)
    reserve_seat("SHOW-2", "A7")
    release_seat("SHOW-2", 3)
    print("Ticket code:", ticket_code("SHOW-1", 5))
    seat = input("Seat number to book for SHOW-2 (Enter for 4): ") or "4"
    reserve_seat("SHOW-2", seat)
    dump_reservations()
    load_reservations()
    print_seating_summary()
    os.chmod("seats.json", 0o600)


main()
