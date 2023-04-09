import unittest
from my_romanos import decimal_to_roman
from my_decimal import roman_to_decimal

class MyTest(unittest.TestCase):

    def test_1(self):
        resultado = decimal_to_roman(1)
        self.assertEqual(resultado,"I")
    
    def test_cinco(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado,"V")
    
    def test_dos(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado,"II")

    def test_tres(self):
        resultado = decimal_to_roman(3)
        self.assertEqual(resultado,"III")
    
    def test_seis(self):
        resultado = decimal_to_roman(6)
        self.assertEqual(resultado,"VI")
    
    def test_siete(self):
        resultado = decimal_to_roman(7)
        self.assertEqual(resultado,"VII")
    
    def test_ocho(self):
        resultado = decimal_to_roman(8)
        self.assertEqual(resultado, "VIII")
    
    def test_cuatro(self):
        resultado = decimal_to_roman(4)
        self.assertEqual(resultado, "IV")

    def test_nueve(self):
        resultado = decimal_to_roman(9)
        self.assertEqual(resultado,"IX")

    def test_diez(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado,"X")

    def test_24(self):
        resultado = decimal_to_roman(24)
        self.assertEqual(resultado,"XXIV")
    
    def test_37(self):
        resultado = decimal_to_roman(37)
        self.assertEqual(resultado,"XXXVII")

    def test_94(self):
        resultado = decimal_to_roman(94)
        self.assertEqual(resultado,"XCIV")

    def test_105(self):
        resultado = decimal_to_roman(105)
        self.assertEqual(resultado,"CV")

    def test_207(self):
        resultado = decimal_to_roman(207)
        self.assertEqual(resultado,"CCVII")

    def test_462(self):
        resultado = decimal_to_roman(462)
        self.assertEqual(resultado,"CDLXII")

    def test_702(self):
        resultado = decimal_to_roman(702)
        self.assertEqual(resultado,"DCCII")

    def test_999(self):
        resultado = decimal_to_roman(999)
        self.assertEqual(resultado,"CMXCIX")
    
    def test_2500(self):
        resultado = decimal_to_roman(2500)
        self.assertEqual(resultado,"MMD")

    def test_3999(self):
        resultado = decimal_to_roman(3999)
        self.assertEqual(resultado,"MMMCMXCIX")

    def test_2584(self):
        resultado = decimal_to_roman(2584)
        self.assertEqual(resultado,"MMDLXXXIV")

    def test_2831(self):
        resultado = decimal_to_roman(2831)
        self.assertEqual(resultado,"MMDCCCXXXI")

    def test_I(self):
        resultado = roman_to_decimal("I")
        self.assertEqual(resultado,1)

    def test_III(self):
        resultado = roman_to_decimal("III")
        self.assertEqual(resultado,3)

    def test_IV(self):
        resultado = roman_to_decimal("IV")
        self.assertEqual(resultado,4)

    def test_V(self):
        resultado = roman_to_decimal("V")
        self.assertEqual(resultado,5)

    def test_VI(self):
        resultado = roman_to_decimal("VI")
        self.assertEqual(resultado,6)

    def test_CDXXXIV(self):
        resultado = roman_to_decimal("CDXXXIV")
        self.assertEqual(resultado,434)

    def test_MXI(self):
        resultado = roman_to_decimal("MXI")
        self.assertEqual(resultado,1011)

    def test_DLVIII(self):
        resultado = roman_to_decimal("DLVIII")
        self.assertEqual(resultado,558)

if __name__ == "__main__":
    unittest.main()