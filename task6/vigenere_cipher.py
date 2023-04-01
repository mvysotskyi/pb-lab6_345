"""
Vigenere Cipher implementation.
"""

class VigenereCipher:
    """
    Vigenere Cipher implementation.
    """
    def __init__(self, keyword: str):
        self.keyword = keyword

    def extend_keyword(self, number):
        """
        Extend keyword length to number.
        """
        repeats = number // len(self.keyword) + 1
        return (self.keyword * repeats)[:number]

    def _code(self, text, combine_func):
        """
        Encode or decode text.
        """
        text = text.replace(" ", "").upper()
        combined = []
        keyword = self.extend_keyword(len(text))
        for p,k in zip(text, keyword):
            combined.append(combine_func(p,k))

        return "".join(combined)

    def encode(self, plaintext):
        """
        Encode plaintext.
        """
        return self._code(plaintext, self.combine_character)

    def decode(self, ciphertext):
        """
        Decode ciphertext.
        """
        return self._code(ciphertext, self.separate_character)

    @staticmethod
    def combine_character(plain, keyword):
        """
        Combine plain and keyword characters.
        """
        plain = plain.upper()
        keyword = keyword.upper()
        plain_num = ord(plain) - ord('A')
        keyword_num = ord(keyword) - ord('A')
        return chr(ord('A') + (plain_num + keyword_num) % 26)

    @staticmethod
    def separate_character(cypher, keyword):
        """
        Separate cypher and keyword characters.
        """
        cypher = cypher.upper()
        keyword = keyword.upper()
        cypher_num = ord(cypher) - ord('A')
        keyword_num = ord(keyword) - ord('A')

        return chr(ord('A') + (cypher_num - keyword_num) % 26)
