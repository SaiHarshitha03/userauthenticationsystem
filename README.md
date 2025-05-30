User Authentication System (Python + SQLite + bcrypt)

Project Description:
This is a simple command-line User Authentication System implemented in Python using SQLite for data storage and bcrypt for secure password hashing. Users can register with a unique username and a password (minimum 6 characters), then log in by verifying their credentials securely.

Features:
Register new users with unique usernames
Passwords are securely hashed using bcrypt before storage
Login verification by checking hashed passwords
Input validation for username uniqueness and password length
Stores user data locally in an SQLite database (users.db)
Simple text-based menu interface

Requirements:
Python 3.x
bcrypt Python package (install via pip install bcrypt)

File Structure:
auth_system.py — Main Python script containing the authentication logic.
users.db — SQLite database file (auto-created on first run).


Future Enhancements:
Add password reset feature
Implement account lockout after multiple failed attempts
Add email verification
Create a graphical user interface (GUI)
Integrate with web applications or APIs

