import csv
import Room_booking

# Placeholder for payment processing
# Currently just returns 0 but can be extended later
def Pyments():
    pyments = 0
    return pyments

# Gets the room price from the booking module
# This is the base price before discounts
def price_calculation():
    balance = Room_booking.DeliverRoom()
    return balance

# Applies a 20% discount to the room price
# Returns the discounted amount rounded to 2 decimal places
def discount():
    discount_rate = 0.20
    current_price = price_calculation()
    amount_to_subtract = current_price * discount_rate
    final_price = current_price - amount_to_subtract
    return round(final_price, 2)

# Adds extra services charge (like cleaning, WiFi etc.) to the discounted price
# Fixed 1000 PKR for miscellaneous services
def Extra_services():
    other_misc = 1000
    return other_misc + discount()

# Calculates and saves the final bill amount to CSV
# Combines all charges including room, services, and any additional payments
def final_bill():
    with open("data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        total_bill = Extra_services() + Pyments()
        writer.writerow([total_bill])
    return total_bill

