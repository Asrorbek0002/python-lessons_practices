import unittest
from python_func2 import get_Area,get_Perimeter

class CircleTest(unittest.TestCase):
    def test_Area(self):
        area=get_Area(10)
        self.assertAlmostEqual(area,314.159)


    def test_Perimeter(self):
        Perimeter=get_Perimeter(10)
        self.assertAlmostEqual(Perimeter,62.8318)



