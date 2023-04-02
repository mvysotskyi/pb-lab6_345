# Task 3. Notebook auth system

## Description
In this task you will implement a notebook auth system. The system will be able to register new users, log in existing users, and log out users. The system will also be able to user permissions to restrict access to certain notebook operations.

## Usage/Examples

```
Welcome to the Notebook.
Please login to continue.
Type 1 to create an account, 2 to log in, 3 to quit
Choice: 1
Username: mykola
Password: 123456
To get create and edit permissions, enter admin password.
Password: admin123
Account created and permissions granted.
Welcome mykola!

        Notebook Menu
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Log out

Enter an option: 3
Enter a memo: My first note
Your note has been added.

        Notebook Menu
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Log out

Enter an option: 1
1: 
My first note

        Notebook Menu
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Log out

Enter an option: 5
Thank you for using your notebook today.
Type 1 to create an account, 2 to log in, 3 to quit
Choice: 3
```

## Exceptions

### Register exceptions
```UserAlreadyExistsException```
This exception should be thrown when a user tries to register with a username that is already taken.

```PasswordTooShort```
This exception should be thrown when a user tries to register with a password that is too short.

### Login exceptions
```NotLoggedInError```
This exception should be thrown when a user tries to perform an operation that requires the user to be logged in, but the user is not logged in.

```InvalidUsername```
This exception should be thrown when a user tries to log in with a username that does not exist.

```InvalidPassword```
This exception should be thrown when a user tries to log in with a password that does not match the password for the given username.

### Permission exceptions

```PermissionError```
Single exception for all permission errors.