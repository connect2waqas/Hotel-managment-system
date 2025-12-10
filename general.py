from Room_booking import  DeliverRoom , Greet_To_room, Room_confirmation
from Check_in import Customer_infomation
from pyments import Pyments

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
            print("Room booking module opened...")
            print(Customer_infomation())
            print(Greet_To_room())
            total_bill = DeliverRoom()
            current  = Pyments()
            current += total_bill
            if current >= 5000:
                print(Room_confirmation())
                print(f"You have Pay {current}")
                print("Email recived! ")
            else:
                print("Something went wrong!")
            return current
        
        elif choice == "2":
            print("Check-in module opened...")

        # add more later…

        else:
            print("Invalid option. Try again.")
