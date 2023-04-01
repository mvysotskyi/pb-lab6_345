"""
Test Vigenere Cipher class.
"""

import unittest
from vigenere_cipher import VigenereCipher

class TestVigenereCipher(unittest.TestCase):
    """
    Test Vigenere Cipher class.
    """
    def setUp(self) -> None:
        self.cipher = VigenereCipher('TRAIN')

    def test_encode(self):
        """
        Test encode method.
        """
        self.assertEqual(self.cipher.encode('ENCODEDINPYTHON'), 'XECWQXUIVCRKHWA')

    def test_decode(self):
        """
        Test decode method.
        """
        self.assertEqual(self.cipher.decode('XECWQXUIVCRKHWA'), 'ENCODEDINPYTHON')

    def test_encode_spaces(self):
        """
        Test encode method with spaces.
        """
        self.assertEqual(self.cipher.encode('ENCODED IN PYTHON'), 'XECWQXUIVCRKHWA')

    def test_lowercase(self):
        """
        Test encode method with lowercase.
        """
        self.assertEqual(self.cipher.encode('encoded in python'), 'XECWQXUIVCRKHWA')

    def test_combine_character(self):
        """
        Test combine_character function.
        """
        assert VigenereCipher.combine_character("E", "T") == "X"
        assert VigenereCipher.combine_character("N", "R") == "E"

    def test_separate_character(self):
        """
        Test separate_character function.
        """
        assert VigenereCipher.separate_character("X", "T") == "E"

    def test_extend_keyword(self):
        """
        Test extend_keyword method.
        """
        cipher = VigenereCipher("TRAIN")
        extended = cipher.extend_keyword(16)
        assert extended == "TRAINTRAINTRAINT"

if __name__ == '__main__':
    unittest.main(verbosity=2)
