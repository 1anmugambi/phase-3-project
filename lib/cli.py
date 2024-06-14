import sys
import os

# Append the absolute path of the project directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.helpers import add_location, view_locations, exit_program, delete_location

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
            add_location()
        elif choice == "2":
            view_locations()
        elif choice == "3":
            delete_location()    
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
