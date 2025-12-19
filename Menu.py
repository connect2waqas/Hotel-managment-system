import control
def show_dashboard(username):
    print(f"\nWelcome, {username}! You are logged in.")

    while True:
        print("""
======== HOTEL MANAGEMENT DASHBOARD ========
1) Room booking
2) Check-in
3) Check-out
4) Payments
5) Customer management
6) Room management
7) Staff management
8) Reports
9) Logout
""")

        choice = input("Select from the Menu: ").strip()

        if choice == "9":
            print("Logged out.")
            break

        elif choice == "1":
             print(control.booking())

        elif choice == "2":
            return control.checking()
        
        # elif choice == 3:

        # add more later…\\\

        else:
            print("Invalid option. Try again.")
