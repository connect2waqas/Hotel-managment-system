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
    choice = Room_selection() - 1      
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