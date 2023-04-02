"""
Exceptions for the auth module.
"""

class AuthException(Exception):
    """
    Base class for auth exceptions.
    """
    def __init__(self, username, user=None):
        super().__init__(username, user)
        self.username = username
        self.user = user

class UsernameAlreadyExists(AuthException):
    """
    Raised when attempting to create an account with an existing username.
    """
    ...

class PasswordTooShort(AuthException):
    """
    Raised when attempting to create an account with a password that is too short.
    """
    ...

class InvalidUsername(AuthException):
    """
    Raised when attempting to login with an invalid username.
    """
    ...

class InvalidPassword(AuthException):
    """
    Raised when attempting to login with an invalid password.
    """
    ...

class NotLoggedInError(AuthException):
    """
    Raised when attempting to perform a function that requires being logged in.
    """
    ...

class NotPermittedError(AuthException):
    """
    Raised when attempting to perform a function that the user is not allowed to perform.
    """
    ...
