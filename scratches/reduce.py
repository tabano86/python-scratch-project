import functools
import unittest


class Tester(unittest.TestCase):
    def test_aggregate_numbers(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = functools.reduce(lambda a, b: a + b, arr)
        self.assertEqual(55, result)

    def test_combine_words(self):
        arr = ["foo", "bar", "lol", "fizz", "biz"]
        result = functools.reduce(lambda a, b: a + "," + b, arr)
        self.assertEqual("foo,bar,lol,fizz,biz", result)

    def test_product_sum(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = functools.reduce(lambda a, b: a * b, arr)
        self.assertEqual(3628800, result)
