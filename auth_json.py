import json
from pathlib import Path
import os
import secrets
import hashlib
import base64
import hmac
import tempfile

DATA_FILE = Path("users.json")
PBKDF2_ITERS = 150_000

def atomic_write(path: Path, data: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)

def load_users():
    if not DATA_FILE.exists():
        return {}
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))

def save_users(users):
    atomic_write(DATA_FILE, users)

def hash_password(password: str, salt: bytes = None, iterations: int = PBKDF2_ITERS):
    if salt is None:
        salt = secrets.token_bytes(16)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
    return base64.b64encode(salt).decode(), base64.b64encode(dk).decode(), iterations

def register(username, password):
    users = load_users()
    if username in users:
        return False, "username exists"
    salt_b64, hash_b64, iters = hash_password(password)
    users[username] = {"salt": salt_b64, "hash": hash_b64, "iterations": iters}
    save_users(users)
    return True, "registered"

def authenticate(username, password):
    users = load_users()
    if username not in users:
        return False, "username not found"
    rec = users[username]
    salt = base64.b64decode(rec["salt"])
    expected = base64.b64decode(rec["hash"])
    derived = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, rec["iterations"])
    if hmac.compare_digest(expected, derived):
        return True, "authenticated"
    return False, "invalid password"


# def processing():
#     return f"Processing..."


# import os

# def fetch_data():
#     file_path = "user_data.json"

#     if not os.path.exists(file_path):
#         return []
#     try:
#         with open(file_path,"r") as f:
#             data = json.load(f)
#         if isinstance(data,dict):
#             data = [data]
#         return data
#     except json.JSONDecodeError:
#         return []

# def save_user_data():
#     full_name = input("Enter your name: ").strip()
#     occupation = input("Enter your occupation: ").strip()
#     while True:
#         try:
#             age = int(input("Enter age: "))
#             ID = int(input("Enter your ID: "))
#             users = fetch_data()
#             for user in users:
#                 if user["ID"] == ID:
#                     print("User Already Present!")
#                     break
#             break
#         except ValueError:
#             print("Pleas enter a Valid number")
#     new_entry = {
#         "full_name": full_name,
#         "ID": ID,
#         "age": age,
#         "occupation": occupation
#     }

#     # JSON file path
#     file_path = "user_data.json"

#     # If file exists & is not empty -> load it
#     if os.path.exists(file_path):
#         try:
#             with open(file_path, "r") as f:
#                 existing_data = json.load(f)

#             # If data is a dict, convert it into a list
#             if isinstance(existing_data, dict):
#                 existing_data = [existing_data]

#         except json.JSONDecodeError:
#             # If file is corrupted/empty → reset to empty list
#             existing_data = []
#     else:
#         existing_data = []

#     # Append new entry
#     existing_data.append(new_entry)

#     # Save back into JSON
#     with open(file_path, "w") as f:
#         json.dump(existing_data, f, indent=4)

#     # print("Data saved successfully!")
#     return new_entry
