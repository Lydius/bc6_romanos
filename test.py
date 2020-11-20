from romanos import *
import unittest

class RomanosTest(unittest.TestCase):

    def test_I(self):
        self.assertEqual(romano_a_entero('I'), 1)

    def test_M(self):
        self.assertEqual(romano_a_entero('M'), 1000)
    
    def test_D(self):
        self.assertEqual(romano_a_entero('D'), 500)
    
    def test_C(self):
        self.assertEqual(romano_a_entero('C'), 100)
    
    def test_L(self):
        self.assertEqual(romano_a_entero('L'), 50)
    
    def test_X(self):
        self.assertEqual(romano_a_entero('X'), 10)
    
    def test_V(self):
        self.assertEqual(romano_a_entero('V'), 5)

    def test_J(self):
        self.assertRaises(ValueError, romano_a_entero, 'J')
    
    def test_23(self):
        self.assertRaises(ValueError, romano_a_entero, 23)
    
    def test_MMM(self):
        self.assertEqual(romano_a_entero('MMM'), 3000)

    def test_MMMM(self):
        self.assertRaises(OverflowError, romano_a_entero, 'MMMM')



    
if __name__ == '__main__':
    unittest.main()  
