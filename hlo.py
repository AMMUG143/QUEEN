
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

    # Save account
    user_accounts[username] = password
    print(f"Account created successfully for user: {username}")

create_user_account()
print("\nCurrent Accounts:", user_accounts)
