from __future__ import annotations

import csv
import json
from pathlib import Path

import streamlit as st

import Room_booking
import auth_json
import customer_management


APP_DIR = Path(__file__).resolve().parent
DATA_FILE = APP_DIR / "user_data.json"
ORDER_FILE = APP_DIR / "data.csv"

FOOD_MENU = {
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
    "Kashmiri Chai": 150,
}


def ensure_session_state() -> None:
    st.session_state.setdefault("is_authenticated", False)
    st.session_state.setdefault("username", "")
    st.session_state.setdefault("orders", [])
    st.session_state.setdefault("room_total", 0)


def save_customers(users: list[dict]) -> None:
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)


def upsert_customer(full_name: str, occupation: str, age: int, customer_id: int) -> str:
    users = customer_management.fetch_data()
    for user in users:
        if user["ID"] == customer_id:
            user["full_name"] = full_name.lower().strip()
            user["occupation"] = occupation.lower().strip()
            user["age"] = age
            save_customers(users)
            return "User already present. Data updated."
    users.append(
        {
            "full_name": full_name.lower().strip(),
            "ID": customer_id,
            "age": age,
            "occupation": occupation.lower().strip(),
        }
    )
    save_customers(users)
    return "New user added."


def delete_customer(customer_id: int) -> bool:
    users = customer_management.fetch_data()
    updated_users = [user for user in users if user["ID"] != customer_id]
    if len(updated_users) == len(users):
        return False
    save_customers(updated_users)
    return True


def search_customer(customer_id: int) -> dict | None:
    for user in customer_management.fetch_data():
        if user["ID"] == customer_id:
            return user
    return None


def calculate_booking_total(room_index: int, days: int, number_of_rooms: int) -> int:
    rooms = Room_booking.Room_info()
    nightly_price = rooms[room_index]["payment"][0]["Price"]
    return nightly_price * days * number_of_rooms


def calculate_bill(room_total: float, food_total: float) -> dict:
    discount_rate = 0.20
    discounted_room = round(room_total * (1 - discount_rate), 2)
    extra_services = 1000 if room_total > 0 else 0
    final_total = round(discounted_room + extra_services + food_total, 2)
    return {
        "Room total": room_total,
        "Room total after 20% discount": discounted_room,
        "Extra services": extra_services,
        "Food total": food_total,
        "Final bill": final_total,
    }


def append_bill_to_csv(final_bill: float) -> None:
    with ORDER_FILE.open("a", encoding="utf-8", newline="") as file:
        csv.writer(file).writerow([final_bill])


def auth_screen() -> None:
    st.title("🏨 Hotel Management System")
    st.subheader("Register or Login")
    auth_tab1, auth_tab2 = st.tabs(["Login", "Register"])

    with auth_tab1:
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")
        if submitted:
            ok, msg = auth_json.authenticate(username, password)
            if ok:
                st.session_state["is_authenticated"] = True
                st.session_state["username"] = username
                st.success("Login successful.")
                st.rerun()
            else:
                st.error(msg)

    with auth_tab2:
        with st.form("register_form"):
            username = st.text_input("Choose username")
            password = st.text_input("Choose password", type="password")
            submitted = st.form_submit_button("Register")
        if submitted:
            ok, msg = auth_json.register(username, password)
            if ok:
                st.success(msg)
            else:
                st.error(msg)


def booking_section() -> None:
    st.subheader("Room Booking")
    rooms = Room_booking.Room_info()
    labels = [f"{room['type']} — PKR {room['payment'][0]['Price']}/night" for room in rooms]
    selected_label = st.radio("Select room type", labels, horizontal=True)
    selected_index = labels.index(selected_label)
    st.table([rooms[selected_index]])
    with st.form("booking_form"):
        days = st.number_input("Duration (days)", min_value=1, value=1, step=1)
        quantity = st.number_input("Number of rooms", min_value=1, value=1, step=1)
        submitted = st.form_submit_button("Book room")
    if submitted:
        st.session_state["room_total"] = calculate_booking_total(selected_index, int(days), int(quantity))
        st.success("Room(s) booked successfully.")
        st.info(f"Current room total: PKR {st.session_state['room_total']}")


