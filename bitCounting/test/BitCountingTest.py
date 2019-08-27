import unittest

from python_katas.bitCounting.src import BitCounting


class FindTheParityOutlierTest(unittest.TestCase):

    def test_should_count_0_bits_for_0(self):
        self.assertEqual(BitCounting.count_bits(0), 0)

    def test_should_count_1_bits_for_4(self):
        self.assertEqual(BitCounting.count_bits(4), 1)

    def test_should_count_3_bits_for_7(self):
        self.assertEqual(BitCounting.count_bits(7), 3)

    def test_should_count_2_bits_for_9(self):
        self.assertEqual(BitCounting.count_bits(9), 2)

    def test_should_count_2_bits_for_10(self):
        self.assertEqual(BitCounting.count_bits(10), 2)
