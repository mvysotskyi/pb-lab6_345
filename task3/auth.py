"""
...
"""

import hashlib
from exceptions import (
    UsernameAlreadyExists, PasswordTooShort, InvalidUsername,\
    InvalidPassword, NotLoggedInError, NotPermittedError
)

class User:
    """
    Represents a user of the system.
    """
    def __init__(self, username, password):
        """
        Create a new user object. The password
        will be encrypted before storing.
        """
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False

    def _encrypt_pw(self, password):
        """
        Encrypt the password with the username and return
        the sha digest.
        """
        hash_string = self.username + password
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        """
        Return True if the password is valid for this
        user, false otherwise.
        """
        encrypted = self._encrypt_pw(password)
        return encrypted == self.password


class Authenticator:
    """
    Manages user login and logout.
    """
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        """
        Add a new user to the system.
        """
        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < 6:
            raise PasswordTooShort(username)
        self.users[username] = User(username, password)

    def login(self, username, password):
        """
        Log the user in.
        """
        try:
            user = self.users[username]
        except KeyError as exc:
            raise InvalidUsername(username) from exc

        if not user.check_password(password):
            raise InvalidPassword(username, user)

        user.is_logged_in = True
        return True

    def is_logged_in(self, username):
        """
        Return True if the user is logged in, False otherwise.
        """
        if username in self.users:
            return self.users[username].is_logged_in
        return False

    def logout(self, username):
        """
        Log the user out.
        """
        if username in self.users:
            self.users[username].is_logged_in = False
            return True
        return False

class Authorizor:
    """
    Manages user permissions.
    """
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, perm_name):
        """
        Create a new permission that users
        can be added to.
        """
        try:
            _ = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()
        else:
            raise PermissionError("Permission Exists")

    def permit_user(self, perm_name, username):
        """
        Grant the given permission to the user.
        """
        try:
            perm_set = self.permissions[perm_name]
        except KeyError as exc:
            raise PermissionError("Permission does not exist") from exc
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)

    def check_permission(self, perm_name, username):
        """
        Check whether a user has a specific permission.
        """
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError as exc:
            raise PermissionError("Permission does not exist") from exc
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True
