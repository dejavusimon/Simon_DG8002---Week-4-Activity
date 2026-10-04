# DG8002 - F26 - Activity 4
# Author Name: Simon Su
# Date: Oct.04.2026

menu  = {
    "Burger" : 12.00,
    "Pizza" : 15.00,
    "Salad" : 9.00,
    "Fries" : 5.00,
    "Drink" : 3.00
}

order = []

print("MENU")
for item in menu:
    print(f"{item}: ${menu[item]:.2f}")

ordering = True
while ordering:
    choice = input("What would you like to order? (type Done to finish): ")

    if choice == "Done":
        ordering = False
    elif choice in menu:
        order.append(choice)
        print(f"{choice} added to your order.")
    else:
        print(f"Sorry, {choice} is not on the menu.")

print("RECEIPT")
subtotal = 0
for item in order:
    print(f"{item}: ${menu[item]:.2f}")
    subtotal += menu[item]

print(f"Subtotal: ${subtotal:.2f}")