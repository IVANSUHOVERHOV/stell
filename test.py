import unittest
from dz8 import *

class My_test(unittest.TestCase):

    def test_fun(self):
        self.assertEqual(fun(2, 2), 4)


if __name__ == '__main__':
    unittest.main()