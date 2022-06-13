import functools
import unittest


class Tester(unittest.TestCase):
    @staticmethod
    def my_function1(input_array):
        return functools.reduce(lambda accumulator, value: accumulator + value, input_array)

    @staticmethod
    def my_function2(input_array):
        accumulator = 0
        for value in input_array:
            accumulator = accumulator + value
        return accumulator

    @staticmethod
    def my_function3(input_array):
        return sum(input_array)

    # Main test method
    def test(self):
        input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result1 = self.my_function1(input_array)
        result2 = self.my_function2(input_array)
        result3 = self.my_function3(input_array)
        result4 = functools.reduce(lambda accumulator, value: accumulator + value, input_array)
        self.assertEqual(result1, result2)
        self.assertEqual(result2, result3)
        self.assertEqual(result3, result4)
