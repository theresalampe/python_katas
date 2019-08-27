import unittest

from python_katas.isograms.src import Isograms


class IsogramsTest(unittest.TestCase):

    def test_should_return_true_for_isograms(self):
        self.assertEqual(Isograms.is_isogram("Dermatoglyphics"), True)
        self.assertEqual(Isograms.is_isogram("isogram"), True)
        self.assertEqual(Isograms.is_isogram(""), True, "an empty string is a valid isogram")

    def test_should_return_false_for_no_isograms(self):
        self.assertEqual(Isograms.is_isogram("aba"), False, "same chars may not be adjacent")
        self.assertEqual(Isograms.is_isogram("moOse"), False, "same chars may not be same case")
        self.assertEqual(Isograms.is_isogram("isIsogram"), False)
