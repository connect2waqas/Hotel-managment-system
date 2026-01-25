import control
def show_dashboard(username):
    print(f"\nWelcome, {username}! You are logged in.")

    while True:
        print("""
======== HOTEL MANAGEMENT DASHBOARD ========
1) Room booking
2) Check-in
3) Check-out
4) order_food
5) Payments
6) Customer management
7) Room management
8) Staff management
9) Logout
10) Reports
""")

        choice = input("Select from the Menu: ").strip()

        if choice == "9":
            print("Logged out.")
            break

        elif choice == "1":
             print(control.booking())

        elif choice == "2":
            return control.checking()
        elif choice == "4":
            control.food()
        
        # elif choice == 3:

        # add more later…\\\

        else:
            print("Invalid option. Try again.")
