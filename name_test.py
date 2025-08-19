import unittest
from python_func1 import get_full_name

class NameTest(unittest.TestCase):
    def test_full_name(self):
        name=get_full_name('alijon','valiyev')
        self.assertEqual(name,'Alijon Valiyev')

    def test_otasi_ismi(self):
        name=get_full_name('alijon','valiyev','olimovich')
        self.assertEqual(name,'Alijon Olimovich Valiyev')

if __name__=='__main__':
    unittest.main()











