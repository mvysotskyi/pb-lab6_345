"""
Cursor class.
"""

from exceptions import CursorAtBeginningOfDocument

class Cursor:
    """
    Represents the cursor in the document.
    """
    def __init__(self, document):
        if not hasattr(document, "characters"):
            raise TypeError(f"Expected Document instance, got {type(document).__name__}")

        self.document = document
        self.position = 0

    def forward(self):
        """
        Move the cursor forward one character.
        """
        self.position += 1

    def back(self):
        """
        Move the cursor back one character.
        """
        self.position -= 1
        if self.position < 0:
            raise CursorAtBeginningOfDocument

    def home(self):
        """
        Move the cursor to the beginning of the current line.
        """
        while self.document.characters[self.position - 1].character != "\n":
            self.position -= 1
            if self.position == 0:
                # Got to beginning of file before newline
                break

    def end(self):
        """
        Move the cursor to the end of the current line.
        """
        while (self.position < len(self.document.characters) and
               self.document.characters[self.position].character != "\n"):
            self.position += 1
