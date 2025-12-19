from Room_booking import  Greet_To_room, Room_confirmation
import payments
import customer_management
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
            print(Greet_To_room())
            print(customer_management.save_user_data()) 
            total_bill = 0
            current  = payments.final_bill()
            current += total_bill
            if current >= 5000:
                print(Room_confirmation())
                print(f"You have Pay {current}")
                print("Email recived! ")
                delete_data = input("Did you want to delete your data: ").lower()
                if delete_data == "yes":
                    customer_management.delete_customer_data()
                else:
                    print("Thank You")

            else:
                print("Something went wrong!")
            return current
        
        elif choice == "2":
            print("Check-in module opened...")
            print(customer_management.processing())
            userData = customer_management.save_user_data()
            delete_data = input("Did you want to delete your data: ").lower()
            if delete_data == "yes":
                    customer_management.delete_customer_data()
            else:
                print("Thank You")
            print("Profile Update Successfully...")

            break



        # elif choice == 3:

        # add more later…\\\

        else:
            print("Invalid option. Try again.")
