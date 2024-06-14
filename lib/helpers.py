from lib.models import session, Location

# Function to add a new location to the database
def add_location(name, latitude, longitude):
    new_location = Location(name=name, latitude=latitude, longitude=longitude)
    session.add(new_location)
    session.commit()
    print(f"Added location: {name} ({latitude}, {longitude})")

# Function to view all locations in the database
def view_locations():
    locations = session.query(Location).all()
    if not locations:
        print("No locations found.")
    else:
        print("Locations:")
        for index, location in enumerate(locations, start=1):
            print(f"{index}. {location.name} ({location.latitude}, {location.longitude})")


# Function to delete a location from the database by ID
def delete_location(location_id):
    location = session.query(Location).get(location_id)
    if location:
        session.delete(location)
        session.commit()
        print(f"Location {location.name} deleted successfully.")
        return True
    else:
        print("Location not found.")
        return False

# Function to exit the program
def exit_program():
    print("Goodbye!")
    exit()
