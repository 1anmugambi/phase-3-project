from lib.models import session, Location

# Function to add a new location to the database
def add_location(name, latitude, longitude):
    location = Location(name=name, latitude=latitude, longitude=longitude)
    session.add(location)
    session.commit()

# Function to view all locations in the database
def view_locations():
    return session.query(Location).all()

# Function to delete a location from the database by ID
def delete_location(location_id):
    location = session.query(Location).get(location_id)
    if location:
        session.delete(location)
        session.commit()
        return True
    else:
        return False

# Function to exit the program
def exit_program():
    print("Goodbye!")
    exit()
