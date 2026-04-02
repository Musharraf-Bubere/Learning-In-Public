import mysql.connector
import sys
import bcrypt

class DBhelper:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Musharraf@123",
                database="hit_db_demo"
            )
            self.cursor = self.conn.cursor()
            print("✅ Connected to Database")

        except Exception as e:
            print("❌ DB Error:", e)
            sys.exit(0)

    # ✅ REGISTER USER
    def register(self, name, email, password):
        try:
            # Check if email already exists
            self.cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            if self.cursor.fetchone():
                print("⚠️ Email already exists")
                return -1

            # Hash password
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            query = """
                INSERT INTO users (name, email, password)
                VALUES (%s, %s, %s)
            """

            self.cursor.execute(query, (name, email, hashed_password))
            self.conn.commit()

            return 1

        except Exception as e:
            print("❌ Error:", e)
            return -1

    # ✅ LOGIN USER
    def login(self, email, password):
        try:
            query = "SELECT * FROM users WHERE email = %s"
            self.cursor.execute(query, (email,))
            user = self.cursor.fetchone()

            if user is None:
                print("❌ User not found")
                return

            stored_password = user[3]  # password column

            # Check password
            if bcrypt.checkpw(password.encode('utf-8'), stored_password):
                print(f"✅ Welcome {user[1]} (Login Successful)")
            else:
                print("❌ Incorrect Password")

        except Exception as e:
            print("❌ Error:", e)