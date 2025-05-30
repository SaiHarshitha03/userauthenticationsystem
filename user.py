import sqlite3
import bcrypt

# Connect to SQLite database (creates file if not exists)
con = sqlite3.connect("users.db")
cur = con.cursor()

# Create users table if it doesn't exist
cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT UNIQUE, password BLOB)")
con.commit()

def register():
    while True:
        u = input("Username: ").strip()
        if not u:
            print("Username cannot be empty.")
            continue
        # Check if username exists
        cur.execute("SELECT * FROM users WHERE username=?", (u,))
        if cur.fetchone():
            print("Username already taken. Try another.")
            continue
        break

    while True:
        p = input("Password: ")
        if len(p) < 6:
            print("Password should be at least 6 characters.")
        else:
            break

    # Hash password
    p_bytes = p.encode('utf-8')
    hashed = bcrypt.hashpw(p_bytes, bcrypt.gensalt())

    # Insert into DB
    cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (u, hashed))
    con.commit()
    print("Registered successfully!")

def login():
    u = input("Username: ").strip()
    p = input("Password: ").strip()

    cur.execute("SELECT password FROM users WHERE username=?", (u,))
    record = cur.fetchone()

    if record:
        stored_hash = record[0]
        # bcrypt needs bytes, stored_hash is bytes from DB
        if bcrypt.checkpw(p.encode('utf-8'), stored_hash):
            print("Login success!")
            return
    print("Login failed. Invalid username or password.")

def main():
    while True:
        print("\n1. Register  2. Login  3. Exit")
        choice = input("Choice: ").strip()
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

