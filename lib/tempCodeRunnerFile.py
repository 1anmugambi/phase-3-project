import tkinter as tk

import tkinter as tk
from tkinter import messagebox
from lib.helpers import add_location, view_locations
from lib.models import session, Location

# Function to add a location
def ui_add_location():
    def submit():
        name = entry_name.get()
        latitude = entry_latitude.get()
        longitude = entry_longitude.get()
        if name and latitude and longitude:
            try:
                latitude = float(latitude)
                longitude = float(longitude)
                location = Location(name=name, latitude=latitude, longitude=longitude)
                session.add(location)
                session.commit()
                messagebox.showinfo("Success", f"Location '{name}' added successfully.")
                add_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Latitude and Longitude must be numbers.")
        else:
            messagebox.showerror("Error", "All fields are required.")

    add_window = tk.Toplevel(root)
    add_window.title("Add Location")

    tk.Label(add_window, text="Location Name:").grid(row=0, column=0, padx=10, pady=10)
    entry_name = tk.Entry(add_window)
    entry_name.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(add_window, text="Latitude:").grid(row=1, column=0, padx=10, pady=10)
    entry_latitude = tk.Entry(add_window)
    entry_latitude.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(add_window, text="Longitude:").grid(row=2, column=0, padx=10, pady=10)
    entry_longitude = tk.Entry(add_window)
    entry_longitude.grid(row=2, column=1, padx=10, pady=10)

    submit_button = tk.Button(add_window, text="Add Location", command=submit)
    submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Function to view all locations
def ui_view_locations():
    view_window = tk.Toplevel(root)
    view_window.title("View Locations")

    locations = session.query(Location).all()
    if locations:
        for loc in locations:
            tk.Label(view_window, text=f"{loc.id}: {loc.name} (Lat: {loc.latitude}, Long: {loc.longitude})").pack(padx=10, pady=5)
    else:
        tk.Label(view_window, text="No locations found.").pack(padx=10, pady=10)

# Main window
root = tk.Tk()
root.title("Survey Studio CLI Application")

main_frame = tk.Frame(root)
main_frame.pack(padx=20, pady=20)

tk.Label(main_frame, text="Survey Studio CLI Application", font=("Helvetica", 16)).pack(pady=10)

add_button = tk.Button(main_frame, text="Add Location", command=ui_add_location)
add_button.pack(pady=5)

view_button = tk.Button(main_frame, text="View Locations", command=ui_view_locations)
view_button.pack(pady=5)

exit_button = tk.Button(main_frame, text="Exit", command=root.quit)
exit_button.pack(pady=20)

# Start the main loop
root.mainloop()

