"""
A menu-driven command-line notebook.
Uses a Notebook object to store notes.
"""

import sys

from auth_account import auth_account
from auth import Authenticator, Authorizor
from exceptions import NotPermittedError, NotLoggedInError
from notebook import Notebook, Note

class Menu:
    """
    Display a menu and respond to choices when run.
    """
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": (self.show_notes, "read"),
            "2": (self.search_notes, "read"),
            "3": (self.add_note, "create"),
            "4": (self.modify_note, "edit"),
            "5": (self.quit, None)
        }

    def display_menu(self):
        """
        Display the menu of options to the user.
        """
        print("""
        Notebook Menu
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit
        """
        )

    def run(self, user, authorizor):
        """
        Display the menu and respond to choices.
        """
        if user.is_logged_in:
            print(f"Welcome {user.username}!")
        else:
            raise NotLoggedInError(user.username, user)

        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)

            if action:
                if action[1] is None:
                    action[0]()
                try:
                    if authorizor.check_permission(action[1], user.username):
                        action[0]()
                except NotPermittedError:
                    print(f"Permission denied: {action[1]}")
            else:
                print(f"{choice} is not a valid choice")

    def show_notes(self, notes=None):
        """
        Display all notes in the notebook.
        """
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(f"{note.id}: {note.tags}\n{note.memo}")

    def search_notes(self):
        """
        Search all notes in the notebook for a string.
        """
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        """
        Add a note to the notebook.
        """
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added.")

    def modify_note(self):
        """
        Modify a note in the notebook.
        """
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        """
        Quit the program.
        """
        print("Thank you for using your notebook today.")
        sys.exit(0)

if __name__ == "__main__":
    print("Welcome to the Notebook.")
    print("Please login to continue.")

    authenticator = Authenticator()
    authorizor = Authorizor(authenticator)

    authenticator.add_user("admin", "admin123")

    authorizor.add_permission("read")
    authorizor.add_permission("create")
    authorizor.add_permission("edit")

    authorizor.permit_user("read", "admin")
    authorizor.permit_user("create", "admin")
    authorizor.permit_user("edit", "admin")

    username = auth_account(authenticator, authorizor)

    menu = Menu()

    try:
        menu.run(authenticator.users[username], authorizor)
    except NotLoggedInError:
        print("Please log in to continue.")
