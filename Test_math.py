# Practice in class

import unittest 
from math import add
from calc import *

class test_math(unittest.TestCase):
    def test_add_pos(self):
        self.assertEqual(add(2,2),4)

if __name__ == "__main__":
    unittest.main()


# coverage run test_name
# coverage report -m
# will use coverage and give back a report to see how covered I am

# coverage html 
# will make a html report in the same directory as the test
