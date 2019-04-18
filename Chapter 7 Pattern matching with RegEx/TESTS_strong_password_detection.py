import unittest
from strong_password_detection import password_validator

class TestsPasswordValidator(unittest.TestCase):

    def test_missing_values(self):
        self.assertFalse(password_validator(""))

    def test_under_min_length(self):
        self.assertFalse(password_validator("1Aa"))

    def test_above_max_length(self):
        self.assertFalse(password_validator("ABCDEabcde1234567890A"))

    def test_only_digits(self):
        self.assertFalse(password_validator("123456789"))

    def test_only_letters(self):
        self.assertFalse(password_validator("ABCDabcd"))

    def test_valid(self):
        self.assertTrue(password_validator("ABCabc12"))

    def test_valid_max_length(self):
        self.assertTrue(password_validator("ABCDEabcde12345%#*()"))

if __name__ == '__main__':
    unittest.main()