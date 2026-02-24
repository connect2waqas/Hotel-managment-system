from Room_booking import  Greet_To_room, Room_confirmation
import payments
import customer_management
from Food_menu import menu

# Main booking flow - handles room booking and payment processing
# Collects customer data and confirms when payment threshold is met
def booking():
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

# Handles customer check-in process
# Updates customer information and gives option to delete data after check-in
def checking():
    print("Check-in module opened...")
    print(customer_management.processing())
    userData = customer_management.save_user_data()
    delete_data = input("Did you want to delete your data: ").lower()
    if delete_data == "yes":
         customer_management.delete_customer_data()
    else:
        print("Thank You")
        print("Profile Update Successfully...")

    return 1

# Opens the food ordering menu for customers
# Processes customer data before showing menu options
def food():
    print("Food menu is opend...")
    print(customer_management.processing())
    userData = customer_management.save_user_data()
    return menu()