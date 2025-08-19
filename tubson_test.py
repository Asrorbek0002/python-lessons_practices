import unittest
from python_func3 import get_tub_son

class TubsonTest(unittest.TestCase):
    def test_tubson(self):
        tubson=get_tub_son(31)
        self.assertFalse(tubson,False)

if __name__=='main':
    unittest.main()











