#!/usr/bin/env python3
"""
Simple CLI application for user sign‑up and login.

Features
--------
* In‑memory user database (list of dicts)
* Sign‑up with duplicate‑email check
* Login with email + password
* Initial prompt for existing/new user
* Password confirmation during sign‑up
* Data saved to file for persistence
"""

import json
import os

DATA_FILE = "users_data.json"

def load_users():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_users(users):
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

users_data = load_users()

def find_user_by_email(data, email):
    for user in data:
        if user["email"].lower() == email.lower():
            return user
    return None

def signup_user(data):
    print("\n--- Sign‑Up ---")
    while True:
        email = input("Enter your email: ").strip()
        if find_user_by_email(data, email):
            print("⚠️  An account with that email already exists. Try logging in instead.")
        else:
            break

    name = input("Enter your name: ").strip().title()
    age_input = input("Enter your age: ").strip()
    try:
        age = int(age_input)
    except ValueError:
        print("Invalid age. Setting age to 0.")
        age = 0

    while True:
        password = input("Create a password: ").strip()
        confirm = input("Confirm your password: ").strip()
        if password == confirm:
            break
        else:
            print("❌ Passwords do not match. Try again.")

    data.append({"name": name, "email": email, "password": password, "age": age})
    save_users(data)
    print("✅ Account created successfully! You can now log in.\n")

def login_user(data):
    print("\n--- Login ---")
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()

    user = find_user_by_email(data, email)
    if user and user["password"] == password:
        print("\n✅ User authenticated successfully!\n")
        print("User Details:")
        print(f"Name : {user['name']}")
        print(f"Email: {user['email']}")
        print(f"Age  : {user['age']}\n")
    else:
        print("\n❌ Invalid email or password.\n")

def main():
    print("Welcome to the User Portal!")
    while True:
        response = input("\nDo you already have an account? (yes/no/quit): ").strip().lower()
        if response in ["yes", "y"]:
            login_user(users_data)
        elif response in ["no", "n"]:
            signup_user(users_data)
        elif response in ["quit", "q"]:
            print("👋 Goodbye!")
            break
        else:
            print("Please type 'yes', 'no', or 'quit'.")

if __name__ == "__main__":
    main()
