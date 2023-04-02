"""
...
"""

from exceptions import InvalidPassword, InvalidUsername, UsernameAlreadyExists, PasswordTooShort

def auth_account(authenticator, authorizor):
    """
    Create an account, log in, and add permissions.
    """
    while True:
        print("Type 1 to create an account, 2 to log in, 3 to quit")
        choice = input("Choice: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            try:
                authenticator.add_user(username, password)
            except UsernameAlreadyExists as exc:
                print(f"Username {exc.username} already exists")
                continue
            except PasswordTooShort:
                print("Password too short")
                continue

            authorizor.permit_user("read", username)

            print("To get create and edit permissions, enter admin password.")
            admin_password = input("Password: ")
            try:
                if authenticator.login("admin", admin_password):
                    authorizor.permit_user("create", username)
                    authorizor.permit_user("edit", username)

                    print("Account created and permissions granted.")
            except InvalidPassword:
                print("Invalid password for admin.")
                print("You can only read notes.")

            authenticator.login(username, password)
            return username

        elif choice == "2":
            try:
                username = input("Username: ")
                password = input("Password: ")
                authenticator.login(username, password)
            except InvalidPassword as exc:
                print(f"Invalid password for {exc.username}")
            except InvalidUsername as exc:
                print(f"Invalid username {exc.username}")

            return username
        elif choice == "3":
            exit()
