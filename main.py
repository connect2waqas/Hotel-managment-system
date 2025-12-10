import auth_json
import general
import greet
number_Of_register_user = 0

def main():
    greet.welcome()

    while True:
        cmd = input("Do you want to register, login, or exit? ").strip().lower()

        if cmd == "register":
            u = input("Enter username: ")
            p = input("Enter password: ")
            ok, msg = auth_json.register(u, p)
            print(msg)
            global number_Of_register_user 
            number_Of_register_user +=1
            
            
        elif cmd == "login":
            u = input("Enter username: ")
            p = input("Enter password: ")

            ok, msg = auth_json.authenticate(u, p)
            print(msg)
            
            number_Of_register_user +=1
            
            if ok:
                general.show_dashboard(u)  # <-- CALL GENERAL.PY


        elif cmd == "exit":
            print("Goodbye!")
            
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
