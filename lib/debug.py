from lib.helpers import add_location, exit_program, view_locations
from lib.models import Base, engine
from lib.models.location import Location

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Database and tables created.")

def main():
    while True:
        print("Please select an option:")
        print("0. Exit the program")
        print("1. Add a location")
        print("2. View locations")
        print("3 Delete location")
        choice = input("> ")
        print(f"User selected: {choice}")

        if choice == "0":
            exit_program()
            break
        elif choice == "1":
            add_location()
        elif choice == "2":
            view_locations()
        else:
            print("Invalid choice. Please try again.")
