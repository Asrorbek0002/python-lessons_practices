import unittest
from cars import Car

class CarTest(unittest.TestCase):
    """Car clasini tekshirish uchun test"""
    def setUp(self):
        make='GM'
        self.model='Malibu'
        year=2020
        self.price=40000
        self.km=10000
        self.avto1=Car(make,self.model,year)
        self.avto2=Car(make,self.model,year,price=self.price)

    def test_create(self):
        # qiymatni mavjud yoki mavjud emasligini tekshirish assertIsNotNone(x) orqali  there is for attribute
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.year)
        self.assertEqual(self.model,self.avto1.model)
        self.assertIsNotNone(self.avto1.model)

        # i can check values does not exist in this
        self.assertIsNone(self.avto1.price)

        # i can check equal assertEqual
        self.assertEqual(0,self.avto1.get_km())
        self.assertEqual(self.price,self.avto2.price)

        # there is for methods
    def test_set_price(self):
        new_price=45000
        self.avto2.set_price(new_price)
        self.assertEqual(new_price,self.avto2.price)

    def test_add_km(self):
        # i can check plus numbers
        self.avto1.add_km(self.km)
        self.assertEqual(self.km,self.avto1.get_km())
        self.avto1.add_km(5000)
        self.assertEqual(15000, self.avto1.get_km())
        # i can check minus numbers
        new_km=-5000
        try:
            self.avto1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error),ValueError)


    def test_get_info(self):
        avto1_info='GM Malibu, 2020-yil, 0km yurgan.'
        self.assertEqual(avto1_info,self.avto1.get_info())
        # avto1ni narhi va kmni ozgartiramiz
        self.avto1.set_price(50000)
        self.avto1.add_km(200000)
        avto1_info='GM Malibu, 2020-yil, 200000km yurgan.Narhi: 50000'
        self.assertEqual(avto1_info,self.avto1.get_info())



