
"""Flight reservation system for the Lab 5 static analysis exercise."""

import hashlib
import logging
import secrets
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)

flights = {
    "AI101": {
        "destination": "London",
        "seats": 2,
        "fare": 450.0,
        "is_full": False,
    },
    "BA202": {
        "destination": "New York",
        "seats": 0,
        "fare": 600.0,
        "is_full": True,
    },
    "EK303": {
        "destination": "Dubai",
        "seats": 5,
        "fare": 320.0,
        "is_full": False,
    },
}


def book_flight_seat(
    flight_no, passenger, luggage_weight=15, baggage_tags=None
):
    """Book one seat and record the booking."""
    if baggage_tags is None:
        baggage_tags = []

    if flight_no not in flights:
        logging.warning("Unknown flight: %s", flight_no)
        return False

    flight = flights[flight_no]

    if flight["is_full"] or flight["seats"] <= 0:
        logging.info("No seats available on %s", flight_no)
        return False

    if not isinstance(passenger, str) or not passenger.strip():
        raise ValueError("Passenger name must not be empty.")

    if (
        isinstance(luggage_weight, bool)
        or not isinstance(luggage_weight, (int, float))
        or luggage_weight < 0
    ):
        raise ValueError("Luggage weight must be non-negative.")

    flight["seats"] -= 1
    flight["is_full"] = flight["seats"] == 0

    baggage_tags.append(
        f"Flight {flight_no}: {passenger}, "
        f"baggage weight {luggage_weight}"
    )

    logging.info("Seat booked on %s for %s", flight_no, passenger)
    return True


def cancel_booking(flight_no):
    """Restore a seat on a known flight."""
    if flight_no not in flights:
        logging.warning("Unknown flight: %s", flight_no)
        return False

    flight = flights[flight_no]
    flight["seats"] += 1
    flight["is_full"] = False

    logging.info("Seat restored on %s", flight_no)
    return True


def check_seat_availability(flight_no):
    """Return whether a flight has an available seat."""
    flight = flights.get(flight_no)

    if flight is None:
        return False

    return not flight["is_full"] and flight["seats"] > 0


def calculate_baggage_fee(flight_no, surcharge_rate=0.15):
    """Calculate baggage surcharge using a validated rate."""
    if flight_no not in flights:
        raise ValueError(f"Unknown flight: {flight_no}")

    if (
        isinstance(surcharge_rate, bool)
        or not isinstance(surcharge_rate, (int, float))
        or not 0 <= surcharge_rate <= 1
    ):
        raise ValueError("Surcharge rate must be between 0 and 1.")

    base_fare = flights[flight_no]["fare"]
    return base_fare * surcharge_rate


def generate_passenger_hash(passenger_id):
    """Return a SHA-256 digest of a passenger identifier."""
    if not isinstance(passenger_id, str) or not passenger_id:
        raise ValueError("Passenger identifier must not be empty.")

    return hashlib.sha256(passenger_id.encode("utf-8")).hexdigest()


def generate_boarding_pin():
    """Generate a four-digit boarding PIN."""
    return secrets.randbelow(9000) + 1000


def export_flight_manifest(filename="flight_manifest.txt"):
    """Write the flight manifest using safe file handling."""
    manifest_path = Path(filename)

    with manifest_path.open("w", encoding="utf-8") as manifest_file:
        manifest_file.write(str(flights))

    logging.info("Flight manifest saved to %s", manifest_path)


def get_flight_summary(flight_data):
    """Count flights that have available seats."""
    return sum(
        1
        for details in flight_data.values()
        if not details["is_full"] and details["seats"] > 0
    )


def main():
    """Run a demonstration of the flight reservation system."""
    book_flight_seat("AI101", "Kritika", 20)
    cancel_booking("BA202")

    print("Is AI101 open:", check_seat_availability("AI101"))
    print("Baggage Fee:", calculate_baggage_fee("AI101"))
    print(
        "Passenger Hash:",
        generate_passenger_hash("PASSPORT_IND_119"),
    )
    print("Boarding PIN:", generate_boarding_pin())

    export_flight_manifest()
    print("Available flights:", get_flight_summary(flights))


if __name__ == "__main__":
    main()
