import unittest

from python_katas.digital_root.src.DigitalRoot import DigitalRoot


class DigitalRootTest(unittest.TestCase):

    def test_should_return_7_for_17(self):
        self.assertEqual(DigitalRoot.digital_root(16), 7)

    def test_should_return_6_for_456(self):
        self.assertEqual(DigitalRoot.digital_root(456), 6)