from unittest.mock import patch

# Dictionary to store user accounts
user_accounts = {}

def create_user_account():
    print("=== Create New User Account ===")
    username = input("Enter a username: ").strip()

    if username in user_accounts:
        print("Username already exists. Please try a different one.")
        return

    password = input("Enter a password: ").strip()
    confirm_password = input("Confirm your password: ").strip()

    if password != confirm_password:
        print("Passwords do not match. Try again.")
        return

    user_accounts[username] = password
    print(f"Account created successfully for user: {username}")

# --- Simple test run ---
print("Running simple test...")

with patch('builtins.input', side_effect=['alice', '12345', '12345']):
    create_user_account()

print("\nAccounts now:", user_accounts)


