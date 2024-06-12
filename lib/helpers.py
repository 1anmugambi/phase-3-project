from lib.models import session, Location

# Function to add a new location to the database
def add_location():
    # Prompt the user for location details
    name = input("Enter location name: ")
    latitude = float(input("Enter latitude: "))
    longitude = float(input("Enter longitude: "))

    # Create a new Location instance
    location = Location(name=name, latitude=latitude, longitude=longitude)

    # Add the new location to the session and commit to the database
    session.add(location)
    session.commit()

    # Confirmation message
    print(f"Location '{name}' added successfully.")

# Function to view all locations in the database
def view_locations():
    # Query all locations from the database
    locations = session.query(Location).all()

    # Print each location
    if locations:
        for loc in locations:
            print(f"{loc.id}: {loc.name} (Lat: {loc.latitude}, Long: {loc.longitude})")
    else:
        # Message if no locations are found
        print("No locations found.")

# Function to exit the program
def exit_program():
    print("Goodbye!")
    exit()
