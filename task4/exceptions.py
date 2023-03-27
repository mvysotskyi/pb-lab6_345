"""
Exceptions for Document, Cursor, and Character classes.
"""

class CursorAtBeginningOfDocument(Exception):
    """
    Raised when the cursor is at the beginning of the document.
    """
    def __init__(self, message="Cannot move cursor before beginning of document."):
        super().__init__(message)

class CursorOutOfDocument(Exception):
    """
    Raised when the cursor is at the end of the document.
    """
    def __init__(self, message="Cannot move cursor after end of document."):
        super().__init__(message)

class CharacterLengthError(Exception):
    """
    Raised when a character is not a single character.
    """
    def __init__(self, character, message=""):
        if not message:
            message = f"Character '{character}' is not a single character.Lenght: {len(character)}."
        super().__init__(message) 
