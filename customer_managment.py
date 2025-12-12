import json
import os

def processing():
    return f"Processing..."

def fetch_data():
    file_path = "user_data.json"

    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path,"r") as f:
            data = json.load(f)
        if isinstance(data,dict):
            data = [data]
        return data
    except json.JSONDecodeError:
        return []

def save_user_data():
    full_name = input("Enter your name: ").strip()
    occupation = input("Enter your occupation: ").strip()
    while True:
        try:
            age = int(input("Enter age: "))
            ID = int(input("Enter your ID: "))
            users = fetch_data()
            for user in users:
                if user["ID"] == ID:
                    print("User Already Present!")
                    break
            break
        except ValueError:
            print("Pleas enter a Valid number")
    new_entry = {
        "full_name": full_name,
        "ID": ID,
        "age": age,
        "occupation": occupation
    }

    # JSON file path
    file_path = "user_data.json"

    # If file exists & is not empty -> load it
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                existing_data = json.load(f)

            # If data is a dict, convert it into a list
            if isinstance(existing_data, dict):
                existing_data = [existing_data]

        except json.JSONDecodeError:
            # If file is corrupted/empty → reset to empty list
            existing_data = []
    else:
        existing_data = []

    # Append new entry
    existing_data.append(new_entry)

    # Save back into JSON
    with open(file_path, "w") as f:
        json.dump(existing_data, f, indent=4)

    # print("Data saved successfully!")
    return new_entry

def delete_customer_data():
    data = fetch_data()
    data = [item for item in data if item.get("name") != "Waqas"]

    with open("user_data.json", "w") as f:
        json.dump(data, f, indent=4)

