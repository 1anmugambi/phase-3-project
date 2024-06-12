# lib/cli.py

from helpers import exit_program, add_location, view_locations


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_location()
        elif choice == "2":
            view_locations()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add a location")
    print("2. View all locations")


if __name__ == "__main__":
    main()
