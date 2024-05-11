import unittest
from para8_4 import *

class My_test(unittest.TestCase):

    def test_args(self):
        self.assertEqual(adder(3,3,2,3), 10)


if __name__ == '__main__':
    unittest.main()