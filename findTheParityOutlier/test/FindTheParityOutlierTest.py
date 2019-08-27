import unittest

from python_katas.findTheParityOutlier.src import FindTheParityOutlier


class FindTheParityOutlierTest(unittest.TestCase):

    def test_should_return_3_as_outlier(self):
        self.assertEqual(FindTheParityOutlier.find_outlier([2, 4, 6, 8, 10, 3]), 3)

    def test_should_return_11_as_outlier(self):
        self.assertEqual(FindTheParityOutlier.find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)

    def test_should_return_160_as_outlier(self):
        self.assertEqual(FindTheParityOutlier.find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)
