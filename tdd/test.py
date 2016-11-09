import unittest
import mock
from calc import Calculator


class TestExample(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def should_return_correct_result(self):
        result = self.calc.add(1, 2)
        self.assertEqual(3, result)
