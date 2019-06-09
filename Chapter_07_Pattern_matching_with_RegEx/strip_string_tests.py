import unittest
from strip_string import strip

#TODO find a way to write tests for functions with input()


class TestsStrip(unittest.TestCase):

    def test_both_sides(self):
        self.assertEqual(strip("_text_", "_"), "text")

    def test_only_right(self):
        self.assertEqual(strip(" text_", "_"), " text")

    def test_only_left(self):
        self.assertEqual(strip("_text ", "_"), "text ")

    def test_neither(self):
        self.assertEqual(strip(" _text_ ", "_"), " _text_ ")

    def test_middle_char(self):
        self.assertEqual(strip("_te_xt_", "_"), "te_xt")

    def test_several_char(self):
        self.assertEqual(strip("____text_", "_"), "text")
        
    def test_space_symbol(self):
        self.assertEqual(strip(" text ", " "), "text")


if __name__ == '__main__':
    unittest.main()