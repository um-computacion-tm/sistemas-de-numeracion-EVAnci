#################
#    Imports    #
#################

import unittest
from decimal_base import decimal_to_binary, decimal_to_octal, decimal_to_hexadecimal
from binary_base import *

#################
#   Testing     #
#################

class Test_base_Change(unittest.TestCase):

    def test_binary_numbers(self):
        output = decimal_to_binary(7)
        self.assertEqual(output, '111')
        output = decimal_to_binary(13)
        self.assertEqual(output, '1101')
        output = decimal_to_binary(20)
        self.assertEqual(output, '10100')
        output = decimal_to_binary(3)
        self.assertEqual(output, '11')

    def test_octal_numbers(self):
        output = decimal_to_octal(7)
        self.assertEqual(output, '7')
        output = decimal_to_octal(12)
        self.assertEqual(output, '14')
        output = decimal_to_octal(23)
        self.assertEqual(output, '27')
        output = decimal_to_octal(70)
        self.assertEqual(output, '106')

    def test_hexadecimal_numbers(self):
        output = decimal_to_hexadecimal(456)
        self.assertEqual(output, '1C8')
        output = decimal_to_hexadecimal(7)
        self.assertEqual(output, '7')
        output = decimal_to_hexadecimal(40)
        self.assertEqual(output, '28')
        output = decimal_to_hexadecimal(737250)
        self.assertEqual(output, 'B3FE2')


if __name__ == '__main__':
    unittest.main()