"""
Character class.
"""

from exceptions import CharacterLengthError

class Character:
    """
    Class representing a character.
    """
    def __init__(self, character, bold=False, italic=False, underline=False):
        if not isinstance(character, str):
            raise TypeError("'character' must be a str.")

        if len(character) != 1:
            raise CharacterLengthError(character)

        if not all(isinstance(x, bool) for x in (bold, italic, underline)):
            raise TypeError("bold, italic, and underline must be bools.")

        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        bold = "*" if self.bold else ""
        italic = "/" if self.italic else ""
        underline = "_" if self.underline else ""
        return bold + italic + underline + self.character
