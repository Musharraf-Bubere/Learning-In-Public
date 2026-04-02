import sys
from dbhelper import DBhelper

class App:

    def __init__(self):
        self.db = DBhelper()
        self.menu()

    def menu(self):
        while True:
            user_input = input("""
==============================
1. Register
2. Login
3. Exit
==============================
Enter choice: """)

            if user_input == "1":
                self.register()

            elif user_input == "2":
                self.login()

            elif user_input == "3":
                print("👋 Exiting...")
                sys.exit(0)

            else:
                print("❌ Invalid choice")

    def register(self):
        print("\n--- REGISTER ---")

        name = input("Enter name: ").strip()
        email = input("Enter email: ").strip()
        password = input("Enter password: ").strip()

        if not name or not email or not password:
            print("⚠️ All fields are required")
            return

        result = self.db.register(name, email, password)

        if result == 1:
            print("✅ Registration Successful")
        else:
            print("❌ Registration Failed")

    def login(self):
        print("\n--- LOGIN ---")

        email = input("Enter email: ").strip()
        password = input("Enter password: ").strip()

        if not email or not password:
            print("⚠️ All fields are required")
            return

        self.db.login(email, password)


# Run app
if __name__ == "__main__":
    App()