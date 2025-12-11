# import main
# from pyments import Pyments

def Greet_To_room():
    return f"Welcome to Room Booking:"
# def check_room_aviable():
#     if main.number_Of_register_user != 5:
#         print("Rooms avialable: ")
#         print(5 - main.number_Of_register_user,"rooms avialable")
        
        
    # else:
    #     print("Rooms not aivalable")
def Room_info():
    single_setter = {"number_of_rooms":5,"bed": "1 Bed", "bathroom": "1 bathroom", "type": "Single bed", "payment": [{"Price": 5000}]}
    Double_setter = {"number_of_rooms":5,"bed": "2 Bed", "bathroom": "2 bathroom", "type": "Double beds", "payment": [{"Price": 10000}]}
    Three_setter =  {"number_of_rooms":5,"bed": "2 Bed", "bathroom": "3 bathroom", "type": "Three beds", "payment": [{"Price": 15000}]}
    Family_Halls =  {"number_of_rooms":5,"bed": "2 Bed", "bathroom": "2 bathroom", "type": "5-6 beds", "payment": [{"Price": 10000}]}
    global total_room_info
    total_room_info = [single_setter,Double_setter,Three_setter, Family_Halls]
    return total_room_info
def Room_selection():
    print("What type of room do you want!: ")
    print("""
          1) Single Setter
          2) Double Setter
          3) Three Setter
          4) Family Halls
          """)
    return  int(input("Enter options (1-4): "))
    
def DeliverRoom():
    rooms = Room_info()
    choice = Room_selection() - 1      # Convert 1-4 to 0-3 index
    selected_room = rooms[choice]

    print(selected_room)

    Duration = int(input("For how much time (in days): "))
    number_of_rooms = int(input("How many rooms do you want to book: "))

    nightly_price = selected_room["payment"][0]["Price"]
    final_price = nightly_price * number_of_rooms * Duration

    print("Room(s) booked successfully!")
    # print(f"Total bill: {final_price}")

    return final_price
def Room_confirmation():
    return f"Room booked successfully"
# def DeliverRoom():
#     total_payments_due = 0
#     if Room_selection() == 1:
#         print((Room_info()[0]))
#         Duration = int(input("For how much time: "))
#         number_of_room_book = int(input("How many single rooms you want to book (1-4): "))
#         total_duration_price = 1
#         if number_of_room_book == 1:
#             nightly_price = Room_info()[0]["payment"][0]["Price"]
#             total_duration_price = nightly_price * number_of_room_book * Duration
#             total_payments_due += total_duration_price 
#             print("Your Have Book The Room ")
#             print(f"Total bill is {total_payments_due}")
#         elif number_of_room_book == 2:
#             nightly_price = Room_info()[0]["payment"][0]["Price"]
#             total_duration_price = nightly_price * number_of_room_book * Duration
#             total_payments_due += total_duration_price 
#             print("Your Have Book The Room ")
#             print(f"Total bill is {total_payments_due}")
#         elif number_of_room_book == 3:
#             nightly_price = Room_info()[0]["payment"][0]["Price"]
#             total_duration_price = nightly_price * number_of_room_book * Duration
#             total_payments_due += total_duration_price 
#             print("Your Have Book The Room ")
#             print(f"Total bill is {total_payments_due}")
#         elif number_of_room_book == 4:
#             nightly_price = Room_info()[0]["payment"][0]["Price"]
#             total_duration_price = nightly_price * number_of_room_book * Duration
#             total_payments_due += total_duration_price 
#             print("Your Have Book The Room ")
#             print(f"Total bill is {total_payments_due}")
#         elif number_of_room_book == 5:
#             nightly_price = Room_info()[0]["payment"][0]["Price"]
#             total_duration_price = nightly_price * number_of_room_book * Duration
#             total_payments_due += total_duration_price 
#             print("Your Have Book The Room ")
#             print(f"Total bill is {total_payments_due}")
#         else:
#             print("Enter a valid number ")

#     elif Room_selection() == 2:
#         print(Room_info()[1])
#         Duration = int(input("For How much time: "))
#         number_of_room_book = int(input("How many Double setter Room you want to Book: "))
#         total_duration_price = 1
#         if number_of_room_book == 1:
#             nightly_price = Room_info()[1]["payment"][0]["Price"]
#             total_duration_price = nightly_price * Duration * number_of_room_book
#             total_payments_due += total_duration_price
#             print(f"You Have Book {number_of_room_book} Rooms for Duration of {Duration}.")
#         elif number_of_room_book == 2:
#             nightly_price = Room_info()[1]["payment"][0]["Price"]
#             total_duration_price = nightly_price * Duration * number_of_room_book
#             total_payments_due += total_duration_price
#             print(f"You Have Book {number_of_room_book} Rooms for Duration of {Duration}.")
#         elif number_of_room_book == 3:
#             nightly_price = Room_info()[1]["payment"][0]["Price"]
#             total_duration_price = nightly_price * Duration * number_of_room_book
#             total_payments_due += total_duration_price
#             print(f"You Have Book {number_of_room_book} Rooms for Duration of {Duration}.")
#         elif number_of_room_book == 4:
#             nightly_price = Room_info()[1]["payment"][0]["Price"]
#             total_duration_price = nightly_price * Duration * number_of_room_book
#             total_payments_due += total_duration_price
#             print(f"You Have Book {number_of_room_book} Rooms for Duration of {Duration}.")
#         elif number_of_room_book == 5:
#             nightly_price = Room_info()[1]["payment"][0]["Price"]
#             total_duration_price = nightly_price * Duration * number_of_room_book
#             total_payments_due += total_duration_price
#             print(f"You Have Book {number_of_room_book} Rooms for Duration of {Duration}.")
#         else:
#             print("Enter a valid number.")