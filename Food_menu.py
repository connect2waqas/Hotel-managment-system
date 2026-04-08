import csv
# Displays the food menu and handles customer orders
# Calculates total price and saves orders to CSV file
def menu():
    # Pakistani food items with their prices in PKR
    pakistani_food_prices = {
    "Chicken Biryani": 400,         
    "Beef Nihari": 650,             
    "Chicken Karahi": 500,          
    "Beef Haleem": 410,             
    "Mutton Karahi": 1400,         
    "Chapli Kabab": 250,           
    "Sada Pulao": 300,        
    "Chicken Tikka": 450,          
    "Chicken Qorma": 450,          
    "Gol Gappay": 250,            
    "Seekh Kabab": 100,             
    "Naan": 30,                     
    "Roti": 15,                     
    "Zarda": 400,                   
    "Kashmiri Chai": 150           
}  
    for food , price in pakistani_food_prices.items():
        print(f"{food} :: {price}")
    with open("data.csv",mode="a",newline="") as file:
        writer = csv.writer(file)
    total_1 = 0
    while True:
        choice = input("which you will order or want to exit: ").title()
        if choice.lower() == "exit":
            price("Existing to menu..")
            break
        elif choice in pakistani_food_prices:
            try:
                amount = int(input("Enter quantaty: "))
                item_price = pakistani_food_prices[choice]
                print(f"Excellent choice! {choice} is avialable")
                order_total = amount * item_price
                writer.writerow([choice,amount,order_total])
                total_1 += order_total
                print(f"This order costs: PKR {order_total}")
                print(f"Your running total is: PKR {total_1}")
                print("-" * 40)
            except ValueError:
                print("please enter a valid number of quantaty")
        else:
            print(f"Sorry {choice} is not avialable Yet")
            print("Available items:", ", ".join(pakistani_food_prices.keys()))
