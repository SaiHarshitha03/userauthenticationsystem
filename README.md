User Authentication System (Python + SQLite + bcrypt)

Project Description:
This is a simple command-line User Authentication System implemented in Python using SQLite for data storage and bcrypt for secure password hashing. Users can register with a unique username and a password (minimum 6 characters), then log in by verifying their credentials securely.

User Login:
Verifies username exists
Validates password by comparing bcrypt hashes
Provides clear success/failure messages

Data Storage:
Uses SQLite database (users.db)
Automatically creates the database and table if not present

Simple CLI Interface:
Intuitive menu-driven interaction
Input validation for menu choices

Features:
User Registration:
Ensures usernames are unique
Enforces a minimum password length (6 characters)
Passwords are hashed using bcrypt for secure storage (not stored in plain text)

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

Why Use This Project?
Security Best Practices: Learn how to hash passwords properly with bcrypt to avoid storing plain text passwords.
Database Handling: Practice working with SQLite, a popular embedded database.
Python Skills: Improve command-line input handling, control flow, and modular programming.
Foundation for Larger Apps: Use this as a base for building larger Python applications requiring authentication.
Lightweight and Portable: No need for external database servers — runs anywhere Python is installed.