def customer_section() -> None:
    st.subheader("Customer Check-in / Check-out / Management")
    tab1, tab2, tab3, tab4 = st.tabs(["Check-in", "Search", "Update", "Delete (Check-out)"])

    with tab1:
        with st.form("checkin_form"):
            name = st.text_input("Full name")
            occupation = st.text_input("Occupation")
            age = st.number_input("Age", min_value=1, max_value=120, value=18, step=1)
            customer_id = st.number_input("Customer ID", min_value=1, value=1, step=1)
            submitted = st.form_submit_button("Save customer")
        if submitted:
            msg = upsert_customer(name, occupation, int(age), int(customer_id))
            st.success(msg)

    with tab2:
        customer_id = st.number_input("Customer ID to search", min_value=1, value=1, step=1, key="search_id")
        if st.button("Search customer"):
            customer = search_customer(int(customer_id))
            if customer:
                st.table([customer])
            else:
                st.warning("ID Not found")

    with tab3:
        with st.form("update_form"):
            customer_id = st.number_input("Customer ID to update", min_value=1, value=1, step=1)
            name = st.text_input("Updated full name")
            occupation = st.text_input("Updated occupation")
            age = st.number_input("Updated age", min_value=1, max_value=120, value=18, step=1)
            submitted = st.form_submit_button("Update customer")
        if submitted:
            msg = upsert_customer(name, occupation, int(age), int(customer_id))
            st.success(msg)

    with tab4:
        customer_id = st.number_input("Customer ID to delete", min_value=1, value=1, step=1, key="delete_id")
        if st.button("Delete customer"):
            if delete_customer(int(customer_id)):
                st.success("User deleted successfully.")
            else:
                st.warning("No user found with this ID.")

    users = customer_management.fetch_data()
    st.markdown("#### All customers")
    if users:
        st.table(users)
    else:
        st.info("No customer records available.")


def food_section() -> None:
    st.subheader("Food Ordering")
    st.table([{"Item": item, "Price (PKR)": price} for item, price in FOOD_MENU.items()])
    item = st.selectbox("Select item", list(FOOD_MENU.keys()))
    quantity = st.number_input("Quantity", min_value=1, value=1, step=1)
    if st.button("Add order"):
        order_total = FOOD_MENU[item] * int(quantity)
        st.session_state["orders"].append({"Item": item, "Quantity": int(quantity), "Total (PKR)": order_total})
        st.success(f"Added {item}. Order total: PKR {order_total}")

    if st.session_state["orders"]:
        st.markdown("#### Current orders")
        st.table(st.session_state["orders"])
        food_total = sum(order["Total (PKR)"] for order in st.session_state["orders"])
        st.info(f"Food running total: PKR {food_total}")


def payment_section() -> None:
    st.subheader("Payment Processing & Bill")
    room_total = float(st.session_state["room_total"])
    food_total = float(sum(order["Total (PKR)"] for order in st.session_state["orders"]))
    bill = calculate_bill(room_total, food_total)
    st.table([bill])
    if st.button("Finalize payment"):
        append_bill_to_csv(bill["Final bill"])
        st.success("Payment processed and bill saved.")


def dashboard() -> None:
    st.title(f"Dashboard — Welcome {st.session_state['username']}")
    st.sidebar.header("Navigation")
    section = st.sidebar.radio(
        "Select operation",
        [
            "Room Booking",
            "Customer Management",
            "Food Ordering",
            "Payments",
        ],
    )
    if st.sidebar.button("Logout"):
        st.session_state["is_authenticated"] = False
        st.session_state["username"] = ""
        st.session_state["orders"] = []
        st.session_state["room_total"] = 0
        st.rerun()

    if section == "Room Booking":
        booking_section()
    elif section == "Customer Management":
        customer_section()
    elif section == "Food Ordering":
        food_section()
    elif section == "Payments":
        payment_section()


def main() -> None:
    st.set_page_config(page_title="Hotel Management System", layout="wide")
    ensure_session_state()
    if st.session_state["is_authenticated"]:
        dashboard()
    else:
        auth_screen()


if __name__ == "__main__":
    main()
