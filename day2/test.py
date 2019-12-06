import unittest

import part1


class Part11TestCase(unittest.TestCase):
    def test_example_program(self):
        program = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        expected = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        result = part1.execute_intcode(program)

        self.assertEqual(result, expected)

    def test_small_programs(self):
        self.assertEqual(
            part1.execute_intcode([1, 0, 0, 0, 99]),
            [2, 0, 0, 0, 99]
        )
        self.assertEqual(
            part1.execute_intcode([2, 3, 0, 3, 99]),
            [2, 3, 0, 6, 99]
        )
        self.assertEqual(
            part1.execute_intcode([2, 4, 4, 5, 99, 0]),
            [2, 4, 4, 5, 99, 9801]
        )
        self.assertEqual(
            part1.execute_intcode([1, 1, 1, 4, 99, 5, 6, 0, 99]),
            [30, 1, 1, 4, 2, 5, 6, 0, 99]
        )
