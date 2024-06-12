# lib/helpers.py

from models import Location, session


def add_location():
    name = input("Enter the name of the location: ")
    latitude = float(input("Enter the latitude: "))
    longitude = float(input("Enter the longitude: "))
    location = Location(name=name, latitude=latitude, longitude=longitude)
    session.add(location)
    session.commit()
    print("Location added!")


def view_locations():
    locations = session.query(Location).all()
    for location in locations:
        print(location)


def exit_program():
    print("Goodbye!")
    exit()
