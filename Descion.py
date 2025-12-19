from Room_booking import  Greet_To_room, Room_confirmation
import payments
import customer_management
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
        