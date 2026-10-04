# DG8002 - F26 - Activity 4
# Author Name: Simon Su
# Date: Oct.04.2026

registered_guests = [
    "Alice",
    "Bob"
]

checked_in = []

while len(checked_in) < len(registered_guests):
    name = input("Please enter your name: ")

    is_registered = False
    for guest in registered_guests:
        if guest == name:
            is_registered = True
            break

    if is_registered:
        if name in checked_in:
            print(f"{name}, you have already checked in.")
        else:
            checked_in.append(name)
            print(f"Welcome, {name}! You are now checked in.")
    else:
        print(f"Sorry, {name}, you are not on the registered guest list.")

    print(f"Checked-in guests: {checked_in}")

print("All guests have successfully checked in!")