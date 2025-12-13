import csv
import Room_booking
def Pyments():
    pyments = 0
    return pyments

def price_calculation():
    balance = Room_booking.DeliverRoom()
    return balance
def discount():
    discount_rate = 0.20
    current_price = price_calculation()
    amount_to_subtract = current_price * discount_rate
    final_price = current_price - amount_to_subtract
    return round(final_price, 2)


def Extra_services():
    other_misc = 1000
    return other_misc + discount()

def final_bill():
    with open("data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        total_bill = Extra_services() + Pyments()
        writer.writerow([total_bill])
    return total_bill

