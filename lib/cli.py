# lib/cli.py

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.helpers import add_location, delete_location, view_locations, exit_program

def main():
    while True:
        print("Please select an option:")
        print("0. Exit the program")
        print("1. Add a location")
        print("2. View locations")
        print("3. Delete location")
        choice = input("> ")

        if choice == "0":
            exit_program()
            break
        elif choice == "1":
            name = input("Enter location name: ")
            latitude = float(input("Enter latitude: "))
            longitude = float(input("Enter longitude: "))
            add_location(name, latitude, longitude)
        elif choice == "2":
            view_locations()
        elif choice == "3":
            location_id = int(input("Enter location ID to delete: "))
            if delete_location(location_id):
                print("Location deleted successfully.")
            else:
                print("Location not found.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()