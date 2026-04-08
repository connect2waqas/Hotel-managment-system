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
# Safely writes data to file using atomic operations to prevent corruption
# Creates a temp file first, then replaces the original to avoid data loss
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
# Loads all registered users from the JSON file
# Returns empty dict if file doesn't exist yet
def load_users():
    if not DATA_FILE.exists():
        return {}
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))
# Saves the user dictionary back to the JSON file
def save_users(users):
    atomic_write(DATA_FILE, users)
# Creates a secure hash of the password using the PBKDF2 algorithm
# Generates a random salt if not provided for extra security
def hash_password(password: str, salt: bytes = None, iterations: int = PBKDF2_ITERS):
    if salt is None:
        salt = secrets.token_bytes(16)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
    return base64.b64encode(salt).decode(), base64.b64encode(dk).decode(), iterations
# Registers a new user with a hashed password
# Returns False if username already exists, True if successful
def register(username, password):
    users = load_users()
    if username in users:
        return False, "username exists."
    salt_b64, hash_b64, iters = hash_password(password)
    users[username] = {"salt": salt_b64, "hash": hash_b64, "iterations": iters}
    save_users(users)
    return True, "registered."

# Verifies user credentials during login
# Uses secure comparison to prevent timing attacks
def authenticate(username, password):
    users = load_users()
    if username not in users:
        return False, "username not found."
    rec = users[username]
    salt = base64.b64decode(rec["salt"])
    expected = base64.b64decode(rec["hash"])
    derived = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, rec["iterations"])
    if hmac.compare_digest(expected, derived):
        return True, "authenticated."
    return False, "Invalid Password."
