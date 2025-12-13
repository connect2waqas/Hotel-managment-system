import json
import os

def processing():
    return f"Processing..."

def fetch_data():
    file_path = "user_data.json"

    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            if isinstance(data, dict):
                return [data]
            return data
    except json.JSONDecodeError:
        return []

def save_user_data():
    full_name = input("Enter your name: ").lower().strip()
    occupation = input("Enter your occupation: ").lower().strip()

    while True:
        try:
            age = int(input("Enter age: "))
            ID = int(input("Enter your ID: "))
            break
        except ValueError:
            print("Please enter valid numbers for age and ID.")

    users = fetch_data()
    user_found = False

    # 🔄 Update if ID exists
    for user in users:
        if user["ID"] == ID:
            user["full_name"] = full_name
            user["occupation"] = occupation
            user["age"] = age
            user_found = True
            print("🔄 User already present. Data updated.")
            break

    # ➕ Insert if ID not found
    if not user_found:
        users.append({
            "full_name": full_name,
            "ID": ID,
            "age": age,
            "occupation": occupation
        })
        print("➕ New user added.")

    # 💾 Save back to JSON
    with open("user_data.json", "w") as f:
        json.dump(users, f, indent=4)

    return 

def delete_customer_data():
    users = fetch_data()
    ID = int(input("Enter user ID to delete: "))

    updated_users = [user for user in users if user["ID"] != ID]

    if len(users) == len(updated_users):
        print("❌ No user found with this ID.")
    else:
        with open("user_data.json", "w") as f:
            json.dump(updated_users, f, indent=4)
        print("✅ User deleted successfully.")

def search_customer():
    ID = int(input("Enter ID of customer: "))
    users = fetch_data()
    customer_found = False
    for user in users:
        if user["ID"] == ID:
            print(user["ID"],user["full_name"],user["age"],user["occupation"])
            customer_found = True
            break
    if not customer_found:
        print("ID Not found")
