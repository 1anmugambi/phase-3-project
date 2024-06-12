from lib.helpers import add_location, view_locations, exit_program

# Main function that runs the CLI
def main():
    while True:
        # Display the menu and get user input
        menu()
        choice = input("> ")

        # Execute functions based on user input
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_location()
        elif choice == "2":
            view_locations()
        else:
            print("Invalid choice")

# Function to display the menu options
def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add a location")
    print("2. View locations")

# Entry point of the program
if __name__ == "__main__":
    main()
