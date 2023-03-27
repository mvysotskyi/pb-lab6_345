"""
Document class.
"""

from cursor import Cursor
from character import Character

from exceptions import CursorOutOfDocument

class Document:
    """
    Represents a document.
    """
    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ""

    def insert(self, character):
        """
        Insert a character at the cursor's position.
        """
        if not isinstance(character, (Character, str)):
            raise TypeError(f"Expected Character or str, got {type(character).__name__}")

        if not hasattr(character, "character"):
            character = Character(character)

        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        """
        Delete the character after the cursor.
        """
        if self.cursor.position >= len(self.characters):
            raise CursorOutOfDocument

        del self.characters[self.cursor.position]

    def save(self):
        """
        Save the document to a file.
        """
        with open(self.filename, "w", encoding="utf-8") as file:
            file.write("".join(self.characters))

    @property
    def string(self):
        """
        Return the document as a string.
        """
        return "".join(str(c) for c in self.characters)
